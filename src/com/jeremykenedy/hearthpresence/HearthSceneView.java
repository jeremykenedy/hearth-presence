package com.jeremykenedy.hearthpresence;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.AssetFileDescriptor;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.SurfaceTexture;
import android.media.MediaPlayer;
import android.media.PlaybackParams;
import android.opengl.GLES11Ext;
import android.opengl.GLES20;
import android.opengl.GLSurfaceView;
import android.opengl.GLUtils;
import android.preference.PreferenceManager;
import android.view.Surface;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.FloatBuffer;
import java.util.HashMap;
import java.util.Random;
import javax.microedition.khronos.egl.EGLConfig;
import javax.microedition.khronos.opengles.GL10;

public final class HearthSceneView extends GLSurfaceView implements GLSurfaceView.Renderer {
  private final HashMap<String, String> settings = new HashMap<>();
  private final FloatBuffer vertices =
      ByteBuffer.allocateDirect(32).order(ByteOrder.nativeOrder()).asFloatBuffer();
  private final float[] matrix = new float[16];
  private final float[] ashParticles = new float[36];
  private final HashMap<String, Integer> uniforms = new HashMap<>();
  private int position;
  private volatile boolean active;
  private boolean frameAvailable;
  private SurfaceTexture video;
  private MediaPlayer player;
  private MediaPlayer sound;
  private int program, texture, width, height;
  private final int[] materialTextures = new int[2];
  private long started;

  public HearthSceneView(Context context) {
    super(context);
    SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(context);
    Random random = new Random();
    boolean all = "true".equals(prefs.getString("randomize_all", "false"));
    for (String[] row : SettingsValues.OPTIONS)
      settings.put(
          row[0], SettingsValues.resolve(row[0], prefs.getString(row[0], row[2]), all, random));
    vertices.put(new float[] {-1, -1, 1, -1, -1, 1, 1, 1}).position(0);
    setEGLContextClientVersion(2);
    setRenderer(this);
    setRenderMode(RENDERMODE_CONTINUOUSLY);
  }

  public void start() {
    active = true;
    onResume();
  }

  public void stop() {
    active = false;
    queueEvent(this::release);
    onPause();
  }

  private void release() {
    if (player != null) {
      player.release();
      player = null;
    }
    if (sound != null) {
      sound.release();
      sound = null;
    }
    if (video != null) {
      video.release();
      video = null;
    }
  }

  private String readShader() {
    try (java.io.InputStream input = getContext().getAssets().open("hearth.frag")) {
      java.io.ByteArrayOutputStream out = new java.io.ByteArrayOutputStream();
      byte[] bytes = new byte[4096];
      int count;
      while ((count = input.read(bytes)) != -1) out.write(bytes, 0, count);
      return out.toString("UTF-8");
    } catch (java.io.IOException e) {
      throw new IllegalStateException(e);
    }
  }

  private int shader(int type, String source) {
    int shader = GLES20.glCreateShader(type);
    GLES20.glShaderSource(shader, source);
    GLES20.glCompileShader(shader);
    int[] ok = new int[1];
    GLES20.glGetShaderiv(shader, GLES20.GL_COMPILE_STATUS, ok, 0);
    if (ok[0] == 0) throw new IllegalStateException(GLES20.glGetShaderInfoLog(shader));
    return shader;
  }

