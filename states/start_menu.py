import pygame

from states.state import State
from source.game_state import GameState
from source import button



class StartMenuState(State):
    def __init__(self, game):
        super().__init__(game)

        try:
            self.bg_image = pygame.image.load("resources/background_menu.png").convert()
        except FileNotFoundError:
            print("Error: File not found")
            self.bg_image = None

        self.start_button = button.Button("Start Game", "white", self.font, "purple",
                                          300, 100, 5,
                                          "black", 5, game.screen, True)

        self.leave_game_button = button.Button("Leave Game", "purple", self.font, "gray",
                                               300, 100, 5,
                                               "black", 5, game.screen, True)
        self.on_resize()

    def handle_event(self, event):
        self.start_button.handle_events(event)
        self.leave_game_button.handle_events(event)



    def update(self, dt):
        if self.start_button.consume_click():
            self.game.message_text = "Player 1 Choosing"
            self.game.message_duration = 1.0
            self.game.message_next_state = GameState.CREATURE_SELECTION
            self.game.current_player_index = 0
            self.game.change_state(GameState.MESSAGE)
        elif self.leave_game_button.consume_click():
            self.game.running = False



    def draw(self):
        if self.bg_image:
            self.game.renderer.draw_image(self.bg_image, (0, 0),
                                          (self.game.get_width(), self.game.get_height()))
        else:
            self.game.renderer.clear((100, 0, 0))

        self.start_button.draw()
        self.leave_game_button.draw()

    def on_resize(self):
        self.start_button.set_font(self.font)
        self.leave_game_button.set_font(self.font)
        self.start_button.set_position((self.game.get_width() - self.start_button.width) // 2, self.game.get_height() * 0.3)
        self.leave_game_button.set_position((self.game.get_width() - self.leave_game_button.width) // 2, self.game.get_height() * 0.45)

