import board
import digitalio
from adafruit_hid.keycode import Keycode

COLUMN_PINS = {
  8: board.GP8,
  9: board.GP9,
  12: board.GP12,
  13: board.GP13,
  14: board.GP14,
  15: board.GP15
}

ROW_PINS = {
  1: board.GP1,
  2: board.GP2,
  3: board.GP3,
  4: board.GP4,
  5: board.GP5,
  6: board.GP6,
  7: board.GP7,
  10: board.GP10,
  11: board.GP11
}

KEYMAP = {
  (8, 5): ('/', Keycode.FORWARD_SLASH),
  (8, 4): (';', Keycode.SEMICOLON),  # does not work
  (8, 1): ('P', Keycode.P),
  (8, 2): ('0', Keycode.ZERO),
  (8, 11): ('Z', Keycode.Z),
  (8, 3): ('A', Keycode.A),
  (8, 10): ('Q', Keycode.Q), # doesn't work most times
  (8, 7): ('1', Keycode.ONE), # does not work

  (13, 5): ('.', Keycode.PERIOD),
  (13, 4): ('L', Keycode.L), # does not work
  (13, 1): ('O', Keycode.O),
  (13, 2): ('9', Keycode.NINE),
  (13, 11): ('X', Keycode.X),
  (13, 3): ('S', Keycode.S),
  (13, 10): ('W', Keycode.W),
  (13, 7): ('2', Keycode.TWO),

  (14, 5): (',', Keycode.COMMA),
  (14, 4): ('K', Keycode.K), # does not work
  (14, 1): ('I', Keycode.I),
  (14, 2): ('8', Keycode.EIGHT),
  (14, 11): ('C', Keycode.C),
  (14, 3): ('D', Keycode.D),
  (14, 10): ('E', Keycode.E),
  (14, 7): ('3', Keycode.THREE),

  (15, 5): ('M', Keycode.M),
  (15, 4): ('J', Keycode.J), # does not work
  (15, 1): ('U', Keycode.U),
  (15, 2): ('7', Keycode.SEVEN),
  (15, 11): ('V', Keycode.V),
  (15, 3): ('F', Keycode.F),
  (15, 10): ('R', Keycode.R),
  (15, 7): ('4', Keycode.FOUR),

  (9, 5): ('N', Keycode.N),
  (9, 4): ('H', Keycode.H), # does not work
  (9, 1): ('Y', Keycode.Y),
  (9, 2): ('6', Keycode.SIX),
  (9, 11): ('B', Keycode.B),
  (9, 3): ('G', Keycode.G),
  (9, 10): ('T', Keycode.T),
  (9, 7): ('5', Keycode.FIVE),

  (12, 5): ('=', Keycode.EQUALS), # does not work
  (12, 4): ('SPACE', Keycode.SPACE), # does not work
  (12, 1): ('ENTER', Keycode.ENTER),
  (12, 2): ('UNUSED', Keycode.F24),
  (12, 11): ('UNUSED', Keycode.F24),
  (12, 3): ('SHIFT', None), # not yet implemented
  (12, 10): ('CONTROL', Keycode.F24), # not yet implemented
  (12, 7): ('FUNCTION', Keycode.F24), # not yet implemented
}

def init_rows():
  rows = {}

  for pin_number, pin in ROW_PINS.items():
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.INPUT
    io.pull = digitalio.Pull.UP
    rows[pin_number] = io

  return rows

def init_columns():
  columns = {}

  for pin_number, pin in COLUMN_PINS.items():
    io = digitalio.DigitalInOut(pin)
    io.direction = digitalio.Direction.OUTPUT
    io.value = True # idle high
    columns[pin_number] = io

  return columns
