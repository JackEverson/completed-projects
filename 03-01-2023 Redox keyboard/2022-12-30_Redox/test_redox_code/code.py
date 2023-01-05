#Note that this project is being scrapped and left as a left hand only code. The new development will be focused on getting a two handed, one microcontroller keyboard working.
print("Starting")

#importing circuit python "board" ability to use GPIO pins.
import board

#General KMK keyboard import 
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

#Importing layers for KMK
from kmk.modules.layers import Layers
keyboard.modules.append(Layers())

keyboard = KMKKeyboard()

#Redox has 7 columns on left and 7 columns on right (total 14, left to right) and 5 rows, as it is COL2ROW diodes the 1N4148 diodes attach to the rows with the black side of the diode attached to the row (not the switch)
keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3,board.GP4,board.GP5,board.GP6,         board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13)
#Columns left to right      1         2         3         4         5         6         7   |split|         8         9        10         11        12          13         14                 

keyboard.row_pins = (board.GP14,board.GP15,board.GP16,board.GP17,board.GP18)
#Rows top to bottom         1           2           3         4          5

keyboard.diode_orientation = DiodeOrientation.COL2ROW

#easier to see function, empty, and transpartent keys
XXXXX = KC.NO
_____ = KC.TRNS
FN_Layer = KC.MO(1)
Num_Layer = KC.MO(2)


keyboard.keymap = [
    [#layer 0: Base layer
    KC.ESC,    KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,      XXXXX,                          KC.PGUP,    KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.MINUS,

    KC.TAB,    KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,       XXXXX,                          KC.PGDN,    KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,       KC.LBRC,

    KC.CAPS,   KC.A,       KC.S,       KC.D,       KC.F,       KC.G,       XXXXX,                          KC.END,     KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,    KC.QUOTE,

    KC.LSHIFT, KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,       XXXXX,                          KC.HOME,    KC.N,       KC.M,       KC.COMMA,   KC.DOT,     KC.SLSH,    KC.RSHIFT,

    KC.LCTRL,  KC.LGUI,    FN_Layer,   XXXXX,      KC.LALT,    KC.ENTER,   KC.SPACE,                       KC.BSPC,    KC.DEL,     Num_Layer,  KC.LEFT,    KC.DOWN,    KC.UP,      KC.RIGHT,
    ],

    [#layer 1: Functions layer
    KC.TILD,  KC.F1,      KC.F2,      KC.F3,      KC.F4,      KC.F5,       KC.F6,                          KC.F7,    KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,      KC.EQUAL,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       KC.RBRC,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    ],

    [#Layer 2: Number layer
    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    ],


'''
#template transparent layer incase I want to add more layers
    [
    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    _____,    _____,      _____,      _____,      _____,      _____,       _____,                          _____,    _____,      _____,      _____,      _____,      _____,       _____,

    ],

'''
    ]




if __name__ == '__main__':
    keyboard.go()
