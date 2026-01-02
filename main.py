import pygame

from source.game import Game


if __name__ == "__main__":
    game = Game(1280, 720, "Game")
    try:
        game.run()
    except Exception as e:
        print("Error while running game:", e)
    finally:
        pygame.quit()
