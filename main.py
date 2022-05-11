from Director import Director
from Director import Deck

director = Director()
deck = Deck()
keep_playing = 'y'

while keep_playing == 'y':
    card_deck = director.cards() #brings card_deck list using cards function

    #print(card_deck) left this here for debbugging purposes

    guess = input('Higher or lower? [h/l] ').lower()

    print("\t\t\t     ____________________")
    print("\t\t\t                         ")  
    print("\t\t\t     The Next Card was {}".format(card_deck[1]))   
    print("\t\t\t     ____________________")
    print("\t\t\t                         ") 

    #compares the 2 card values in the card deck list
    # first card will be position [0] and second card will be position [1]

    if guess == 'h' and (card_deck[1] > card_deck[0]):
        deck.award_points()
        print("\t\t\t    Your score is plus 100 now!")
    elif guess == 'h' and (card_deck[1] < card_deck[0]):
        deck.deduct_points()
        print("\t\t\t    Your score is minus 75 now!")
    elif guess == 'l' and (card_deck[1] < card_deck[0]):
        deck.award_points()
        print("\t\t\t    Your score is plus 100 now!")
    elif guess == 'l' and (card_deck[1] > card_deck[0]):
        deck.deduct_points()
        print("\t\t\t    Your score is minus 75 now!")
    elif guess == 'h' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
        print("\t\t\t    Your score is minus 75 now!")
    elif guess == 'l' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
        print("\t\t\t    Your score is minus 75 now!")


    card_deck.clear()
    #clears deck for new loop

    # print the scoreboad for the user
    deck.print_scoreboard()

        #finds score so that it can be compared
    score = deck.game_over_score()

        #if player reaches score of 0 or less then the game is over
    if score <= 0:
        keep_playing = 'n'
        #if score is greater than 0 they can continue to play
    else:
        keep_playing = input('Play again? [y/n]: ').lower()

    print()