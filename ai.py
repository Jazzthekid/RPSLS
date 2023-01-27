from player_one import Player
import random

class AI(Player):
    def __init__(self,name):
        super().__init__(name)

    def choose_gesture (self):
        self.selection = random.choice(self.gestures)
        print(f'{self.name} has chosesn {self.selection}')
        # choice = random.randint (1,5)
        # if choice == 1:
        #     print('Player Two chose Rock')
        # elif choice == 2:
        #     print('Player Two chose Paper')
        # elif choice == 3:
        #     print('Player Two chose Scissors')
        # elif choice == 4:
        #     print('Player Two chose Lizard')
        # elif choice == 5:
        #     print('Player Two have chose Spock')

        # return choice



