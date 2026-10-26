package com.jeremykenedy.hearthpresence;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.View;
import android.widget.*;

public final class SettingsActivity extends Activity {
  private Spinner flameHeight;

  private String[] labels(String[] values) {
    String[] labels = new String[values.length];
    for (int i = 0; i < values.length; i++) {
      String value = values[i];
      if ("gas".equals(value)) {
        labels[i] = "Traditional gas";
        continue;
      }
      if ("linear".equals(value)) {
        labels[i] = "Modern linear gas";
        continue;
      }
      labels[i] =
          "true".equals(value)
              ? "Enabled"
              : "false".equals(value)
                  ? "Disabled"
                  : Character.toUpperCase(value.charAt(0)) + value.substring(1);
    }
    return labels;
  }

  @Override
  public void onCreate(Bundle state) {
    super.onCreate(state);
    SharedPreferences prefs = PreferenceManager.getDefaultSharedPreferences(this);
    ScrollView scroll = new ScrollView(this);
    LinearLayout content = new LinearLayout(this);
    content.setOrientation(LinearLayout.VERTICAL);
    content.setPadding(64, 32, 64, 48);
    content.setBackgroundColor(0xff171310);
    scroll.addView(content);
    TextView title = new TextView(this);
    title.setText("Hearth Presence");
    title.setTextSize(32);
    content.addView(title);
    TextView description = new TextView(this);
    description.setText("A real fire, your own fireplace. Choose a surround and settle in.");
    description.setTextSize(18);
    description.setPadding(0, 8, 0, 20);
    content.addView(description);
    Button preview = new Button(this);
    preview.setText("Open fireplace");
    preview.setOnClickListener(v -> startActivity(new Intent(this, PreviewActivity.class)));
    content.addView(preview);
    for (String[] row : SettingsValues.OPTIONS) {
      TextView label = new TextView(this);
      label.setText(row[1]);
      label.setTextSize(20);
      label.setPadding(0, 18, 0, 4);
      content.addView(label);
      String[] values = java.util.Arrays.copyOfRange(row, 3, row.length);
      Spinner spinner = new Spinner(this);
      spinner.setMinimumHeight(54);
      spinner.setFocusable(true);
      if ("flame_size".equals(row[0])) {
        flameHeight = spinner;
        spinner.setEnabled(!"gas".equals(prefs.getString("fuel", "wood")));
      }
      ArrayAdapter<String> adapter =
          new ArrayAdapter<>(this, android.R.layout.simple_spinner_item, labels(values));
      adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
      spinner.setAdapter(adapter);
      String selected = prefs.getString(row[0], row[2]);
      for (int i = 0; i < values.length; i++)
        if (values[i].equals(selected)) spinner.setSelection(i);
      spinner.setOnItemSelectedListener(
          new AdapterView.OnItemSelectedListener() {
            public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
              prefs.edit().putString(row[0], values[position]).apply();
              if ("fuel".equals(row[0]) && flameHeight != null)
                flameHeight.setEnabled(!"gas".equals(values[position]));
            }

            public void onNothingSelected(AdapterView<?> parent) {}
          });
      content.addView(spinner);
    }
    Button credits = new Button(this);
    credits.setText("Credits and licenses");
    credits.setOnClickListener(view -> CreditsDialog.show(this));
    content.addView(credits);
    setContentView(scroll);
    preview.requestFocus();
  }
}
