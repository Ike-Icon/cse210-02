from hilo_game import Deck
deck = Deck()

class Director:

    # import hilo_game.py info
    # start hilo game by calling deck class
    

    def __init__(self):
        #creates list where card values can be stored
        self.card_deck = []

    def cards(self):
    # draw 2 cards using class Deck that will be added to self.card_deck list
        
        first_card = deck.draw_card()
        print(f'The card is: {first_card}')

        second_card = deck.draw_card()

        self.card_deck.append(first_card)
        self.card_deck.append(second_card)

        return self.card_deck #returns the card_deck list
    

