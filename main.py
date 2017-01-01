import pygame
from controller import Controller
import constants

if __name__ == "__main__":
    pygame.init()

    controller = Controller()
    size = width, height = constants.SQUARE_SIZE*8, constants.SQUARE_SIZE*8
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    running = 1

    while running:
        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                controller.handle_mouseclick()

        screen.fill(black)
        controller.draw(screen)
        pygame.display.flip()

        elapsed_time = pygame.time.get_ticks() - time
        if elapsed_time < 1000/30:
            pygame.time.wait(1000/30-elapsed_time)