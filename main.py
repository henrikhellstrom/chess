import pygame
from board import Board
from gameState import GameState

def handle_mouseclick(board):
    mouse_state = pygame.mouse.get_pressed()
    if mouse_state[0] == True:
        mouse_pos = pygame.mouse.get_pos()
        board.select_square(mouse_pos)

if __name__ == "__main__":
    pygame.init()

    board = Board()
    game_state = GameState()
    size = width, height = 640, 640
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)
    pieces = []

    running = 1

    while running:
        time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouseclick(board)

        screen.fill(black)
        board.draw(screen)
        game_state.draw_pieces(screen)
        pygame.display.flip()

        elapsed_time = pygame.time.get_ticks() - time
        if elapsed_time < 1000/30:
            pygame.time.wait(1000/30-elapsed_time)