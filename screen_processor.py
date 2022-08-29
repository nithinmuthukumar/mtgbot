import cv2
import mss
import numpy as np

monitor = {"top": 0, "left": 0, "width": 1440, "height": 900}

class ScreenProcessor:


    def __init__(self):
        self.stc = mss.mss()
        self.recording = False
        self.last_shot = None
        
    def screen_shot(self):
        screen = self.stc.grab(monitor)
        img = np.array(screen)
        img = cv2.cvtColor(img,cv2.IMREAD_COLOR)
        return img
    def record_screen(self):
        self.recording = True

        while self.recording:

            self.last_shot = self.screen_shot()

