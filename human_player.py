from player_one import Player

class Human(Player):
    def __init__(self) -> None:
        super().__init__()

    def selection (self):
        print('Choose 1 for Rock')
        print('Choose 2 for Paper')
        print('Choose 3 for Scissors')
        print('Choose 4 for Lizard')
        print('Choose 5 for Spock')
        print('')
        choice = int(input("Choose your gesture"))

        if choice == 1:
            print('You have choosen Rock')
        elif choice == 2:
            print('You have chosen Paper')
        elif choice == 3:
            print('You have choosen Scissors')
        elif choice == 4:
            print('You have choosen Lizard')
        elif choice == 5:
            print('You have choosen Spock')

        else:
            print('Invalid Input. Please make a selection that is 1-5')

user_choice = Human()
print(user_choice)
        
