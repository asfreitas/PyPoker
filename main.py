import pygame
import time
import sys

import poker

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 600
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
white = (255,255,255)

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

def main():
    game = poker.Poker()
    d1 = game.current_deck
    game.deal_cards(SCREEN_HEIGHT, SCREEN_WIDTH)

    player1 = game.player_one

    while 1:
        draw_cards(player1.hand)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)

        game_display.fill(white)
        redraw_window(player1.hand)

        # in doing some reading, this is a super slow way to update
        # apparently we can choose to update only the part of the screen
        # where objects would be redrawn
        pygame.display.update()

if __name__=="__main__":
    main()
