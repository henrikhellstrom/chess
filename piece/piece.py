import pygame
import constants

#The Piece class represents a general chess piece
class Piece:
    yellow = (255, 255, 0)

    #pos should be defined as [x, y] where x and y takes values between 0 and 7
    def __init__(self, pos, white):
        self.pos = pos
        self.image = None
        self.white = white

    def draw(self, surface):
        pixel_pos = [0, 0]
        if self.image == None:
            pixel_pos[0] = self.pos[0]*constants.SQUARE_SIZE + constants.SQUARE_SIZE/2
            pixel_pos[1] = self.pos[1]*constants.SQUARE_SIZE + constants.SQUARE_SIZE/2
            pygame.draw.circle(surface, self.yellow, pixel_pos, constants.SQUARE_SIZE/3)
        else:
            pixel_pos[0] = self.pos[0]*constants.SQUARE_SIZE
            pixel_pos[1] = self.pos[1]*constants.SQUARE_SIZE
            rect = pygame.Rect(pixel_pos[0], pixel_pos[1], constants.SQUARE_SIZE, constants.SQUARE_SIZE)
            surface.blit(self.image, rect)

    # Returns which moves would be possible on an empty board
    def get_all_moves(self):
        moves = []
        return moves

    #Returns which moves is possible considering the board state
    def get_possible_moves(self, pieces):
        moves = []
        return moves

    def move(self, pos):
        self.pos = pos