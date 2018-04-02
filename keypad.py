from pad4pi import rpi_gpio

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

# define pinout and some config port
ROW_PIN = [4, 14, 15, 17]
COL_PIN = [18, 27, 22, 24]


def print_key(key):
    print(key)


factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PIN, col_pins=COL_PIN)
keypad.registerKeyPressHandler(print_key)
