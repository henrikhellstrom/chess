from piece import Piece
from pawn import Pawn

class GameState:
    pieces = []

    def __init__(self):
        self.init_white_pawns()

    def init_white_pawns(self):
        for x in range(0, 8):
            pawn = Pawn(True, [x, 6])
            self.pieces.append(pawn)

    def draw_pieces(self, surface):
        for piece in self.pieces:
            piece.draw(surface)