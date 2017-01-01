from piece import Piece
import pygame

class Pawn(Piece):
    #white is a boolean
    #pos is a list [x, y], holding square index
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load("white_pawn.png")
        else:
            self.image = pygame.image.load("black_pawn.png")
        self.pos = pos

    #Returns which moves would be possible on an empty board
    def get_all_moves(self):
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
        return ret

    # Returns which moves are possible considering the board state
    def get_possible_moves(self, pieces):
        moves = self.get_all_moves()
        if pieces != None:
            moves_containing_piece = []
            for move in moves:
                for piece in pieces:
                    if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                        moves_containing_piece.append(move)
            for move in moves_containing_piece:
                moves.remove(move)
        #Prevent pawns from being able to jump over pieces
        if len(moves) == 1:
            if abs(moves[0][1] - self.pos[1]) == 2:
                return None
        return moves