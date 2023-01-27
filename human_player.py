import time

from player_one import Player

class Human(Player):
    def __init__(self,name) -> None:
        super().__init__(name)

    def choose_gesture (self):
        print('Choose 1 for Rock')
        time.sleep(.3)
        print('Choose 2 for Paper')
        time.sleep(.3)
        print('Choose 3 for Scissors')
        time.sleep(.3)
        print('Choose 4 for Lizard')
        time.sleep(.3)
        print('Choose 5 for Spock')
        time.sleep(.3)
        print('')
        


        print('')
        valid_choice = False
        while valid_choice == False:
            choice = int(input("Choose your gesture "))
            if choice == 1:
                self.selection = "Rock"
                print('You have choosen Rock')
                valid_choice = True
                print('')
            elif choice == 2:
                self.selection = "Paper"
                print('You have chosen Paper')
                valid_choice =True
                print('')
            elif choice == 3:
                self.selection = "Scissors"
                print('You have choosen Scissors')
                valid_choice = True
                print('')
            elif choice == 4:
                self.selection = "Lizard"
                print('You have choosen Lizard')
                valid_choice = True
                print('')
            elif choice == 5:
                self.selection = "Spock"
                print('You have choosen Spock')
                valid_choice = True
                print('')

            else:
                print('Invalid Input. Please make a selection that is 1-5')
                valid_choice = False
                print('')
       

        
