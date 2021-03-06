import cv2 as cv
import sys
import time
import numpy as np
import Adafruit_SSD1306
import RPi.GPIO as GPIO

from pad4pi import rpi_gpio
from PIL import Image
from icon_path_const import IconPathConstants

auto = False
locked = False

KEYPAD = [
    [1, 2, 3, "A"],
    [4, 5, 6, "B"],
    [7, 8, 9, "C"],
    ["*", 0, "#", "D"]
]

# define pinout and some config port
ROW_PIN = [4,14,15,17]
COL_PIN = [18,27,22,24]
ADDRESS = 0x27
RST_PIN = 24
DC = 23
LED = 0
MOTOR = 0
BUZZER = 1
disp = None
keypad = None

def setup() :
    """
    Setting up program with some configuration
    """

    GPIO.setwarning(False)
    GPIO.setmode(GPIO.BOARD)

    setup_led_blink()
    setup_motor()
    
    setup_keypad()
    setup_display()
    
    
def setup_display():
    disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST_PIN)
    disp.begin()

def setup_keypad():
    factory = rpi_gpio.KeypadFactory()
    keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PIN, col_pins=COL_PIN)
    keypad.registerKeyPressHandler(print_key)

def setup_led_blink() :
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)

def setup_motor():
    GPIO.setup(MOTOR, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)

def print_key(key):
    """
    Handling keypad pressed callback
    """

    res = False

    #press 1
    if key == KEYPAD[0][0]:
        
        res = True

    #press 2
    elif key == KEYPAD[0][1]:
        
        res = True
    #press 3
    elif key == KEYPAD[0][2]:
        
        res = True

    #press 4
    elif key == KEYPAD[1][0]:
        
        res = True

    #press 5
    elif key == KEYPAD[1][1]:
        
        res = True

    #press 6
    elif key == KEYPAD[1][2]:
        
        res = True

    #press 7
    elif key == KEYPAD[2][0]:
        
        res = True

    #press 8
    elif key == KEYPAD[2][1]:
        
        res = True

    #press 9
    elif key == KEYPAD[2][2]:
        
        res = True

    #press * - Back button
    elif key == KEYPAD[3][0]:
        
        res = True

    #press 0
    elif key == KEYPAD[3][1]:
        
        res = True
    
    #press # - Next
    elif key == KEYPAD[3][2]:
        
        res = True

    #press A - OK button
    elif key == KEYPAD[0][3]:
        
        res = True

    #press B - Cancel button
    elif key == KEYPAD[1][3]:
        
        res = True

    #press C - Clear screen if enter mode
    elif key == KEYPAD[2][3]:
    
        res = True

    #press D
    elif key == KEYPAD[3][3]:
        
        res = True

    else :
        res = False

    return res
        

def display_content(content, x ,y):
    """
    Display content to OLED screen
    """
    return True

def clear_and_display_content(content, x, y):
    disp.clear()
    display_content(content, x, y)

def if_image(data):
    """
    Validate an image file
    """
    print("image")

def line_detect():
    """
    Peform line detection
    """

    print("line")

def move(x,y):
    """
    Moving the Robot by coordinates X, Y
    """

    return

def rotate(angleX, angleY):
    """
    Rotating the Robot by angle
    """

    return angleX * angleY / 2

def start_camera():
    """
    Initialize camera
    """

    capture = cv.VideoCapture(0)
    capture.set(3,320.0) #set the size
    capture.set(4,240.0)  #set the size
    capture.set(5,15)
    for i in range(0,2):
        flag, trash = capture.read()
    
    return capture

if __name__ == '__main__':
    setup()
