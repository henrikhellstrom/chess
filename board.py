import pygame
import math
import constants

#The Board class represents the chess board.
class Board:
    black = 222, 184, 135
    white = 255, 255, 255
    red = 255, 0, 0
    blue = 100, 149, 237
    selected_square = [0, 0]

    def __init__(self):
        self.highlighted_squares = []

    #Takes a pixel position as parameter, returns square index position. Also fills selected square with a red color.
    def select_square(self, pos):
        self.selected_square[0] = math.floor(pos[0]/constants.SQUARE_SIZE)
        self.selected_square[1] = math.floor(pos[1]/constants.SQUARE_SIZE)
        return (self.selected_square[0], self.selected_square[1])

    def draw(self, surface):
        for x in range(0, 8):
            for y in range(0, 8):
                rect = pygame.Rect(constants.SQUARE_SIZE*x, constants.SQUARE_SIZE*y, constants.SQUARE_SIZE, constants.SQUARE_SIZE)
                color = self.black
                if x % 2 + y % 2 == 0 or x % 2 + y % 2 == 2:
                    color = self.white
                pygame.draw.rect(surface, color, rect)
                if x == self.selected_square[0] and y == self.selected_square[1]:
                    self.draw_transparent_square(self.selected_square, self.red, surface)
        if self.highlighted_squares != None:
            for square in self.highlighted_squares:
                self.draw_transparent_square(square, self.blue, surface)

    #Draws a square with alpha coding to make it transparent.
    def draw_transparent_square(self, pos, color, surface):
        s = pygame.Surface((constants.SQUARE_SIZE, constants.SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(color)
        surface.blit(s, (constants.SQUARE_SIZE * pos[0], constants.SQUARE_SIZE * pos[1]))


    #Takes list of positions and sets them to be highlighted squares
    def highlight_squares(self, positions):
        self.highlighted_squares = positions