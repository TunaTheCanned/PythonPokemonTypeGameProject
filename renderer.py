
class Renderer:
    def __init__(self, screen):
        self.screen = screen

    def clear(self, color=(0, 0, 0)):
        self.screen.fill(color)

    def draw_text(self, text, font, color, pos):
        img = font.render(text, True, color)
        self.screen.blit(img, pos)