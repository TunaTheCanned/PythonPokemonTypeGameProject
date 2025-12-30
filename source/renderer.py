import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("comicsans", 40)

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_text(self, text, color, pos):
        img = self.font.render(text, True, color)
        self.screen.blit(img, pos)

    def draw_centered_text(self, text):
        img = self.font.render(text, True, (255, 255, 255))
        pos = img.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(img, pos)

    def draw_image(self, img, pos):
        # TODO fix later so the aspect ratio is zachowane idk nie wiem w sumie czy wypada czy nie bo tak tez jest okej ale sie streczuje strasznie
        scaled = pygame.transform.smoothscale(img, (int(self.screen.get_width()*0.3), int(self.screen.get_height())*0.3))
        self.screen.blit(scaled, pos)

