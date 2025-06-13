import usb_hid
from adafruit_hid.keyboard import Keyboard
from keyboard import init_rows, init_columns, KEYMAP, KeyScanner

rows = init_rows()
columns = init_columns()

keyboard = Keyboard(usb_hid.devices)
scanner = KeyScanner(rows, columns, KEYMAP, keyboard)

pressed_state = {}

while True:
  scanner.scan_once()
