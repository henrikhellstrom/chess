from piece import Piece
import pygame

class Pawn(Piece):
    #white is a boolean
    def __init__(self, white, pos):
        if white == True:
            self.image = pygame.image.load("white_pawn.png")
        else:
            self.image = pygame.image.load("black_pawn.png")
        self.pos = pos