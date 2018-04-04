import RPi.GPIO as GPIO
import time
from pad4pi import rpi_gpio
from RPLCD.i2c import CharLCD
import numpy as np

# keypad array definition
KEYPAD = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

# define keypad pin header and keycaps
ROW_PIN = [24, 22, 27, 18]
COL_PIN = [17, 15, 14, 4]
KEY_ACCEPT = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
KEY_CONTROL = ['A', 'B', 'C', 'D']

# i2c address, get it from i2cdetect -y 1
I2C_ADDR = 0x3f

# init lcd i2c module, using PCF8574 expander with new address 0x3f, 16 cols x 4 rows
lcd = CharLCD(i2c_expander='PCF8574', address=I2C_ADDR, cols=16, rows=4)
lcd.clear()
lcd.cursor_pos = (0, 1)
lcd.write_string("ENTER PASSCODE")
lcd.cursor_pos = (1, 6)
lcd.cursor_mode = 'hide'

# disable gpio warning notification
GPIO.setwarnings(False)

# init keypad
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PIN, col_pins=COL_PIN)
# keypad.registerKeyPressHandler(print_key)


passcode = ""
count = 0


def print_key(key):
    # print key callback

    global count
    global passcode

    inp = str(key)

    if inp in KEY_ACCEPT:

        # print key callback

        if count < 4:
            lcd.write_string('*')
            passcode += inp
            count += 1
        else:
            print("Maximum char allowed!")

    elif inp in KEY_CONTROL:
        if inp == 'C':
            # count = 0
            print("Cleared")
            # clear_one_char()
        elif inp == 'A':
            if auth(passcode):
                print("Authenticated")
            else:
                print("Permission denied")
        elif inp == 'B':
            print("Cancelled")


def auth(p):
    if p == '19081996':
        return True
    else:
        return False


def clear_one_char():
    pass
    # global passcode
    #
    # st = passcode[:-1]
    # print(lcd.cursor_pos[1])
    # lcd.cursor_pos = (1, lcd.cursor_pos[1]-1)
    # lcd.write_string('')
    # print(st)
    # lcd.cursor_pos = (1, 0)
    # for ch in st:
    #     lcd.write_string('*')
    # passcode = st


while True:
    # loop to listen keypad pressed event
    keypad.registerKeyPressHandler(print_key)
    time.sleep(100)
