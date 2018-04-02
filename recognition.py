import cv2 as cv
import numpy as np


class Recognition(object):

    @staticmethod
    def __init_camera():
        """
        Initialize camera
        """

        cap = cv.VideoCapture(0)
        cap.set(cv.CAP_PROP_FRAME_WIDTH, 800)
        cap.set(cv.CAP_PROP_FRAME_HEIGHT, 600)
        cap.set(5, 15)

        return cap

    @staticmethod
    def init_recog():
        cap = Recognition.__init_camera()
        while True:
            ret, frame = cap.read()
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    def _init__(self, *args):
        super(Recognition, self).__init__(*args)
