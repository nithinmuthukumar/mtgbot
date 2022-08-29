import cv2
from pynput.mouse import Button, Controller
from screen_processor import ScreenProcessor
from game import Game
 





if __name__ == "__main__":
    sp = ScreenProcessor()

    game = Game(sp)
    game.play()
    



