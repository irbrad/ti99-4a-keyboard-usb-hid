import time

class KeyScanner:
  def __init__(self, rows, columns, keymap, keyboard, sleep=0.01):
    self.rows = rows
    self.columns = columns
    self.keymap = keymap
    self.keyboard = keyboard
    self.sleep = sleep
    self.state = {}  # tracks pressed state

  def scan_once(self):
    for column_number, column_io in self.columns.items():
      column_io.value = False  # pull this column low
      time.sleep(0.001)

      for row_number, row_io in self.rows.items():
        key = (column_number, row_number)
        is_pressed = not row_io.value  # active low

        if is_pressed:
          if not self.state.get(key, False):
            self._on_press(key)
            self.state[key] = True
        else:
          if self.state.get(key, False):
            self._on_release(key)
            self.state[key] = False

      column_io.value = True  # return column high

    time.sleep(self.sleep)

  def _on_press(self, key):
    if key in self.keymap:
      char, keycode = self.keymap[key]
      print(f"key pressed: {char} (col {key[0]}, row {key[1]})")

      self.keyboard.press(keycode)
    else:
      print(f"key pressed: unknown (col {key[0]}, row {key[1]})")

  def _on_release(self, key):
    if key in self.keymap:
      char, keycode = self.keymap[key]
      print(f"key released: {char} (col {key[0]}, row {key[1]})")

      self.keyboard.release(keycode)
    else:
      print(f"key released: unknown (col {key[0]}, row {key[1]})")
