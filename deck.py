import pygame
import os
import random
suits = ['hearts', 
         'clubs', 
         'spades', 
         'diamonds']


ranks = ['2',
         '3',
         '4',
         '5',
         '6',
         '7',
         '8',
         '9',
         '10',
         'jack',
         'queen',
         'king',
         'ace']
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.image = pygame.image.load(os.path.join('images/cards', rank + '_' + suit + '.png'))
class Deck:
    def __init__(self):
        deck = []
        for rank in ranks:
            for suit in suits:
                deck.append(Card(suit, rank))
        self.deck = deck
    def shuffle(self):
        random.shuffle(self.deck)
    def getCard(self):
        card = self.deck.pop()
        return card
        

