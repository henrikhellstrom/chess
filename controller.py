from board import Board
from gameState import GameState
import pygame

#This class is the middle hand between user input and the GameState and Board class.
class Controller:
    def __init__(self):
        self.board = Board()
        self.game_state = GameState()
        self.selected_square = [0, 0]
        self.possible_moves = []

    def select_square(self, square):
        self.selected_square = square
        self.game_state.select_piece(self.selected_square)
        self.possible_moves = self.game_state.get_moves()

    def handle_mouseclick(self):
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0] == True:
            mouse_pos = pygame.mouse.get_pos()
            pressed_square = self.board.get_square(mouse_pos)
            if self.is_possible_move(pressed_square):
                self.game_state.move_selected_piece(pressed_square)
            self.select_square(pressed_square)

    #Returns true if square is a possible move
    def is_possible_move(self, square):
        if self.possible_moves == None:
            return False
        else:
            for move in self.possible_moves:
                if square[0] == move[0] and square[1] == move[1]:
                    return True
            return False

    def draw(self, surface):
        self.board.draw(surface, self.selected_square, self.possible_moves)
        self.game_state.draw_pieces(surface)