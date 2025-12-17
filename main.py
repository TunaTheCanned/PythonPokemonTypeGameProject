import time
import keyboard
import pygame
import button

#initialize the game window
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Main Menu")


#variables for main menu
font = pygame.font.SysFont("comicsans", 40)
TEXT_COLOR = (255, 255, 255)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


#game variables
pause = False
running = True
clock = pygame.time.Clock()
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0


#main loop for running the game
while running:

    start_button = button.Button("Start Game", font, "purple", "blue",
                                 160, 160, 300, 100, 5,
                                 "black", 5, screen, True)
    load_game_button = button.Button("Load Game", font, "purple", "yellow",
                                     160, 260, 300, 100, 5,
                                     "black", 5, screen, True)
    leave_game_button = button.Button("Leave Game", font, "purple", "gray",
                                      160, 360, 300, 100, 5,
                                      "black", 5, screen, True)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = True
        if event.type == pygame.QUIT:
            running = False

    screen.fill("red")

    if pause == True:
        draw_text("AAAAAAAAAAAAAAAAAAAAAAAAA", font, TEXT_COLOR, 160, 250)
        start_button.draw()
        load_game_button.draw()
        leave_game_button.draw()
        if start_button.check_click():
            print(start_button.check_click())
    else:
        pass

    pygame.draw.circle(screen, 'yellow', player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    if keys[pygame.K_x]:
        running = False

    # pygame.display.flip()
    pygame.display.update()

    dt = clock.tick(60) / 1000



pygame.quit()