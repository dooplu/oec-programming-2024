import pygame
from game import Game

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Math Wizard")
    done = False
    clock = pygame.time.Clock()
    game = Game()

    # -------- Main Program Loop -----------
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    main()