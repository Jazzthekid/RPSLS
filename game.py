from human_player import Human
from ai import AI

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
      
        


    def welcome(self):
        print('')
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')

    def rules(self):
        print('This game will be played in rounds! Whoever wins the best out of three wins the game! Each selection is paired with a number.')
        print('')
        print('Rock crushes Scissors')
        print('Scissors Cuts Paper')
        print('Paper Covers Rock')
        print('Rock crushes Lizard')
        print('Lizard poisons Spock')
        print('Spock smashes Scissors')
        print('Scissors decapitiates Lizard')
        print('Lizard eats paper')
        print('Paper disproves Spock')
        print('Spock vaporizes Rock')


    def choose_player(self):
        print('')
        user_choice = input('Press 1 for single player or 2 for muli-player ')
        if user_choice == "1":
            p_one_name = input("what is player ones name?")
            self.player_one = Human(p_one_name)
            self.player_two = AI("Bob")
        if user_choice == "2":
            p_one_name = input("What is player ones name? ")
            self.player_one = Human(p_one_name)
            print('')
            p_two_name = input("What is player twos name? ")
            print('')
            self.player_two = Human(p_two_name)

    def play_rounds(self):
        # while loop here but make sure you can get throgh an entire hand before trying to add this
        # loop while player one score is less than 2 and player two score is less than 2
        while self.player_one.score <2 and self.player_two.score <2:
        
        
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.selection == self.player_two.selection:
                print("its a tie, keep playing")
            elif self.player_one.selection == "Rock" and self.player_two.selection == "Scissors":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                self.player_one.score += 1 
            elif self.player_one.selection == "Scissors" and self.player_two.selection == "Paper":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                self.player_one.score += 1 

            elif self.player_one.selection == "Paper" and self.player_two.selection == "Rock":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                self.player_one.score += 1 

            elif self.player_one.selection == "Rock" and self.player_two.selection == "Lizard":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                self.player_one.score += 1 

            elif self.player_one.selection == "Lizard" and self.player_two.selection == "Spock":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            elif self.player_one.selection == "Spock" and self.player_two.selection == "Scissors":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            elif self.player_one.selection == "Scissors" and self.player_two.selection == "Lizard":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 
    
            elif self.player_one.selection == "Lizard" and self.player_two.selection == "Paper":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 
            
            elif self.player_one.selection == "Paper" and self.player_two.selection == "Spock":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            elif self.player_one.selection == "Spock" and self.player_two.selection == "Rock":
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            
            else:
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1
            
    
    def run_game(self):
            self.welcome()
            self.rules()
            self.choose_player()
            self.play_rounds()

