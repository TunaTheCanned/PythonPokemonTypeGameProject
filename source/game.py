import pygame
from source.game_state import GameState
from source.renderer import Renderer
from states.creature_selection import CreatureSelectionState
from states.fighting import FightingState
from states.message import MessageState
from states.start_menu import StartMenuState
from states.playing import PlayingState
from source.player import Player
from source.creature_loader import load_creature

class Game:
    def __init__(self, width, height, title):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True

        self.renderer = Renderer(self.screen)

        self.game_state = None
        self.change_state(GameState.START_MENU)

        self.creatures = load_creature("C:\\dev\\source\\repos\\PythonProject\\creatures.json")
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player_index = 0
        self.selected_creature = None
        self.battle_result = None

        self.message_text = ""
        self.message_duration = 0.0
        self.message_next_state = None


    def get_height(self):
        return self.screen.get_height()
    def get_width(self):
        return self.screen.get_width()




    def change_state(self, state):
        match state:
            case GameState.START_MENU:
                self.game_state = StartMenuState(self)
            case GameState.GAME_IS_ACTIVE:
                self.game_state = PlayingState(self)
            case GameState.CREATURE_SELECTION:
                self.game_state = CreatureSelectionState(self, self.creatures)
            case GameState.MESSAGE:
                self.game_state = MessageState(self)
            case GameState.FIGHTING:
                self.game_state = FightingState(self)




    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self.screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                self.renderer.screen = self.screen
                self.game_state.on_resize()
            else:
                self.game_state.handle_event(event)




    # def render(self):
    #     self.screen.fill((0, 0, 0))
    #     self.renderer.draw()
    #     #self.renderer.draw_text()
    #     self.screen.display.update()




    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.game_state.update(dt)
            self.game_state.draw()
            pygame.display.flip()

        pygame.quit()


