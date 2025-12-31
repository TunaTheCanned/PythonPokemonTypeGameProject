import pygame

from source import button
from source.game_state import GameState
from states.state import State
from source.moves import perform_move

class FightingState(State):
    def __init__(self, game):
        super().__init__(game)

        self.current_turn = 0
        self.move_buttons = []
        # self.font = pygame.font.SysFont("arial", 40)
        self.font = pygame.font.Font("C:\\dev\\source\\repos\\PythonProject\\Minecraft.ttf", 40)

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


    def use_move(self, move_name):
        attacker = self.game.players[self.current_turn].creature
        defender = self.game.players[1 - self.current_turn].creature
        perform_move(move_name, attacker, defender)
        if defender.hp <= 0:
            self.game.message_text = f"{attacker.name} wins"
            self.game.message_duration = 1.0
            self.game.message_next_state = GameState.START_MENU
            self.game.change_state(GameState.MESSAGE)

        self.end_turn()

    def handle_event(self, event):
        for btn in self.move_buttons:
            btn.handle_events(event)
            if btn.consume_click():
                self.use_move(btn.text)


    def end_turn(self):
        self.current_turn = 1 - self.current_turn
        self.update_move_buttons()

    def update(self, dt):
        pass


    def draw_healthbar(self, creature, x, y):
        width = 250
        height = 20

        pygame.draw.rect(self.game.screen, (80, 80, 80), (x, y, width, height))
        ratio = creature.hp / creature.max_hp
        ratio = max(0, min(1, ratio))
        pygame.draw.rect(self.game.screen, (0, 200,  0), (x, y, int(width * ratio), height))
        pygame.draw.rect(self.game.screen, (0, 0, 0), (x, y, width, height), 2)


    def draw(self):
        self.game.renderer.clear((60, 60, 60))
        player1 = self.game.players[0].creature
        player2 = self.game.players[1].creature
        self.game.renderer.draw_image(player1.sprite, (40, 120))
        self.game.renderer.draw_text(player1.name, (255, 255, 255), (40, 350))
        self.game.renderer.draw_image(player2.sprite, (self.game.get_width() - 360, 120))
        self.game.renderer.draw_text(player2.name, (255, 255, 255), (self.game.get_width()-360, 350))
        self.draw_healthbar(player1, 40, 420)
        self.draw_healthbar(player2, self.game.get_width() - 360, 420)

        self.game.renderer.draw_text("Attack: " + str(player1.attack), (255, 255, 255), (40, 450))
        self.game.renderer.draw_text("Defense: " + str(player1.defense), (255, 255, 255), (40, 500))
        self.game.renderer.draw_text("Health: " + str(player1.hp), (255, 255, 255), (40, 550))

        self.game.renderer.draw_text("Attack: " + str(player2.attack), (255, 255, 255), (self.game.get_width()-360, 450))
        self.game.renderer.draw_text("Defense: " + str(player2.defense), (255, 255, 255), (self.game.get_width()-360, 500))
        self.game.renderer.draw_text("Health: " + str(player2.hp), (255, 255, 255), (self.game.get_width()-360, 550))

        self.game.renderer.draw_text(f"Player {self.current_turn + 1} turn", (255, 255, 255), (self.game.get_width() // 2 - 100, 20))

        for btn in self.move_buttons:
            btn.draw()