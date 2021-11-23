from states.poker import Poker

class River(Poker):
    def __init__(self, game):
        Poker.__init__(self, game)

    def update(self, delta_time, actions):
        pass

    def render(self, display):
        display.fill((255,255,255))
        self.game.draw_text(display, "Now at the river", (0,0,0), self.game.GAME_W/2, self.game.GAME_H/2)