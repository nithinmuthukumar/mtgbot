
import cv2

class TemplateMatcher:
    def __init__(self, sp):
        self.sp = sp

    def match_state(self,state):
        accept = [cv2.imread(f"templates/{path}",cv2.IMREAD_COLOR)
                for path in state.accept]
        reject = [cv2.imread(f"templates/{path}",cv2.IMREAD_COLOR)
                for path in state.reject]
        for template in accept:
            res = cv2.matchTemplate(self.sp.last_shot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val<.8:
                return False
        for template in reject:
            res = cv2.matchTemplate(self.sp.last_shot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val>.8:
                return False

        

            


        return True

        # for template in templates:


        #     res = cv2.matchTemplate(sp.last_shot, template, cv2.TM_CCOEFF_NORMED)
        #     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # return max_val>.8

