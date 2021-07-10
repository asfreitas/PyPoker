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
        self.resize_image(4, 4)
        self.x = 0
        self.y = 0

    def resize_image(self, width_scale, height_scale):
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.smoothscale(self.image, (int(width/width_scale), int(height/height_scale)))

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def get_height(self):
        return self.image.get_height()

    def get_width(self):
        return self.image.get_width()

    def set_y(self, y):
        self.y = y

    def set_x(self, x):
        self.x = x


class Deck:
    def __init__(self):
        deck = []
        for rank in ranks:
            for suit in suits:
                deck.append(Card(suit, rank))
        self.deck = deck
        self.shuffle()

    # shuffle the deck 
    def shuffle(self):
        random.shuffle(self.deck)

    # pop a card off the deck and return it
    def get_card(self):
        card = self.deck.pop()
        return card
        

