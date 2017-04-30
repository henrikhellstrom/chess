from piece import Piece
import pygame
import constants

class Bishop(Piece):
    #white is a boolean
    #pos is a list [x, y], holding square index
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_bishop.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_bishop.png")
        self.pos = pos
        self.type = "bishop"

    #Returns which moves would be possible on an empty board
    def get_all_moves(self):
        ret = []
        for x in range(-7, 8):
            for y in range(-7, 8):
                if self.pos[0]+x >= 0 and self.pos[0]+x <= 7 and self.pos[1]+y >= 0 and self.pos[1]+y <= 7:
                    if abs(x) == abs(y):
                        ret.append([self.pos[0]+x, self.pos[1]+y])
        return ret

    # Remove all moves blocked by movement and return the remaining moves
    def remove_blocked_moves(self, pieces):
        ret = self.get_all_moves()
        moves_with_piece = self.get_moves_containing_piece(pieces)
        for move in moves_with_piece:
            for piece in pieces:
                if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                    if piece.white == self.white:
                        if ret.count(move) > 0:
                            ret.remove(move)
            if move[0] > self.pos[0] and move[1] > self.pos[1]:
                self.remove_below_right(ret, move)
            if move[0] < self.pos[0] and move[1] > self.pos[1]:
                self.remove_below_left(ret, move)
            if move[0] > self.pos[0] and move[1] < self.pos[1]:
                self.remove_above_right(ret, move)
            if move[0] < self.pos[0] and move[1] < self.pos[1]:
                self.remove_above_left(ret, move)


        return ret

    def get_moves_containing_piece(self, pieces):
        moves = self.get_all_moves()
        moves_containing_piece = []
        if pieces != None:
            for move in moves:
                for piece in pieces:
                    if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                        moves_containing_piece.append(move)
        return moves_containing_piece

    #Removes all moves from moves that are to below and to the right of piece_square
    def remove_below_right(self, moves, piece_square):
        blocked_moves = []
        for move in moves:
            if move[0] > piece_square[0] and move[1] > piece_square[1]:
                blocked_moves.append(move)
        for move in blocked_moves:
            moves.remove(move)

    #Removes all moves from moves that are to below and to the right of piece_square
    def remove_below_left(self, moves, piece_square):
        blocked_moves = []
        for move in moves:
            if move[0] < piece_square[0] and move[1] > piece_square[1]:
                blocked_moves.append(move)
        for move in blocked_moves:
            moves.remove(move)

    #Removes all moves from moves that are to below and to the right of piece_square
    def remove_above_right(self, moves, piece_square):
        blocked_moves = []
        for move in moves:
            if move[0] > piece_square[0] and move[1] < piece_square[1]:
                blocked_moves.append(move)
        for move in blocked_moves:
            moves.remove(move)

    #Removes all moves from moves that are to below and to the right of piece_square
    def remove_above_left(self, moves, piece_square):
        blocked_moves = []
        for move in moves:
            if move[0] < piece_square[0] and move[1] < piece_square[1]:
                blocked_moves.append(move)
        for move in blocked_moves:
            moves.remove(move)