  @Override
  public void onSurfaceCreated(GL10 gl, EGLConfig config) {
    release();
    int vertex =
        shader(
            GLES20.GL_VERTEX_SHADER,
            "attribute vec2 position; varying vec2 uv; void main(){uv=position*.5+.5;gl_Position=vec4(position,0.,1.);}");
    int fragment = shader(GLES20.GL_FRAGMENT_SHADER, readShader());
    program = GLES20.glCreateProgram();
    GLES20.glAttachShader(program, vertex);
    GLES20.glAttachShader(program, fragment);
    GLES20.glLinkProgram(program);
    int[] ok = new int[1];
    GLES20.glGetProgramiv(program, GLES20.GL_LINK_STATUS, ok, 0);
    if (ok[0] == 0) throw new IllegalStateException(GLES20.glGetProgramInfoLog(program));
    uniforms.clear();
    for (String name :
        new String[] {
          "fire",
          "diffuseMap",
          "normalMap",
          "videoMatrix",
          "resolution",
          "time",
          "material",
          "opening",
          "hue",
          "light",
          "ash",
          "gas",
          "drift",
          "frameless",
          "linear",
          "frameThickness",
          "ashParticles[0]"
        }) {
      uniforms.put(name, GLES20.glGetUniformLocation(program, name));
    }
    position = GLES20.glGetAttribLocation(program, "position");
    GLES20.glDeleteShader(vertex);
    GLES20.glDeleteShader(fragment);
    int[] textures = new int[1];
    GLES20.glGenTextures(1, textures, 0);
    texture = textures[0];
    GLES20.glBindTexture(GLES11Ext.GL_TEXTURE_EXTERNAL_OES, texture);
    GLES20.glTexParameteri(
        GLES11Ext.GL_TEXTURE_EXTERNAL_OES, GLES20.GL_TEXTURE_MIN_FILTER, GLES20.GL_LINEAR);
    GLES20.glTexParameteri(
        GLES11Ext.GL_TEXTURE_EXTERNAL_OES, GLES20.GL_TEXTURE_MAG_FILTER, GLES20.GL_LINEAR);
    GLES20.glGenTextures(2, materialTextures, 0);
    String material =
        "frameless".equals(settings.get("surround")) ? "brick" : settings.get("surround");
    loadTexture(materialTextures[0], "materials/" + material + "_diff.jpg");
    loadTexture(materialTextures[1], "materials/" + material + "_normal.jpg");
    video = new SurfaceTexture(texture);
    video.setOnFrameAvailableListener(
        surface -> {
          synchronized (this) {
            frameAvailable = true;
          }
        });
    Surface surface = new Surface(video);
    player = new MediaPlayer();
    try (AssetFileDescriptor asset =
        getResources()
            .openRawResourceFd(
                "linear".equals(settings.get("fuel"))
                    ? R.raw.linear
                    : "gas".equals(settings.get("fuel")) ? R.raw.gas : R.raw.wood)) {
      player.setDataSource(asset.getFileDescriptor(), asset.getStartOffset(), asset.getLength());
      player.setSurface(surface);
      player.setLooping(true);
      player.setVolume(0, 0);
      player.prepare();
      player.setPlaybackParams(
          new PlaybackParams()
              .setSpeed(SettingsValues.playbackSpeed(settings.get("burn_speed")))
              .setPitch(1f));
      if (active) player.start();
    } catch (java.io.IOException e) {
      throw new IllegalStateException("The bundled fire could not play", e);
    } finally {
      surface.release();
    }
    if (!"off".equals(settings.get("crackle"))) {
      sound = MediaPlayer.create(getContext(), R.raw.crackle);
      sound.setLooping(true);
      float volume = "quiet".equals(settings.get("crackle")) ? .15f : .45f;
      sound.setVolume(volume, volume);
      sound.setPlaybackParams(
          new PlaybackParams()
              .setSpeed(SettingsValues.playbackSpeed(settings.get("burn_speed")))
              .setPitch(1f));
      if (active) sound.start();
    }
    started = System.nanoTime();
  }

