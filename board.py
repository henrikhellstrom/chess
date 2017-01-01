import pygame
import math
import constants

#The Board class represents the chess board. It handles the graphical representation of the board and conversion of
#mouse coordinates to square index.
class Board:

    def __init__(self):
        self.black = 222, 184, 135
        self.white = 255, 255, 255
        self.red = 255, 0, 0
        self.blue = 100, 149, 237

    #Takes a pixel position as parameter, returns square index position.
    def get_square(self, pos):
        ret = [0, 0]
        ret[0] = math.floor(pos[0]/constants.SQUARE_SIZE)
        ret[1] = math.floor(pos[1]/constants.SQUARE_SIZE)
        return ret

    #Draws white and black squares tiled across surface
    def draw_board(self, surface):
        for x in range(0, 8):
            for y in range(0, 8):
                rect = pygame.Rect(constants.SQUARE_SIZE*x, constants.SQUARE_SIZE*y, constants.SQUARE_SIZE, constants.SQUARE_SIZE)
                color = self.black
                if x % 2 + y % 2 == 0 or x % 2 + y % 2 == 2:
                    color = self.white
                pygame.draw.rect(surface, color, rect)

    def draw_selected_square(self, surface, selected_square):
        self.draw_transparent_square(selected_square, self.red, surface)

    def draw_highlighted_squares(self, surface, highlighted_squares):
        if highlighted_squares != None:
            for square in highlighted_squares:
                self.draw_transparent_square(square, self.blue, surface)

    def draw(self, surface, selected_square, highlighted_squares):
        self.draw_board(surface)
        self.draw_selected_square(surface, selected_square)
        self.draw_highlighted_squares(surface, highlighted_squares)

    #Draws a square with alpha coding to make it transparent.
    def draw_transparent_square(self, pos, color, surface):
        s = pygame.Surface((constants.SQUARE_SIZE, constants.SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(color)
        surface.blit(s, (constants.SQUARE_SIZE * pos[0], constants.SQUARE_SIZE * pos[1]))