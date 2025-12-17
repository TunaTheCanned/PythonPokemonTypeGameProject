import pygame

class Button:
    def __init__(self, text, font, text_color, button_color, x_pos, y_pos, width,
                 height, rounded_border_radius, border_color, border_color_thickness, screen, enabled):

        self.text = text
        self.font = font
        self.text_color = text_color
        self.button_color = button_color
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.rounded_border_radius = rounded_border_radius
        self.border_color = border_color
        self.border_color_thickness = border_color_thickness
        self.screen = screen
        self.enabled = enabled
        self.draw()


    def draw(self):
        button_text = self.font.render(self.text, True, self.text_color)
        button_rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)
        pygame.draw.rect(self.screen, self.button_color, button_rect, 0, self.rounded_border_radius)
        pygame.draw.rect(self.screen, self.border_color, button_rect, self.border_color_thickness, self.rounded_border_radius)
        #self.screen.blit(button_text, button_rect)
        self.screen.blit(button_text, (self.x_pos + 10, self.y_pos + 10))

