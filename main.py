import sys
import time
import cv2
import numpy as np
import mss
from pynput.mouse import Button, Controller
import os
import threading

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
            last_time = time.time()
            self.last_shot = self.screen_shot()
            # print("fps: {}".format(1 / (time.time() - last_time)))
        print(self.recording)
sp = ScreenProcessor()

##DONT NEED template matching for most things. Use coordinates:

 
play_img = cv2.imread('templates/play.png', cv2.IMREAD_COLOR)

#TODO check the section of the screen where the template could happen.
#extremely slow currently
def match_play():
    res = cv2.matchTemplate(sp.last_shot, play_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if max_val>.8:
        print(min_val,max_val,min_loc,max_loc)






    

record = threading.Thread(target=sp.record_screen, args=())
record.start()
while True:
    if sp.last_shot is not None:
        cv2.imshow("o",sp.last_shot)
        match_play()


    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()

        break

sp.recording = False
record.join()


