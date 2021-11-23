from states.poker import Poker
from states.river import River
class Turn(Poker):
    def __init__(self, game):
        Poker.__init__(self, game)

    def update(self, delta_time, actions):
        if actions['start']:
            new_state = River(self.game)
            new_state.enter_state()
        self.game.reset_keys()

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display, "Now at the turn", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)

