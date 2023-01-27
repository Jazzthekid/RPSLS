import time

from human_player import Human
from ai import AI

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
      
        


    def welcome(self):
        print('')
        print('Welcome to Rock, Paper, Scissors, Lizard, Spock')
        time.sleep(.3)

    def rules(self):
        time.sleep(.5)
        print('This game will be played in rounds! Whoever wins the best out of three wins the game! Each selection is paired with a number.')
        time.sleep(.5)
        print('')
        print('Rock crushes Scissors')
        time.sleep(.3)
        print('Scissors Cuts Paper')
        time.sleep(.3)
        print('Paper Covers Rock')
        time.sleep(.3)
        print('Rock crushes Lizard')
        time.sleep(.3)
        print('Lizard poisons Spock')
        time.sleep(.3)
        print('Spock smashes Scissors')
        time.sleep(.3)
        print('Scissors decapitiates Lizard')
        time.sleep(.3)
        print('Lizard eats paper')
        time.sleep(.3)
        print('Paper disproves Spock')
        time.sleep(.3)
        print('Spock vaporizes Rock')
        time.sleep(.3)



    def choose_player(self):
        print('')
        user_choice = input('Press 1 for single player, 2 for muli-player, or 3 for a show! ')
        if user_choice == "1":
            p_one_name = input("What is player ones name? ")
            self.player_one = Human(p_one_name)
            self.player_two = AI("E.D.I.T.H")
        if user_choice == "2":
            p_one_name = input("What is player ones name? ")
            self.player_one = Human(p_one_name)
            print('')
            p_two_name = input("What is player twos name? ")
            print('')
            self.player_two = Human(p_two_name)
        if user_choice == "3":
            print("Sit back and watch the show!")
            self.player_one = AI("F.R.I.D.A.Y")
            self.player_two = AI("J.A.R.V.I.S")
    def play_rounds(self):
      
        while self.player_one.score <2 and self.player_two.score <2:
        
        
            self.player_one.choose_gesture()
            self.player_two.choose_gesture()
            if self.player_one.selection == self.player_two.selection:
                time.sleep(.3)
                print("Its a tie, keep playing")
                print('')
            elif self.player_one.selection == "Rock" and self.player_two.selection == "Scissors":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 
            elif self.player_one.selection == "Scissors" and self.player_two.selection == "Paper":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 

            elif self.player_one.selection == "Paper" and self.player_two.selection == "Rock":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                

            elif self.player_one.selection == "Rock" and self.player_two.selection == "Lizard":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 

            elif self.player_one.selection == "Lizard" and self.player_two.selection == "Spock":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            elif self.player_one.selection == "Spock" and self.player_two.selection == "Scissors":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            elif self.player_one.selection == "Scissors" and self.player_two.selection == "Lizard":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 
    
            elif self.player_one.selection == "Lizard" and self.player_two.selection == "Paper":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1 
            
            elif self.player_one.selection == "Paper" and self.player_two.selection == "Spock":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

            elif self.player_one.selection == "Spock" and self.player_two.selection == "Rock":
                time.sleep(.3)
                print(f'{self.player_one.name} won this hand with {self.player_one.selection} vs {self.player_two.selection}')
                print('')
                self.player_one.score += 1

                

            elif self.player_two.selection == "Rock" and self.player_one.selection == "Scissors":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1 
            elif self.player_two.selection == "Scissors" and self.player_one.selection == "Paper":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1 

            elif self.player_two.selection == "Paper" and self.player_one.selection == "Rock":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                self.player_two.score += 1
                

            elif self.player_two.selection == "Rock" and self.player_one.selection == "Lizard":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1 

            elif self.player_two.selection == "Lizard" and self.player_one.selection == "Spock":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1

            elif self.player_two.selection == "Spock" and self.player_one.selection == "Scissors":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1

            elif self.player_two.selection == "Scissors" and self.player_one.selection == "Lizard":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1 
    
            elif self.player_two.selection == "Lizard" and self.player_one.selection == "Paper":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1 
            
            elif self.player_two.selection == "Paper" and self.player_one.selection == "Spock":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1

            elif self.player_two.selection == "Spock" and self.player_one.selection == "Rock":
                time.sleep(.3)
                print(f'{self.player_two.name} won this hand with {self.player_two.selection} vs {self.player_one.selection}')
                print('')
                self.player_two.score += 1

            
                
    
    def run_game(self):
            self.welcome()
            self.rules()
            self.choose_player()
            self.play_rounds()

