import deck
import player

class Poker:
    def __init__(self):
        self.player_one = player.Player()
        self.current_deck = deck.Deck()
        self.community_cards = []

    def deal_cards(self, SCREEN_HEIGHT, SCREEN_WIDTH):
        card1 = self.current_deck.get_card()
        card2 = self.current_deck.get_card()
        self.player_one.hand.append(card1)
        self.player_one.hand.append(card2)

        card1.set_y(SCREEN_HEIGHT - card1.get_height())
        card1.set_x(SCREEN_WIDTH)

        card2.set_y(SCREEN_HEIGHT - card1.get_height())
        card2.set_x(SCREEN_WIDTH)
        print(self.player_one.hand)
    
    def burn_card(self):
        self.current_deck.get_card()
    
    def deal_flop(self):
        burn_card()
        self.community_cards.append(self.current_deck.get_card())
        self.community_cards.append(self.current_deck.get_card())
        self.community_cards.append(self.current_deck.get_card())
    
    def deal_turn(self):
        burn_card()
        self.community_cards.append(self.current_deck.get_card())
    
    def deal_river(self):
        burn_card()
        self.community_cards.append(self.current_deck.get_card())


    