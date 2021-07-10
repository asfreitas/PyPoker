	
import pygame
import time

import deck
import player
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 600
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
white = (255,255,255)

def redraw_window(cards):
    card1, card2 = cards
    card1.draw(game_display)
    card2.draw(game_display)

def main():
    d1 = deck.Deck()

    card1 = d1.get_card()
    card1.set_y(SCREEN_HEIGHT - card1.get_height())
    card1.set_x(SCREEN_WIDTH)

    card2 = d1.get_card()
    card2.set_y(SCREEN_HEIGHT - card1.get_height())
    card2.set_x(SCREEN_WIDTH)

    player1 = player.Player(card1, card2)

    while 1:
        give_cards((card1, card2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game_display.fill(white)
        redraw_window((card1, card2))


        pygame.display.update()


def add_card(card, pos):
    if card.x > pos:
        card.move_left()

def give_cards(cards):
    card1, card2 = cards
    new_position = int(SCREEN_WIDTH / 2 - int(card1.get_width() / 2))
    add_card(card1, new_position)
    if card1.x == new_position:
        add_card(card2, new_position - card2.get_width() / 2)

if __name__=="__main__":
    main()
