import pygame


class State:
    def __init__(self, game):
        self.game = game
        # self.font = pygame.font.SysFont("arial", 40)
        self.font = pygame.font.Font("resources/Minecraft.ttf", 40)

    def handle_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self):
        pass

    def on_resize(self):
        pass