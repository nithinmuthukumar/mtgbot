import cv2
import mss
import numpy as np
import time
import pytesseract

monitor = {"top": 0, "left": 0, "width": 1440, "height": 900}


class ScreenProcessor:
    def __init__(self):
        self.stc = mss.mss()
        self.recording = False
        self.last_shot = None

    def screen_shot(self,m = monitor):
        screen = self.stc.grab(m)
        img = np.array(screen)
        img = cv2.cvtColor(img, cv2.IMREAD_COLOR)
        return img

    def record_screen(self):
        self.recording = True

        while self.recording:

            self.last_shot = self.screen_shot()
    def read_screen(self,x1,x2,y1,y2):
        cv2.imwrite("sc.png",self.last_shot[y1*2:y2*2,x1*2:x2*2])
        print(self.last_shot.shape)
        return pytesseract.image_to_string(self.last_shot[y1*2:y2*2,x1*2:x2*2])

