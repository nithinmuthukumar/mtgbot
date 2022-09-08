from abc import ABC, abstractmethod
import cv2
import time

import pyautogui


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    time.sleep(0.5)  # or whatever you need, if even needed
    pyautogui.mouseUp()


class GameState(ABC):
    def __init__(self, game, accept=[], reject=[]):
        # criteria for template matching
        self.accept = accept
        self.reject = reject
        self.game = game

    @abstractmethod
    def run(self):
        pass

    def match(self):
        accept = [
            cv2.imread(f"templates/{path}", cv2.IMREAD_COLOR) for path in self.accept
        ]
        reject = [
            cv2.imread(f"templates/{path}", cv2.IMREAD_COLOR) for path in self.reject
        ]
        for template in accept:
            res = cv2.matchTemplate(self.game.sp.last_shot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val < 0.8:
                return False
        for template in reject:
            res = cv2.matchTemplate(self.game.sp.last_shot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.8:
                return False
        return True


class HomeState(GameState):
    def __init__(self, game):
        super().__init__(game, ["play.png"], ["x.png"])

    def run(self):

        mission = self.game.sp.read_screen(565,670,700,750)
        if "black" in mission:
            print(True)
        click(1286, 830)
        pyautogui.moveTo(1, 1)


class ChooseModeState(GameState):
    def __init__(self, game):
        super().__init__(game, ["play.png", "x.png"])

    def run(self):
        click(1286, 830)
