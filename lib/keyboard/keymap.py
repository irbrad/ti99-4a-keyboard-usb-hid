import board
import digitalio
from adafruit_hid.keycode import Keycode

COLUMN_PINS = {
  "1Y1": board.GP8,
  "1Y0": board.GP9,
  "2Y0": board.GP12,
  "2Y1": board.GP13,
  "2Y2": board.GP14,
  "2Y3": board.GP15
}

ROW_PINS = {
  "INT5": board.GP1,
  "INT6": board.GP2,
  "INT8": board.GP3,
  "INT4": board.GP4,
  "INT3": board.GP5,
  "P5": board.GP6,
  "INT7": board.GP7,
  "INT9": board.GP10,
  "INT10": board.GP11
}

KEYMAP = {
  ("1Y1", "INT3"): ('/', Keycode.FORWARD_SLASH),
  ("1Y1", "INT4"): (';', Keycode.SEMICOLON), # FIXME: does not work, probably my keyboard
  ("1Y1", "INT5"): ('P', Keycode.P),
  ("1Y1", "INT6"): ('0', Keycode.ZERO),
  ("1Y1", "INT10"): ('Z', Keycode.Z),
  ("1Y1", "INT8"): ('A', Keycode.A),
  ("1Y1", "INT9"): ('Q', Keycode.Q), # FIXME: doesn't work most times, probably my keyboard
  ("1Y1", "INT7"): ('1', Keycode.ONE), # FIXME: does not work, probably my keyboard

  ("2Y1", "INT3"): ('.', Keycode.PERIOD),
  ("2Y1", "INT4"): ('L', Keycode.L), # FIXME: does not work, probably my keyboard
  ("2Y1", "INT5"): ('O', Keycode.O),
  ("2Y1", "INT6"): ('9', Keycode.NINE),
  ("2Y1", "INT10"): ('X', Keycode.X),
  ("2Y1", "INT8"): ('S', Keycode.S),
  ("2Y1", "INT9"): ('W', Keycode.W),
  ("2Y1", "INT7"): ('2', Keycode.TWO),

  ("2Y2", "INT3"): (',', Keycode.COMMA),
  ("2Y2", "INT4"): ('K', Keycode.K), # FIXME: does not work, probably my keyboard
  ("2Y2", "INT5"): ('I', Keycode.I),
  ("2Y2", "INT6"): ('8', Keycode.EIGHT),
  ("2Y2", "INT10"): ('C', Keycode.C),
  ("2Y2", "INT8"): ('D', Keycode.D),
  ("2Y2", "INT9"): ('E', Keycode.E),
  ("2Y2", "INT7"): ('3', Keycode.THREE),

  ("2Y3", "INT3"): ('M', Keycode.M),
  ("2Y3", "INT4"): ('J', Keycode.J), # FIXME: does not work, probably my keyboard
  ("2Y3", "INT5"): ('U', Keycode.U),
  ("2Y3", "INT6"): ('7', Keycode.SEVEN),
  ("2Y3", "INT10"): ('V', Keycode.V),
  ("2Y3", "INT8"): ('F', Keycode.F),
  ("2Y3", "INT9"): ('R', Keycode.R),
  ("2Y3", "INT7"): ('4', Keycode.FOUR),

  ("1Y0", "INT3"): ('N', Keycode.N),
  ("1Y0", "INT4"): ('H', Keycode.H), # FIXME: does not work, probably my keyboard
  ("1Y0", "INT5"): ('Y', Keycode.Y),
  ("1Y0", "INT6"): ('6', Keycode.SIX),
  ("1Y0", "INT10"): ('B', Keycode.B),
  ("1Y0", "INT8"): ('G', Keycode.G),
  ("1Y0", "INT9"): ('T', Keycode.T),
  ("1Y0", "INT7"): ('5', Keycode.FIVE),

  ("2Y0", "INT3"): ('=', Keycode.EQUALS), # FIXME: does not work
  ("2Y0", "INT4"): ('SPACE', Keycode.SPACE), # FIXME: does not work
  ("2Y0", "INT5"): ('ENTER', Keycode.ENTER),
  ("2Y0", "INT6"): ('UNUSED', Keycode.F24),
  ("2Y0", "INT10"): ('UNUSED', Keycode.F24),
  ("2Y0", "INT8"): ('SHIFT', None), # FIXME: not yet implemented
  ("2Y0", "INT9"): ('CONTROL', Keycode.F24), # FIXME: not yet implemented
  ("2Y0", "INT7"): ('FUNCTION', Keycode.F24), # FIXME: not yet implemented
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
