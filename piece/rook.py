from piece import Piece
import pygame
import constants

class Rook(Piece):
    #white is a boolean
    #pos is a list [x, y], holding square index
    def __init__(self, white, pos):
        self.white = white
        if white == True:
            self.image = pygame.image.load(constants.image_dir + "/white_rook.png")
        else:
            self.image = pygame.image.load(constants.image_dir + "/black_rook.png")
        self.pos = pos

    #Returns which moves would be possible on an empty board
    def get_all_moves(self):
        ret = []
        for x in range(0, 8):
            if x != self.pos[0]:
                ret.append([x, self.pos[1]])
        for y in range(0, 8):
            if y != self.pos[1]:
                ret.append([self.pos[0], y])
        return ret

    # Returns which moves are possible considering the board state
    def get_possible_moves(self, pieces):
        moves = self.get_all_moves()
        if pieces != None:
            blocked_moves = []
            for move in moves:
                for piece in pieces:
                    if piece.pos[0] == move[0] and piece.pos[1] == move[1]:
                        #Cannot capture your own pieces
                        if piece.white == self.white:
                            blocked_moves.append(move)
                        #Cannot move past piece
                        if piece.pos[0] < self.pos[0]:
                            self.remove_left(blocked_moves, piece)
                        if piece.pos[0] > self.pos[0]:
                            self.remove_right(blocked_moves, piece)
                        if piece.pos[1] < self.pos[1]:
                            self.remove_up(blocked_moves, piece)
                        if piece.pos[1] > self.pos[1]:
                            self.remove_down(blocked_moves, piece)
            for move in blocked_moves:
                if moves.count(move) == 1:
                    moves.remove(move)


        return moves

    #Appends all moves to blocked moves that are to the left of the blocking piece
    def remove_left(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[0] < piece.pos[0]:
                blocked_moves.append(move)

    # Appends all moves to blocked moves that are to the right of the blocking piece
    def remove_right(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[0] > piece.pos[0]:
                blocked_moves.append(move)

    # Appends all moves to blocked moves that are above the blocking piece
    def remove_up(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[1] < piece.pos[1]:
                blocked_moves.append(move)

    # Appends all moves to blocked moves that are below the blocking piece
    def remove_down(self, blocked_moves, piece):
        for move in self.get_all_moves():
            if move[1] > piece.pos[1]:
                blocked_moves.append(move)