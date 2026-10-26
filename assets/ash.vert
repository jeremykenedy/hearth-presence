precision highp float;
attribute vec3 spark;
uniform vec2 resolution;
uniform float time;
uniform float drift;
varying vec3 particle;
void main(){
 float breathe=1.+.004*sin(time*.019)*drift;
 vec2 translation=drift*vec2(.012*sin(time*.013),.008*cos(time*.017));
 vec2 p=(spark.xy-translation)/breathe;
 gl_Position=vec4(p.x*resolution.y/resolution.x,p.y,0.,1.);
 // Cover the original elliptical particle, including its outer antialias pixels.
 gl_PointSize=resolution.y/210.+2.;
 particle=spark;
}
