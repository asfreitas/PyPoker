import pygame
import time
import sys

import constants
import poker

SCREEN_WIDTH = constants.SCREEN_WIDTH
SCREEN_HEIGHT = constants.SCREEN_HEIGHT
WHITE = constants.WHITE
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def redraw_window(cards):
    card1, card2 = cards
    card1.draw(game_display)
    card2.draw(game_display)

def add_card(card, pos):
    if card.x > pos:
        card.move_left()

def draw_cards(cards):
    card1, card2 = cards
    new_position = int(SCREEN_WIDTH / 2 - int(card1.get_width() / 2))
    add_card(card1, new_position)
    if card1.x == new_position:
        add_card(card2, new_position - card2.get_width() / 2)


### 1. Give Players Cards
### 2. Check for bets/checks
### 3. Deal flop
###
def game_loop(game):
    game.deal_cards()
    game.deal_flop()


def main():
    game = poker.Poker()
    d1 = game.current_deck
    game.deal_cards()

    player1 = game.player_one

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
        game_loop(game)
        game_display.fill(WHITE)
        redraw_window(player1.hand)

        # in doing some reading, this is a super slow way to update
        # apparently we can choose to update only the part of the screen
        # where objects would be redrawn
        pygame.display.update()

if __name__=="__main__":
    main()
