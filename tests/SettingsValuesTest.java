package com.jeremykenedy.hearthpresence;

import static org.junit.Assert.*;

import java.util.HashSet;
import java.util.Random;
import org.junit.Test;

public class SettingsValuesTest {
  @Test
  public void playbackRatesPreserveNaturalDefaultAndSupportedSpeeds() {
    assertEquals(.75f, SettingsValues.playbackSpeed("slow"), 0f);
    assertEquals(1.25f, SettingsValues.playbackSpeed("lively"), 0f);
    assertEquals(1f, SettingsValues.playbackSpeed("natural"), 0f);
    assertEquals(1f, SettingsValues.playbackSpeed(null), 0f);
    assertEquals(1f, SettingsValues.playbackSpeed("invalid"), 0f);
  }

  @Test
  public void modernLinearGasCanBeSelectedAndSurvivesResolution() {
    assertTrue(SettingsValues.isSupported("fuel", "linear"));
    assertEquals("linear", SettingsValues.resolve("fuel", "linear", false, new Random(4)));
  }

  @Test
  public void acceptsDocumentedChoicesAndRejectsInvalidHostWrites() {
    assertFalse(SettingsValues.isSupported(null, "wood"));
    assertFalse(SettingsValues.isSupported("fuel", null));
    assertFalse(SettingsValues.isSupported("unknown", "wood"));
    for (String[] row : SettingsValues.OPTIONS) {
      assertSame(row, SettingsValues.option(row[0]));
      assertFalse(SettingsValues.isSupported(row[0], "invalid"));
      assertFalse(SettingsValues.isSupported(row[0], ""));
      assertTrue(SettingsValues.isSupported(row[0], row[2]));
      for (int i = 3; i < row.length; i++) assertTrue(SettingsValues.isSupported(row[0], row[i]));
    }
    try {
      SettingsValues.option("missing");
      fail();
    } catch (IllegalArgumentException expected) {
      assertTrue(expected.getMessage().contains("missing"));
    }
  }

  @Test
  public void invalidValuesUseTheDocumentedDefault() {
    for (String[] row : SettingsValues.OPTIONS) {
      assertEquals(row[2], SettingsValues.resolve(row[0], "invalid", false, new Random(4)));
      assertEquals(row[2], SettingsValues.resolve(row[0], null, false, new Random(4)));
      assertEquals(row[2], SettingsValues.resolve(row[0], row[2], false, new Random(4)));
    }
  }

  @Test
  public void randomChoicesResolveToRealModesWithoutPersistingRandom() {
    Random random = new Random(13);
    for (String[] row : SettingsValues.OPTIONS) {
      HashSet<String> seen = new HashSet<>();
      for (int i = 0; i < 200; i++) {
        String chosen = SettingsValues.resolve(row[0], row[2], true, random);
        assertTrue(SettingsValues.isSupported(row[0], chosen));
        assertNotEquals("random", chosen);
        seen.add(chosen);
      }
      if ("random".equals(row[row.length - 1])) {
        assertEquals(row.length - 4, seen.size());
        assertNotEquals("random", SettingsValues.resolve(row[0], "random", false, random));
      } else assertEquals(1, seen.size());
    }
  }
}
