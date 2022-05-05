from director import Director
from director import Deck

director = Director()
deck = Deck()
keep_playing = 'y'

while keep_playing == 'y':
    card_deck = director.cards() #brings card_deck list using cards function

    #print(card_deck) left this here for debbugging purposes
    
    guess = input('Higher or lower? [h/l] ').lower()

    #compares the 2 card values in the card deck list
    # first card will be position [0] and second card will be position [1]

    if guess == 'h' and (card_deck[1] > card_deck[0]):
        deck.award_points()
    elif guess == 'h' and (card_deck[1] < card_deck[0]):
        deck.deduct_points()
    elif guess == 'l' and (card_deck[1] < card_deck[0]):
        deck.award_points()
    elif guess == 'l' and (card_deck[1] > card_deck[0]):
        deck.deduct_points()
    elif guess == 'h' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()
    elif guess == 'l' and (card_deck[1] == card_deck[0]):
        deck.deduct_points()

    print(f'Next card was: {card_deck[1]}')
    
    card_deck.clear()
    #clears deck for new loop

    deck.keep_score()
        #award or deduct points based on guess

        #finds score so that it can be compared
    score = deck.game_over_score()
        
        #if player reaches score of 0 or less then the game is over
    if score <= 0:
        keep_playing = 'n'
        #if score is greater than 0 they can continue to play
    else:
        keep_playing = input('Play again? [y/n]: ').lower()
    
    print()
