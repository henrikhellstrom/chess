from piece import Piece
import pygame

class Pawn(Piece):
    #white is a boolean
    #pos is a list [x, y], holding square index
    def __init__(self, white, pos):
        if white == True:
            self.image = pygame.image.load("white_pawn.png")
        else:
            self.image = pygame.image.load("black_pawn.png")
        self.pos = pos

    #Returns which moves would be possible on an empty board
    def moves(self):
        ret = []
        if self.white == True:
            if self.pos[1]-1 >= 0:
                ret.append([self.pos[0], self.pos[1]-1])
            if self.pos[1] == 6:
                ret.append([self.pos[0], self.pos[1]-2])
        if self.white == False:
            if self.pos[1]+1 <= 7:
                ret.append([self.pos[0], self.pos[1]+1])
            if self.pos[1] == 1:
                ret.append([self.pos[0], self.pos[1]+2])