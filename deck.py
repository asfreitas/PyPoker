import pygame
import os
import random

import constants
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
        self.x = constants.SCREEN_WIDTH
        self.y = constants.SCREEN_HEIGHT
        self.new_y = 0
        self.new_x = 0
        self.card_waiting_for = None

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

    def set_new_y(self, y):
        self.new_y = y

    def set_new_x(self, x):
        self.new_x = x

    def set_y(self, y):
        self.y = y

    def set_x(self, x):
        self.x = x

    def draw(self, game_display):
        if self.card_waiting_for == None or self.card_waiting_for.x == self.card_waiting_for.new_x:
            if self.x > self.new_x:
                self.move_left()
            if self.y > self.new_y:
                self.move_down()
            game_display.blit(self.image, (self.x,self.y))


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
        

