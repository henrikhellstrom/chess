from piece import Piece
from pawn import Pawn

class GameState:
    pieces = []

    def __init__(self):
        self.init_pawns()

    def init_pawns(self):
        for x in range(0, 8):
            white_pawn = Pawn(True, [x, 6])
            self.pieces.append(white_pawn)
            black_pawn = Pawn(False, [x, 1])
            self.pieces.append(black_pawn)


    def draw_pieces(self, surface):
        for piece in self.pieces:
            piece.draw(surface)