import pygame
from board import Board
from gameState import GameState
import constants

def handle_mouseclick(board, game_state):
    mouse_state = pygame.mouse.get_pressed()
    if mouse_state[0] == True:
        mouse_pos = pygame.mouse.get_pos()
        selected_square = board.select_square(mouse_pos)
        possible_moves = game_state.get_moves(selected_square)
        board.highlight_squares(possible_moves)


if __name__ == "__main__":
    pygame.init()

    board = Board()
    game_state = GameState()
    size = width, height = constants.SQUARE_SIZE*8, constants.SQUARE_SIZE*8
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
                handle_mouseclick(board, game_state)

        screen.fill(black)
        board.draw(screen)
        game_state.draw_pieces(screen)
        pygame.display.flip()

        elapsed_time = pygame.time.get_ticks() - time
        if elapsed_time < 1000/30:
            pygame.time.wait(1000/30-elapsed_time)