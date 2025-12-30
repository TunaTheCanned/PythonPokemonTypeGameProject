import pygame

from source import button
from states.state import State


class FightingState(State):
    def __init__(self, game):
        super().__init__(game)

        self.current_turn = 0
        self.move_buttons = []
        self.font = pygame.font.SysFont("comicsans", 40)

        for i in range(4):
            btn = button.Button("", "black", self.font, "white",
                                200, 60, 5,
                                "black", 3, self.game.screen, True)
            btn.set_position(((self.game.get_width() - 200 * 4 + 20 * 3) // 2)+i*(200 + 20), (self.game.get_height() - 60 - 20))
            self.move_buttons.append(btn)

        self.update_move_buttons()




    def update_move_buttons(self):

        for i in range(4):
            if i < len(self.game.players[self.current_turn].creature.moves):
                self.move_buttons[i].text = self.game.players[self.current_turn].creature.moves[i]
                self.move_buttons[i].text_surface = self.move_buttons[i].font.render(self.move_buttons[i].text, True, self.move_buttons[i].text_color)
            else:
                self.move_buttons[i].text = "none"
                self.move_buttons[i].text_surface = self.move_buttons[i].font.render(self.move_buttons[i].text, True, self.move_buttons[i].text_color)



    def handle_event(self, event):
        for btn in self.move_buttons:
            btn.handle_events(event)
            if btn.consume_click():
                self.end_turn()

    def end_turn(self):
        self.current_turn = 1 - self.current_turn
        self.update_move_buttons()

    def update(self, dt):
        pass

    def draw(self):
        self.game.renderer.clear((60, 60, 60))
        player1 = self.game.players[0].creature
        player2 = self.game.players[1].creature
        self.game.renderer.draw_image(player1.sprite, (40, 120))
        self.game.renderer.draw_image(player2.sprite, (self.game.get_width() - 360, 120))
        self.game.renderer.draw_text(f"Player {self.current_turn + 1}'s turn", (255, 255, 255), (self.game.get_width() // 2 - 100, 20))

        for btn in self.move_buttons:
            btn.draw()