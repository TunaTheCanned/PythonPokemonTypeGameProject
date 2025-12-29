from game import Game


if __name__ == "__main__":
    game = Game(1280, 720, "Game")
    game.run()

# #initialize the game window
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# pygame.display.set_caption("Main Menu")
#
#
# #variables for main menu
# font = pygame.font.SysFont("comicsans", 40)
# TEXT_COLOR = (255, 255, 255)
#
#
#
#
# #game variables
# game_start_menu = True
# menu_state = "start menu"
# pause = False
# running = True
# clock = pygame.time.Clock()
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# dt = 0
#
# #buttons
# start_button = button.Button("Start Game", font, "purple", "blue",
#                              300, 100, 5,
#                              "black", 5, screen, True)
# load_game_button = button.Button("Load Game", font, "purple", "yellow",
#                                  300, 100, 5,
#                                  "black", 5, screen, True)
# leave_game_button = button.Button("Leave Game", font, "purple", "gray",
#                                   300, 100, 5,
#                                   "black", 5, screen, True)
#
# #main loop for running the game
# while running:
#
#
#     #event type keydown works prints only once on keyboard press
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 pause = True
#             if event.key == pygame.K_ESCAPE:
#                 menu_state = "start menu"
#             if event.key == pygame.K_r:
#                 print('debug')
#         if event.type == pygame.QUIT:
#             running = False
#
#     #ten kod printuje z kazdym tickiem gry
#     #keys = pygame.key.get_pressed()
#     #if keys[pygame.K_b]:
#     #    print('debug b')
#
#     screen.fill("red")
#
#     if menu_state == "start menu":
#
#         start_button.draw(160, 160)
#         load_game_button.draw(160, 260)
#         leave_game_button.draw(160, 360)
#
#         if start_button.check_click():
#             print(start_button.check_click())
#             menu_state = "game is active"
#
#         if load_game_button.check_click():
#             try:
#                 tkinter.Tk().withdraw()
#                 filepath = filedialog.askopenfilename()
#                 print(filepath)
#                 #TODO loading data from save
#             except:
#                 #TODO make it catch the exception when user tries to open a wrong file
#                 print("wrong file extension")
#
#         if leave_game_button.check_click():
#             running = False
#     else:
#         pass
#
#     if menu_state == "game is active":
#         pygame.draw.circle(screen, 'yellow', player_pos, 40)
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_w]:
#             player_pos.y -= 300 * dt
#         if keys[pygame.K_s]:
#             player_pos.y += 300 * dt
#         if keys[pygame.K_a]:
#             player_pos.x -= 300 * dt
#         if keys[pygame.K_d]:
#             player_pos.x += 300 * dt
#         if keys[pygame.K_x]:
#             running = False
#
#     # pygame.display.flip()
#     pygame.display.update()
#
#     dt = clock.tick(60) / 1000
#
#
#
# pygame.quit()

