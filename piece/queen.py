from piece import Piece
import pygame
import constants

class Queen(Piece):
    #white is a boolean
    #pos is a list [x, y], holding square index
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_queen.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_queen.png")
        self.pos = pos

    #Returns which moves would be possible on an empty board
    def get_all_moves(self):
        ret = []
        #"Rook moves"
        for x in range(0, 8):
            for y in range(0, 8):
                if x == self.pos[0] and y != self.pos[1]:
                    ret.append([x, y])
                if y == self.pos[1] and x != self.pos[0]:
                    ret.append([x, y])
        #"Bishop moves"
        for x in range(-7, 8):
            for y in range(-7, 8):
                if abs(x) == abs(y) and x != 0:
                    if self.pos[0]+x >= 0 and self.pos[0]+x < 8 and self.pos[1]+y >= 0 and self.pos[1]+y < 8:
                        move = [self.pos[0] + x, self.pos[1] + y]
                        ret.append(move)
        return ret

    # Returns which moves are possible considering the board state
    def get_possible_moves(self, pieces):
        ret = self.get_all_moves()
        moves_with_piece = self.get_moves_containing_piece(pieces)
        blocked_moves = []

        for move in moves_with_piece:
            for piece in pieces:
                if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                    if piece.white == self.white and blocked_moves.count(move) == 0:
                        blocked_moves.append(move)
            for blocked_move in self.get_blocked_moves(ret, move):
                if blocked_moves.count(blocked_move) == 0:
                    blocked_moves.append(blocked_move)

        for move in blocked_moves:
            ret.remove(move)

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

    #all_moves = List of all possible moves
    #piece_move = move containing piece
    #Returns: List of moves that are blocked by piece at piece_move
    def get_blocked_moves(self, all_moves, piece_move):
        ret = []
        if piece_move[0] < self.pos[0] and piece_move[1] == self.pos[1]:
            ret = self.left_blocked(all_moves, piece_move)
        if piece_move[0] > self.pos[0] and piece_move[1] == self.pos[1]:
            ret = self.right_blocked(all_moves, piece_move)
        if piece_move[1] < self.pos[1] and piece_move[0] == self.pos[0]:
            ret = self.above_blocked(all_moves, piece_move)
        if piece_move[1] > self.pos[1] and piece_move[0] == self.pos[0]:
            ret = self.below_blocked(all_moves, piece_move)
        if piece_move[0] < self.pos[0] and piece_move[1] < self.pos[1]:
            ret = self.above_left_blocked(all_moves, piece_move)
        if piece_move[0] > self.pos[0] and piece_move[1] < self.pos[1]:
            ret = self.above_right_blocked(all_moves, piece_move)
        if piece_move[0] < self.pos[0] and piece_move[1] > self.pos[1]:
            ret = self.below_left_blocked(all_moves, piece_move)
        if piece_move[0] > self.pos[0] and piece_move[1] > self.pos[1]:
            ret = self.below_right_blocked(all_moves, piece_move)
        return ret


    def left_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] < piece_move[0] and move[1] == piece_move[1]:
                ret.append(move)
        return ret

    def right_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] > piece_move[0] and move[1] == piece_move[1]:
                ret.append(move)
        return ret

    def above_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[1] < piece_move[1] and move[0] == piece_move[0]:
                ret.append(move)
        return ret

    def below_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[1] > piece_move[1] and move[0] == piece_move[0]:
                ret.append(move)
        return ret

    def above_left_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] < piece_move[0] and move[1] < piece_move[1]:
                ret.append(move)
                print "Removing: " + str(move[0]) + ", " + str(move[1])
        return ret

    def below_left_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] < piece_move[0] and move[1] > piece_move[1]:
                ret.append(move)
        return ret

    def above_right_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] > piece_move[0] and move[1] < piece_move[1]:
                ret.append(move)
        return ret

    def below_right_blocked(self, all_moves, piece_move):
        ret = []
        for move in all_moves:
            if move[0] > piece_move[0] and move[1] > piece_move[1]:
                ret.append(move)
        return ret