  private void loadTexture(int textureId, String filename) {
    try (java.io.InputStream stream = getContext().getAssets().open(filename)) {
      Bitmap bitmap = BitmapFactory.decodeStream(stream);
      GLES20.glBindTexture(GLES20.GL_TEXTURE_2D, textureId);
      GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D, GLES20.GL_TEXTURE_MIN_FILTER, GLES20.GL_LINEAR);
      GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D, GLES20.GL_TEXTURE_MAG_FILTER, GLES20.GL_LINEAR);
      GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D, GLES20.GL_TEXTURE_WRAP_S, GLES20.GL_REPEAT);
      GLES20.glTexParameteri(GLES20.GL_TEXTURE_2D, GLES20.GL_TEXTURE_WRAP_T, GLES20.GL_REPEAT);
      GLUtils.texImage2D(GLES20.GL_TEXTURE_2D, 0, bitmap, 0);
      bitmap.recycle();
    } catch (java.io.IOException error) {
      throw new IllegalStateException("The bundled material could not load", error);
    }
  }

  @Override
  public void onSurfaceChanged(GL10 gl, int w, int h) {
    width = w;
    height = h;
    GLES20.glViewport(0, 0, w, h);
  }

  private void uniform(String name, float value) {
    GLES20.glUniform1f(uniforms.get(name), value);
  }

  private float choice(String key, String... values) {
    String selected = settings.get(key);
    for (int i = 0; i < values.length; i++) if (values[i].equals(selected)) return i;
    return 0;
  }

  @Override
  public void onDrawFrame(GL10 gl) {
    GLES20.glClearColor(0, 0, 0, 1);
    GLES20.glClear(GLES20.GL_COLOR_BUFFER_BIT);
    if (!active || video == null) return;
    synchronized (this) {
      if (frameAvailable) {
        video.updateTexImage();
        video.getTransformMatrix(matrix);
        frameAvailable = false;
      }
    }
    GLES20.glUseProgram(program);
    for (int i = 0; i < 2; i++) {
      GLES20.glActiveTexture(GLES20.GL_TEXTURE1 + i);
      GLES20.glBindTexture(GLES20.GL_TEXTURE_2D, materialTextures[i]);
      GLES20.glUniform1i(uniforms.get(i == 0 ? "diffuseMap" : "normalMap"), i + 1);
    }

    GLES20.glActiveTexture(GLES20.GL_TEXTURE0);
    GLES20.glBindTexture(GLES11Ext.GL_TEXTURE_EXTERNAL_OES, texture);
    GLES20.glUniform1i(uniforms.get("fire"), 0);
    GLES20.glUniformMatrix4fv(uniforms.get("videoMatrix"), 1, false, matrix, 0);
    GLES20.glUniform2f(uniforms.get("resolution"), width, height);
    float elapsed = (System.nanoTime() - started) / 1000000000f;
    uniform("time", elapsed);
    for (int i = 0; i < 12; i++) {
      float phase = (elapsed * (.065f + i * .007f) + i * .39f) % 1f;
      ashParticles[i * 3] = (float) (Math.sin(i * 7.13) * .8 + Math.sin(elapsed * .6 + i) * .05);
      ashParticles[i * 3 + 1] = phase * 1.45f - .7f;
      ashParticles[i * 3 + 2] = 1f - phase;
    }
    GLES20.glUniform3fv(uniforms.get("ashParticles[0]"), 12, ashParticles, 0);
    uniform("material", choice("surround", "brick", "white", "classic", "slate", "marble"));
    float frame = choice("frame_width", "thin", "standard", "wide");
    uniform("opening", 1.14f - frame * .18f);
    uniform("frameThickness", .65f + frame * .35f);
    uniform("frameless", "frameless".equals(settings.get("surround")) ? 1 : 0);
    uniform("linear", "linear".equals(settings.get("fuel")) ? 1 : 0);
    uniform("hue", choice("color", "natural", "amber", "blue", "violet"));
    uniform("light", .25f + choice("brightness", "night", "warm", "bright") * .35f);
    uniform("ash", choice("ash", "off", "subtle", "lively") * .5f);
    uniform("gas", "gas".equals(settings.get("fuel")) ? 1 : 0);
    uniform("drift", "off".equals(settings.get("motion")) ? 0 : 1);
    GLES20.glEnableVertexAttribArray(position);
    GLES20.glVertexAttribPointer(position, 2, GLES20.GL_FLOAT, false, 0, vertices);
    GLES20.glDrawArrays(GLES20.GL_TRIANGLE_STRIP, 0, 4);
  }
}
