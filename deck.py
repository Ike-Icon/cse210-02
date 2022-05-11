import random
import random

class Deck:
    def __init__(self):
        self.card = 0 #card number
        self.score = 300 #total player score
    
    def draw_card(self):
        self.card = random.randint(1,13) #create a card with a random number between 1-13
        return int(self.card)
      

    def award_points(self):
        self.score += 100 #points awarded if guess is correct
    
    def deduct_points(self):
        self.score = self.score - 75 #points deducted if guess is incorrect
        
    
    #return integer of score so that it can be compare in start_game.py
    def game_over_score(self):
        game_over = self.score
        return int(game_over)

    
    # Function to print the scorebaord  
    def print_scoreboard(self):
   
        print("\t\t\t     ____________________")
        print("\t\t\t    |                    |")
        if self.score <= 0:
            print("\t\t\t    |  Your Score = {}  |".format(self.score))
        else:   
            print("\t\t\t    |  Your Score = {}  |".format(self.score))
          
        print("\t\t\t    |____________________|")

