import pygame


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        # self.font = pygame.font.SysFont("arial", 40)
        self.font = pygame.font.Font("resources/Minecraft.ttf", 40)

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_text(self, text, color, pos):
        img = self.font.render(text, True, color)
        self.screen.blit(img, pos)

    def draw_centered_text(self, text):
        img = self.font.render(text, True, (255, 255, 255))
        pos = img.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(img, pos)

    def draw_image(self, img, pos, size=None):
        if size:
            img = pygame.transform.smoothscale(img, size)
        self.screen.blit(img, pos)

