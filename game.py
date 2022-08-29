import threading
import cv2
import time
import pyautogui
from template_matcher import TemplateMatcher
from screen_processor import ScreenProcessor

#Make state a main class
#move template matcher to state class?
#extend state and add run function
#inheritance
#game has list of states
class State:
    def __init__(self,name,accept=[],reject=[]):
        self.name = name
        self.accept = accept
        self.reject = reject
    



class Game:

    def __init__(self,sp):
        self.sp = ScreenProcessor()
        self.tm = TemplateMatcher(self.sp)
        self.state = 0
        self.states = [State("home",["play.png"],["x.png"]),State("play",["play.png","x.png"])]


    def play(self):
        record = threading.Thread(target=self.sp.record_screen, args=())
        record.start()
        time.sleep(2)

        #check if in state
        while not self.tm.match_state(self.states[self.state]):
            time.sleep(0.3)

        time.sleep(3)
        

        #progress to next state 
        pyautogui.click(1286,830)
        print("clicking")

        

        #transition state
        self.state+=1
        print("HOME!")



        
        

        
        

        self.sp.recording = False
        record.join()

#Identify current screen 
#do tasks
#Play Button : (1286,830)
#Standard Play: (1166,397)
#First Deck: (369,458)
