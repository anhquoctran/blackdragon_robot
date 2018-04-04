import RPi.GPIO as GPIO
import time
from pad4pi import rpi_gpio
from RPLCD.i2c import CharLCD

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

# define pinout and some config port
ROW_PIN = [24, 22, 27, 18]
COL_PIN = [17, 15, 14, 4]
KEY_ACCEPT = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
KEY_CONTROL = ['A', 'B', 'C', 'D']

I2C_ADDR = 0x3f

lcd = CharLCD(i2c_expander='PCF8574', address=I2C_ADDR, cols=16, rows=4)
lcd.clear()
lcd.cursor_pos = (0, 1)
lcd.write_string("ENTER PASSCODE")

GPIO.setwarnings(False)
factory = rpi_gpio.KeypadFactory()
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PIN, col_pins=COL_PIN)
# keypad.registerKeyPressHandler(print_key)

lcd.cursor_pos = (1, 6)
lcd.cursor_mode = 'hide'
passcode = ""
count = 0


def print_key(key):
    global count
    global passcode

    inp = str(key)

    if inp in KEY_ACCEPT:
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
    global passcode

    st = passcode[:-1]
    print(lcd.cursor_pos[1])
    lcd.cursor_pos = (1, lcd.cursor_pos[1]-1)
    lcd.write_string('')
    print(st)
    lcd.cursor_pos = (1, 0)
    for ch in st:
        lcd.write_string('*')
    passcode = st


while True:
    keypad.registerKeyPressHandler(print_key)
    time.sleep(100)
