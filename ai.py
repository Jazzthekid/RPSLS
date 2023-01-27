import time
from player_one import Player
import random

class AI(Player):
    def __init__(self,name):
        super().__init__(name)

    def choose_gesture (self):
        self.selection = random.choice(self.gestures)
        time.sleep(.3)
        print(f'{self.name} has chosesn {self.selection}')
        time.sleep(.3)
        print('')
       


