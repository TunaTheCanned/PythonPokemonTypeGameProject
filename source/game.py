import pygame
from source.game_state import GameState
from source.renderer import Renderer
from states.creature_selection import CreatureSelectionState
from states.start_menu import StartMenuState
from states.playing import PlayingState
from source.player import Player

class Game:
    def __init__(self, width, height, title):

        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.running = True

        self.renderer = Renderer(self.screen)

        self.game_state = None
        self.change_state(GameState.START_MENU)

        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player_index = 0



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
                self.game_state = CreatureSelectionState(self, 0)

            # case GameState.FIGHTING:
            #     self.game_state = PlayingState(self)




    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
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


