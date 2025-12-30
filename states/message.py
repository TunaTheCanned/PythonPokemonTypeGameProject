import pygame

import source.button
from source.game_state import GameState
from states.state import State

class MessageState(State):
    def __init__(self, game):
        super().__init__(game)
        self.timer = 0.0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.game.message_duration:
            self.game.change_state(self.game.message_next_state)


    def draw(self):
        self.game.renderer.clear((0,0,0))
        self.game.renderer.draw_centered_text(self.game.message_text)
