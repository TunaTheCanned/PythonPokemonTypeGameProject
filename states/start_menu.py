import math


import pygame

from states.state import State
from source.game_state import GameState
from source import button
import tkinter
from tkinter import filedialog
from source.creature_loader import load_creature
from states.message import MessageState


class StartMenuState(State):
    def __init__(self, game):
        super().__init__(game)



        self.start_button = button.Button("Start Game", "white", self.font, "purple",
                                          300, 100, 5,
                                          "black", 5, game.screen, True)

        # self.load_game_button = button.Button("Load Game", "purple", self.font, "yellow",
        #                                       300, 100, 5,
        #                                       "black", 5, game.screen, True)

        self.leave_game_button = button.Button("Leave Game", "purple", self.font, "gray",
                                               300, 100, 5,
                                               "black", 5, game.screen, True)
        self.on_resize()

    def handle_event(self, event):
        self.start_button.handle_events(event)
        # self.load_game_button.handle_events(event)
        self.leave_game_button.handle_events(event)



    def update(self, dt):
        if self.start_button.consume_click():
            self.game.message_text = "Player 1 Choosing"
            self.game.message_duration = 1.0
            self.game.message_next_state = GameState.CREATURE_SELECTION
            self.game.current_player_index = 0
            self.game.change_state(GameState.MESSAGE)

        # elif self.load_game_button.consume_click():
        #     # self.game.change_state(GameState.GAME_IS_ACTIVE)
        #     try:
        #         tkinter.Tk().withdraw()
        #         filepath = filedialog.askopenfilename()
        #         load_creature(filepath)
        #     except:
        #         #TODO make it catch the exception when user tries to open a wrong file
        #         print("wrong file extension")


        elif self.leave_game_button.consume_click():
            self.game.running = False



    def draw(self):
        self.game.renderer.clear((100, 0, 0))

        self.start_button.draw()
        # self.load_game_button.draw()
        self.leave_game_button.draw()

    def on_resize(self):
        font_size = max(40, int(self.game.get_height() * 0.05))
        # font = pygame.font.SysFont("comicsans", font_size)
        self.font = pygame.font.Font("resources/Minecraft.ttf", 40)
        self.start_button.set_font(self.font)
        # self.load_game_button.set_font(self.font)
        self.leave_game_button.set_font(self.font)

        self.start_button.set_position((self.game.get_width() - self.start_button.width) // 2, self.game.get_height() * 0.3)
        # self.load_game_button.set_position((self.game.get_width() - self.load_game_button.width) // 2, self.game.get_height() * 0.45)
        self.leave_game_button.set_position((self.game.get_width() - self.leave_game_button.width) // 2, self.game.get_height() * 0.45)

