

from player_one import Player

class Human(Player):
    def __init__(self,name) -> None:
        super().__init__(name)

    def choose_gesture (self):
        print('Choose 1 for Rock')

        print('Choose 2 for Paper')
        print('Choose 3 for Scissors')
        print('Choose 4 for Lizard')
        print('Choose 5 for Spock')
        print('')
        choice = int(input("Choose your gesture "))


        print('')

        if choice == 1:
            self.selection = "Rock"
            print('You have choosen Rock')
            print('')
        elif choice == 2:
            self.selection = "Paper"
            print('You have chosen Paper')
            print('')
        elif choice == 3:
            self.selection = "Scissors"
            print('You have choosen Scissors')
            print('')
        elif choice == 4:
            self.selection = "Lizard"
            print('You have choosen Lizard')
            print('')
        elif choice == 5:
            self.selection = "Spock"
            print('You have choosen Spock')
            print('')

        else:
            print('Invalid Input. Please make a selection that is 1-5')
            print('')

       

        
