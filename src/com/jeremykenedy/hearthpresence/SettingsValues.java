package com.jeremykenedy.hearthpresence;

import java.util.Random;

public final class SettingsValues {
  public static final String[][] OPTIONS = {
    {
      "surround",
      "Surround",
      "brick",
      "brick",
      "white",
      "classic",
      "slate",
      "marble",
      "frameless",
      "random"
    },
    {"fuel", "Fire type", "wood", "wood", "gas", "linear", "random"},
    {"flame_size", "Flame height", "medium", "small", "medium", "large", "random"},
    {"frame_width", "Frame width", "standard", "thin", "standard", "wide", "random"},
    {"burn_speed", "Burn speed", "natural", "slow", "natural", "lively", "random"},
    {"color", "Flame color", "natural", "natural", "amber", "blue", "violet", "random"},
    {"brightness", "Room lighting", "warm", "night", "warm", "bright", "random"},
    {"ash", "Drifting ash", "subtle", "off", "subtle", "lively", "random"},
    {"crackle", "Crackle sound", "off", "off", "quiet", "lively", "random"},
    {"motion", "Protective camera drift", "gentle", "gentle", "off"},
    {"randomize_all", "Randomize each start", "false", "false", "true"}
  };

  private SettingsValues() {}

  public static float flameScale(String value) {
    if ("small".equals(value)) return .65f;
    if ("large".equals(value)) return 1.3f;
    return 1f;
  }

  public static float playbackSpeed(String value) {
    if ("slow".equals(value)) return .75f;
    if ("lively".equals(value)) return 1.25f;
    return 1f;
  }

  public static String[] option(String key) {
    for (String[] row : OPTIONS) if (row[0].equals(key)) return row;
    throw new IllegalArgumentException("Unknown setting: " + key);
  }

  public static boolean isSupported(String key, String value) {
    if (key == null || value == null) return false;
    for (String[] row : OPTIONS) {
      if (row[0].equals(key)) {
        for (int i = 3; i < row.length; i++) if (row[i].equals(value)) return true;
        return false;
      }
    }
    return false;
  }

  public static String resolve(String key, String value, boolean randomize, Random random) {
    String[] row = option(key);
    if (!isSupported(key, value)) value = row[2];
    if ((randomize || "random".equals(value)) && "random".equals(row[row.length - 1]))
      return row[3 + random.nextInt(row.length - 4)];
    return value;
  }
}
