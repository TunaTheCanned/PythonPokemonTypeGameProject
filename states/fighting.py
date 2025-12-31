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

        self.p1_sprite_pos = None
        self.p2_sprite_pos = None
        self.p1_stats_pos = None
        self.p2_stats_pos = None
        self.p1_hp_pos = None
        self.p2_hp_pos = None
        self.turn_text_pos = None
        self.buttons_y = None
        self.button_size = None
        self.button_gap = None

        for i in range(4):
            btn = button.Button("", "black", self.font, "white",
                                200, 60, 5,
                                "black", 3, self.game.screen, True)
            btn.set_position(((self.game.get_width() - 200 * 4 + 20 * 3) // 2)+i*(200 + 20), (self.game.get_height() - 60 - 20))
            self.move_buttons.append(btn)

        self.update_move_buttons()
        self.update_layout()



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
        width = int(self.game.screen.get_width() * 0.18)
        height = int(self.game.screen.get_height() * 0.025)

        pygame.draw.rect(self.game.screen, (80, 80, 80), (x, y, width, height))
        ratio = creature.hp / creature.max_hp
        ratio = max(0, min(1, ratio))
        pygame.draw.rect(self.game.screen, (0, 200,  0), (x, y, int(width * ratio), height))
        pygame.draw.rect(self.game.screen, (0, 0, 0), (x, y, width, height), 2)


    def draw(self):
        self.game.renderer.clear((60, 60, 60))

        player1 = self.game.players[0].creature
        player2 = self.game.players[1].creature

        sprite_size = (int(self.game.get_width() * 0.25), int(self.game.get_height() * 0.35))
        self.game.renderer.draw_image(player1.sprite, self.p1_sprite_pos, sprite_size)
        self.game.renderer.draw_text(player1.name, (255, 255, 255), self.p1_stats_pos)

        self.game.renderer.draw_image(player2.sprite, self.p2_sprite_pos, sprite_size)
        self.game.renderer.draw_text(player2.name, (255, 255, 255), self.p2_stats_pos)

        self.draw_healthbar(player1, *self.p1_stats_pos)
        self.draw_healthbar(player2, *self.p2_stats_pos)

        self.game.renderer.draw_text("Attack: " + str(player1.attack), (255, 255, 255), (40, 450))
        self.game.renderer.draw_text("Defense: " + str(player1.defense), (255, 255, 255), (40, 500))
        self.game.renderer.draw_text("Health: " + str(player1.hp), (255, 255, 255), (40, 550))

        self.game.renderer.draw_text("Attack: " + str(player2.attack), (255, 255, 255), (self.game.get_width()-360, 450))
        self.game.renderer.draw_text("Defense: " + str(player2.defense), (255, 255, 255), (self.game.get_width()-360, 500))
        self.game.renderer.draw_text("Health: " + str(player2.hp), (255, 255, 255), (self.game.get_width()-360, 550))

        self.game.renderer.draw_text(f"Player {self.current_turn + 1} turn", (255, 255, 255), self.turn_text_pos)

        for btn in self.move_buttons:
            btn.draw()

    def update_layout(self):
        width = self.game.get_width()
        height = self.game.get_height()
        sprite_w = int(width * 0.25)
        sprite_h = int(height * 0.35)
        left_x = int(width *0.05)
        right_x = int(width * 0.95 - sprite_w)
        sprite_y = int(height * 0.15)
        self.p1_sprite_pos = (left_x, sprite_y)
        self.p2_sprite_pos = (right_x, sprite_y)

        stats_y = sprite_y + sprite_h + int(height * 0.2)
        self.p1_stats_pos = (left_x, stats_y)
        self.p2_stats_pos = (right_x, stats_y)

        self.p1_hp_pos = (left_x, stats_y - int(height * 0.04))
        self.p2_hp_pos = (right_x, stats_y - int(height * 0.04))
        self.turn_text_pos = (width/2 - int(width * 0.08), int(height * 0.03))
        self.button_size = (int(width * 0.18), int(height * 0.07))
        self.button_gap = int(width * 0.02)
        self.buttons_y = int(height * 0.9)
        total_width = 4 * self.button_size[0] + 3 * self.button_gap
        start_x = (width - total_width) / 2

        for i, btn in enumerate(self.move_buttons):
            btn.set_size(*self.button_size)
            btn.set_position(start_x + i * (self.button_size[0] + self.button_gap), self.buttons_y)

    def on_resize(self):
        self.update_layout()