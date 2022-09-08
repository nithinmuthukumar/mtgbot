import threading
import cv2
import time
import pyautogui
from screen_processor import ScreenProcessor
from game_state import *

# Make state a main class
# move template matcher to state class?
# extend state and add run function
# inheritance
# game has list of states


class Game:
    def __init__(self, sp):
        self.sp = ScreenProcessor()
        self.state = 0

    def play(self):
        record = threading.Thread(target=self.sp.record_screen, args=())
        record.start()
        time.sleep(2)

        print("Starting")

        self.state = HomeState(self)

        # check if in state
        while not self.state.match():
            pass
        self.state.run()

        self.state = ChooseModeState(self)
        while not self.state.match():
            pass
        self.state.run()

        self.sp.recording = False
        record.join()


# Identify current screen
# do tasks
# Play Button : (1286,830)
# Standard Play: (1166,397)
# First Deck: (369,458)
