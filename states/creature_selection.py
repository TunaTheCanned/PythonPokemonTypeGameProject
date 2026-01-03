import math

import pygame

import source.button
from source.game_state import GameState
from states.state import State

class CreatureSelectionState(State):
    def __init__(self, game, creatures):
        super().__init__(game)

        self.creatures = creatures
        self.index = 0
        try:
            self.bg_original = pygame.image.load("resources/background_creatures.png").convert()
        except FileNotFoundError:
            print("Error: File not found")
            self.bg_original = None
        self.sprite_pos = None
        self.title_pos = None
        self.name_pos = None
        self.stats_x = None
        self.stats_y = None
        self.stats_spacing = None

        self.moves_section_title = None
        self.moves_start_y = None
        self.sprite_size = None

        # self.font = pygame.font.SysFont("arial", 40)

        self.left_button = source.button.Button("<<", "black", self.font,"white",
                                          100, 100, 5,
                                          "black", 5, game.screen, True)
        # self.left_button.set_position(20, (game.get_height()-self.left_button.height)-20)

        self.right_button = source.button.Button(">>", "black", self.font, "white",
                                                 100, 100, 5,
                                                 "black", 5, game.screen, True)
        # self.right_button.set_position(game.get_width() - self.right_button.width - 20, (game.get_height() - self.right_button.height) - 20)

        self.select_button = source.button.Button("Choose", "black", self.font, "white",
                                                  300, 100, 5,
                                                  "black", 5, game.screen, True)
        # self.select_button.set_position((game.get_width()-self.select_button.width) / 2, (game.get_height()-self.select_button.height) - 20)

        self.update_layout()


    def update_layout(self):
        width = self.game.screen.get_width()
        height = self.game.screen.get_height()

        if self.bg_original:
            self.bg_scaled = pygame.transform.scale(self.bg_original, (width, height))

        self.title_pos = int((width * 0.5 - 150)), int((height * 0.05))
        self.name_pos = int((width * 0.05)), int((height * 0.05))
        self.stats_x = int((width * 0.55))
        self.stats_y = int((height * 0.1))
        self.stats_spacing = int((height * 0.08))
        self.sprite_pos = int((width * 0.05)), int((height * 0.1) + self.stats_spacing)

        self.moves_section_title = (self.stats_x, self.stats_y + self.stats_spacing * 5)
        self.moves_start_y = self.moves_section_title[1] + self.stats_spacing

        self.left_button.set_position(int(width * 0.02), int(height -self.left_button.height - height * 0.03))
        self.right_button.set_position(int(width - self.right_button.width - width * 0.02), int(height - self.right_button.height - height * 0.03))

        self.select_button.set_position(int(width * 0.5 - self.select_button.width / 2), int(height - self.select_button.height - height * 0.03))

        self.sprite_size = (int(width * 0.25), int(height * 0.35))


    def handle_event(self, event):
        self.left_button.handle_events(event)
        self.right_button.handle_events(event)
        self.select_button.handle_events(event)

        if self.left_button.consume_click():
            self.index -= 1
            if self.index < 0:
                self.index = len(self.creatures) - 1

        if self.right_button.consume_click():
            self.index += 1
            if self.index >= len(self.creatures):
                self.index = 0

        if self.select_button.consume_click():
            self.game.players[self.game.current_player_index].creature = self.creatures[self.index].copy()
            self.game.current_player_index += 1
            if self.game.current_player_index == 2:
                self.game.message_text = "Fight!"
                self.game.message_duration = 1.0
                self.game.message_next_state = GameState.FIGHTING
                self.game.change_state(GameState.MESSAGE)
            else:
                self.index = 0
                self.game.message_text = f"Player {self.game.current_player_index + 1} Choosing"
                self.game.message_duration = 1.0
                self.game.message_next_state = GameState.CREATURE_SELECTION
                self.game.change_state(GameState.MESSAGE)


    def draw(self):
        if self.bg_scaled:
            self.game.screen.blit(self.bg_scaled, (0, 0))
        else:
            self.game.renderer.clear((30, 30, 30))
        #self.game.renderer.clear((30, 30, 30))
        creature = self.creatures[self.index]

        self.game.renderer.draw_image(creature.sprite, self.sprite_pos, self.sprite_size)

        self.game.renderer.draw_text(f"Player {self.game.current_player_index + 1} choosing", (255, 255, 255), self.title_pos)

        self.game.renderer.draw_text(creature.name, (255, 255, 255), self.name_pos)

        # self.game.renderer.draw_centered_text(f"Current index: {self.index + 1}")

        self.game.renderer.draw_text("Moves:", (255, 255, 255), self.moves_section_title)
        self.game.renderer.draw_text("Attack: " + str(creature.attack), (255, 255, 255), (self.stats_x, self.stats_y + 1 * self.stats_spacing))
        self.game.renderer.draw_text("Defense: "+str(creature.defense), (255, 255, 255), (self.stats_x, self.stats_y + 2 * self.stats_spacing))
        self.game.renderer.draw_text("Health: "+str(creature.hp), (255, 255, 255), (self.stats_x, self.stats_y + 3 * self.stats_spacing))
        self.game.renderer.draw_text("Evasion: " + str(creature.evasion), (255, 255, 255), (self.stats_x, self.stats_y + 4 * self.stats_spacing))

        for i, move in enumerate(creature.moves):
            move_name = str(move)
            col = i % 2
            row = i // 2
            x = self.stats_x + col * int(self.game.screen.get_width() * 0.2)
            y = self.moves_start_y + row * int(self.game.screen.get_height() * 0.1)

            self.game.renderer.draw_text(move_name, (255, 255, 255), (x, y))

        self.left_button.draw()
        self.right_button.draw()
        self.select_button.draw()



    def on_resize(self):
        self.update_layout()

        # font_size = max(40, int(self.game.get_height() * 0.05))
        # font = pygame.font.SysFont("comicsans", font_size)
        # self.left_button.set_font(font)
        # self.right_button.set_font(font)
        # self.select_button.set_font(font)

        # self.left_button.set_position(20, (self.game.get_height() - self.left_button.height) - 20)
        # self.right_button.set_position(self.game.get_width() - self.right_button.width - 20, (self.game.get_height() - self.right_button.height) - 20)
        # self.select_button.set_position((self.game.get_width()-self.select_button.width) / 2, (self.game.get_height()-self.select_button.height) - 20)

