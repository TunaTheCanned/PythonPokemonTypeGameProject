import pygame

#dictionary mapping color names to rgb values. we using a dict here !! :DDD !!!!
#TODO add more colors
COLOR_MAP = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "purple": (128, 0, 128),
    "gray": (128, 128, 128),
    "yellow": (255, 255, 0),
}

#function to darken the color, we subtract the amount from the rgb values of the color
def darken_color(color, amount):
    if amount < 0:
        return (
            min(255, color[0] - amount),
            min(255, color[1] - amount),
            min(255, color[2] - amount),
        )
    else:
        return (
            max(0, color[0] - amount),
            max(0, color[1] - amount),
            max(0, color[2] - amount),
        )



class Button:
    def __init__(self, text, text_color, font, button_color, width,
                 height, rounded_border_radius, border_color, border_color_thickness, screen, enabled):
        #in order
        #text = text we want to display on the button
        #font = font of the text
        #text_color = guess
        #button_color = background color of the button
        #width = width of the button
        #height = guess
        #rounded_border_radius = how rounded are the corners supposed to be, 0 = not rounded
        #border_color = color of the border of the button
        #border_color_thickness = how thick is supposed to be the 'other color' border of the button
        #screen = where the button is supposed to be drawn, just use "screen", it is our display
        #enabled = if the button is supposed to be enabled or not, it will still show, but enabled = False button will not be able to be clicked



        self.text = text
        self.font = font
        self.text_color = COLOR_MAP[text_color]
        self.button_color = COLOR_MAP[button_color]
        self.width = width
        self.height = height
        self.rounded_border_radius = rounded_border_radius
        self.border_color = COLOR_MAP[border_color]
        self.border_color_thickness = border_color_thickness
        self.screen = screen
        self.enabled = enabled

        self.rect = pygame.Rect(0, 0, width, height)
        self.hovered = False
        self.clicked = False
        self.pressed = False
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def set_position(self, x, y):
        self.rect.topleft = (x, y)


    def handle_events(self, event):
        if not self.enabled:
            return

        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.pressed = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed and self.rect.collidepoint(event.pos):
                self.clicked = True
            self.pressed = False

    def draw(self):
        base_color = self.button_color

        if self.pressed:
            color = darken_color(base_color, 100)
        elif self.hovered:
            color = darken_color(base_color, 40)
        else:
            color = base_color

        pygame.draw.rect(self.screen, color, self.rect, border_radius=self.rounded_border_radius)
        pygame.draw.rect(self.screen, self.border_color, self.rect, self.border_color_thickness, border_radius=self.rounded_border_radius)

        text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.screen.blit(self.text_surface, text_rect)

    def consume_click(self):
        if self.clicked:
            self.clicked = False
            return True
        return False

    def set_font(self, font):
        self.font = font
        self.text_surface = font.render(self.text, True, self.text_color)