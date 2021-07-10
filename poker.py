import deck
import player

class Poker:
    def __init__(self):
        self.player_one = player.Player()
        self.current_deck = deck.Deck()
        self.flop = []
        self.turn = []
        self.river = []

    def deal_cards(self):
        self.player_one.hand.append(self.current_deck.get_card())
        self.player_one.hand.append(self.current_deck.get_card())
        print(self.player_one.hand)
    
    def burn_card(self):
        self.current_deck.get_card()
    
    def deal_flop(self):
        burn_card()
        self.flop.append(self.current_deck.get_card())
        self.flop.append(self.current_deck.get_card())
        self.flop.append(self.current_deck.get_card())
    
    def deal_turn(self):
        burn_card()
        self.turn.append(self.current_deck.get_card())
    
    def deal_river(self):
        burn_card()
        self.river.append(self.current_deck.get_card())


    