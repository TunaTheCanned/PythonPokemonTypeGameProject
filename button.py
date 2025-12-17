import pygame

#dictionary mapping color names to rgb values. we using a dict here !! :DDD !!!!
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
    return (
        max(0, color[0] - amount),
        max(0, color[1] - amount),
        max(0, color[2] - amount),
    )


class Button:
    def __init__(self, text, font, text_color, button_color, x_pos, y_pos, width,
                 height, rounded_border_radius, border_color, border_color_thickness, screen, enabled):
        #in order
        #text = text we want to display on the button
        #font = font of the text
        #text_color = guess
        #button_color = background color of the button
        #x_pos = x coordinate. WE START FROM THE TOP LEFT> TOP LEFT IS 0,0
        #y_pos = guess
        #width = width of the button
        #height = guess
        #rounded_border_radius = how rounded are the corners supposed to be, 0 = not rounded
        #border_color = color of the border of the button
        #border_color_thickness = how thick is supposed to be the 'other color' border of the button
        #screen = where the button is supposed to be drawn, just use "screen", it is our display
        #enabled = if the button is supposed to be enabled or not, it will still show, but enabled = False button will not be able to be clicked
        #draw = a function to draw the button

        self.text = text
        self.font = font
        self.text_color = COLOR_MAP[text_color]
        self.button_color = COLOR_MAP[button_color]
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.rounded_border_radius = rounded_border_radius
        self.border_color = COLOR_MAP[border_color]
        self.border_color_thickness = border_color_thickness
        self.screen = screen
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = self.font.render(self.text, True, self.text_color)
        button_rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)

        #dim the button when pressed
        if self.check_click():
            pygame.draw.rect(self.screen, darken_color(self.button_color, 50), button_rect, 0, self.rounded_border_radius)
        else:
            #else its just normal
            pygame.draw.rect(self.screen, self.button_color, button_rect, 0, self.rounded_border_radius)

        pygame.draw.rect(self.screen, self.border_color, button_rect, self.border_color_thickness, self.rounded_border_radius)

        #this positions the text at the top left corner
        #self.screen.blit(button_text, button_rect)

        #this moves the button 10 units to the right and down from the top left corner
        self.screen.blit(button_text, (self.x_pos + 10, self.y_pos + 10))

    #function to check if the button has been clicked
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)

        #the button must be enabled to be clicked
        if (left_click and button_rect.collidepoint(mouse_pos) and self.enabled):
            return True
        else:
            return False