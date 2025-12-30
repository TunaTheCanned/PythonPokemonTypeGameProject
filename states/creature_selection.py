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
        self.font = pygame.font.SysFont("comicsans", 40)

        self.left_button = source.button.Button("<<", "black", self.font,"white",
                                          100, 100, 5,
                                          "black", 5, game.screen, True)
        self.left_button.set_position(20, (game.get_height()-self.left_button.height)-20)

        self.right_button = source.button.Button(">>", "black", self.font, "white",
                                                 100, 100, 5,
                                                 "black", 5, game.screen, True)
        self.right_button.set_position(game.get_width() - self.right_button.width - 20, (game.get_height() - self.right_button.height) - 20)

        self.select_button = source.button.Button("Choose", "black", self.font, "white",
                                                  300, 100, 5,
                                                  "black", 5, game.screen, True)
        self.select_button.set_position((game.get_width()-self.select_button.width) / 2, (game.get_height()-self.select_button.height) - 20)


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
            self.game.players[self.game.current_player_index].creature = self.creatures[self.index]
            self.game.current_player_index += 1
            if self.game.current_player_index == 2:
                self.game.message_text = "Fight!"
                self.game.message_duration = 2.0
                self.game.message_next_state = GameState.FIGHTING
                self.game.change_state(GameState.MESSAGE)
            else:
                self.index = 0
                self.game.message_text = f"Player {self.game.current_player_index + 1} Choosing"
                self.game.message_duration = 2.0
                self.game.message_next_state = GameState.CREATURE_SELECTION
                self.game.change_state(GameState.MESSAGE)


    def draw(self):
        self.game.renderer.clear((30, 30, 30))
        creature = self.creatures[self.index]
        self.game.renderer.draw_image(creature.sprite, (60, 120))

        self.game.renderer.draw_text(f"Player {self.game.current_player_index + 1} choosing", (255, 255, 255), (self.game.get_width()/2 - 100, 10))
        self.game.renderer.draw_text(creature.name, (255, 255, 255), (40, 60))
        self.game.renderer.draw_centered_text(f"Current index: {self.index + 1}")
        self.game.renderer.draw_text("Attack: " + str(creature.attack), (255, 255, 255), (self.game.get_width()/2 + 100, 140))
        self.game.renderer.draw_text("Defense: "+str(creature.defense), (255, 255, 255), (self.game.get_width()/2 + 100, 240))
        self.game.renderer.draw_text("Health: "+str(creature.hp), (255, 255, 255), (self.game.get_width()/2 + 100, 340))
        # self.game.renderer.draw_text(creature.moves, (255, 255, 255), (self.game.get_width() - 100, self.game.get_height() - 400))

        self.left_button.draw()
        self.right_button.draw()
        self.select_button.draw()

    def on_resize(self):
        font_size = max(10, int(self.game.get_height() * 0.05))
        font = pygame.font.SysFont("comicsans", font_size)
        self.left_button.set_font(font)
        self.right_button.set_font(font)
        self.select_button.set_font(font)

        self.left_button.set_position(20, (self.game.get_height() - self.left_button.height) - 20)
        self.right_button.set_position(self.game.get_width() - self.right_button.width - 20, (self.game.get_height() - self.right_button.height) - 20)
        self.select_button.set_position((self.game.get_width()-self.select_button.width) / 2, (self.game.get_height()-self.select_button.height) - 20)

