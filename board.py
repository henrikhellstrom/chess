import pygame
import math
import constants

#The Board class represents the chess board.
class Board:
    black = 222, 184, 135
    white = 255, 255, 255
    red = 150, 50, 50
    selected_square = [0, 0]

    def select_square(self, pos):
        self.selected_square[0] = math.floor(pos[0]/constants.SQUARE_SIZE)
        self.selected_square[1] = math.floor(pos[1]/constants.SQUARE_SIZE)

    def draw(self, surface):
        for x in range(0, 8):
            for y in range(0, 8):
                rect = pygame.Rect(constants.SQUARE_SIZE*x, constants.SQUARE_SIZE*y, constants.SQUARE_SIZE, constants.SQUARE_SIZE)
                color = self.black
                if x % 2 + y % 2 == 0 or x % 2 + y % 2 == 2:
                    color = self.white
                if x == self.selected_square[0] and y == self.selected_square[1]:
                    color = self.red
                pygame.draw.rect(surface, color, rect)