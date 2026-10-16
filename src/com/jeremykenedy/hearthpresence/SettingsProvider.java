package com.jeremykenedy.hearthpresence;

import android.content.*;
import android.database.*;
import android.net.Uri;
import android.preference.PreferenceManager;

public final class SettingsProvider extends ContentProvider {
  private static final String AUTHORITY = "com.jeremykenedy.hearthpresence.settings";

  public boolean onCreate() {
    return true;
  }

  private boolean matches(Uri uri, String path) {
    return AUTHORITY.equals(uri.getAuthority()) && ("/" + path).equals(uri.getPath());
  }

  public Cursor query(Uri uri, String[] projection, String selection, String[] args, String order) {
    if (matches(uri, "schema")) {
      MatrixCursor c =
          new MatrixCursor(
              new String[] {"key", "title", "type", "default", "choices", "randomAllowed"});
      for (String[] row : SettingsValues.OPTIONS)
        c.addRow(
            new Object[] {
              row[0],
              row[1],
              "choice",
              row[2],
              android.text.TextUtils.join("|", java.util.Arrays.copyOfRange(row, 3, row.length)),
              "random".equals(row[row.length - 1])
            });
      return c;
    }
    if (matches(uri, "settings")) {
      MatrixCursor c = new MatrixCursor(new String[] {"key", "value"});
      SharedPreferences p = PreferenceManager.getDefaultSharedPreferences(getContext());
      for (String[] row : SettingsValues.OPTIONS)
        c.addRow(new Object[] {row[0], p.getString(row[0], row[2])});
      return c;
    }
    throw new IllegalArgumentException("Unknown settings URI");
  }

  public int update(Uri uri, ContentValues values, String selection, String[] args) {
    if (!matches(uri, "settings") || values == null)
      throw new IllegalArgumentException("Unknown settings URI");
    String key = values.getAsString("key"), value = values.getAsString("value");
    if (!SettingsValues.isSupported(key, value))
      throw new IllegalArgumentException("Unsupported setting");
    PreferenceManager.getDefaultSharedPreferences(getContext())
        .edit()
        .putString(key, value)
        .apply();
    return 1;
  }

  public String getType(Uri uri) {
    return matches(uri, "schema") || matches(uri, "settings")
        ? "vnd.android.cursor.dir/vnd.hearthpresence.setting.v1"
        : null;
  }

  public Uri insert(Uri uri, ContentValues values) {
    throw new UnsupportedOperationException();
  }

  public int delete(Uri uri, String selection, String[] args) {
    throw new UnsupportedOperationException();
  }
}
