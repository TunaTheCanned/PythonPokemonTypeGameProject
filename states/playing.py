import pygame

from source.game_state import GameState
from states.state import State

class PlayingState(State):
    def __init__(self, game):
        super().__init__(game)
        self.pos = pygame.Vector2(640, 360)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.change_state(GameState.START_MENU)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        speed = 300

        if keys[pygame.K_w]:
            self.pos.y -= speed * dt
        if keys[pygame.K_s]:
            self.pos.y += speed * dt
        if keys[pygame.K_a]:
            self.pos.x -= speed * dt
        if keys[pygame.K_d]:
            self.pos.x += speed * dt

    def draw(self):
        self.game.renderer.clear((0, 0, 0))
        pygame.draw.circle(self.game.screen, "yellow", self.pos, 40)