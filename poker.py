import deck
import player

import constants

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT

class Poker:
    def __init__(self):
        self.player_one = player.Player()
        self.current_deck = deck.Deck()
        self.community_cards = []
        self.cards_are_dealt = False

    def deal_cards(self):
        if self.cards_are_dealt:
            return
        card1 = self.current_deck.get_card()
        card2 = self.current_deck.get_card()
        self.player_one.hand.append(card1)
        self.player_one.hand.append(card2)

        new_position = int(SCREEN_WIDTH / 2 - int(card1.get_width() / 2))

        card1.set_new_y(SCREEN_HEIGHT - card1.get_height())
        card1.set_new_x(new_position)

        card2.card_waiting_for = card1 # let this card know it needs to wait for card 1
        card2.set_new_y(SCREEN_HEIGHT - card1.get_height())
        card2.set_new_x(new_position - card2.get_width() / 2)
        print(self.player_one.hand)

        self.cards_are_dealt = True
    
    def burn_card(self):
        self.current_deck.get_card()
    
    def deal_flop(self):
        self.burn_card()

        card1 = self.current_deck.get_card()
        card2 = self.current_deck.get_card()
        card3 = self.current_deck.get_card()

        #self.move_flop(card1, card2, card3)

        self.community_cards.append(card1)
        self.community_cards.append(card2)
        self.community_cards.append(card3)
    
    def move_flop(card1, card2, card3):
        pass
    def deal_turn(self):
        self.burn_card()
        self.community_cards.append(self.current_deck.get_card())
    
    def deal_river(self):
        self.burn_card()
        self.community_cards.append(self.current_deck.get_card())


    