import pygame
from states.state_base import State
from game_state import GameState
import button
import tkinter
from tkinter import filedialog


class StartMenuState(State):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.SysFont("comicsans", 40)


        self.start_button = button.Button("Start Game", self.font,"white", "purple",
                                          300, 100, 5,
                                          "black", 5, game.screen, True)
        self.start_button.set_position(160, 160)


        self.load_game_button = button.Button("Load Game", self.font, "purple", "yellow",
                                              300, 100, 5,
                                              "black", 5, game.screen, True)
        self.load_game_button.set_position(160, 280)


        self.leave_game_button = button.Button("Leave Game", self.font, "purple", "gray",
                                               300, 100, 5,
                                               "black", 5, game.screen, True)
        self.leave_game_button.set_position(160, 400)


    def handle_event(self, event):
        self.start_button.handle_events(event)
        self.load_game_button.handle_events(event)
        self.leave_game_button.handle_events(event)

        if self.start_button.consume_click():
            self.game.change_state(GameState.GAME_IS_ACTIVE)

        elif self.load_game_button.consume_click():
            try:
                tkinter.Tk().withdraw()
                filepath = filedialog.askopenfilename()
                print(filepath)
                #TODO loading data from save
            except:
                #TODO make it catch the exception when user tries to open a wrong file
                print("wrong file extension")


        elif self.leave_game_button.consume_click():
            self.game.running = False




    def update(self, dt):
        pass



    def draw(self):
        self.game.renderer.clear((100, 0, 0))

        self.start_button.draw()
        self.load_game_button.draw()
        self.leave_game_button.draw()
