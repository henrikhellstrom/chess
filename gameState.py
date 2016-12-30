from piece import Piece
class GameState:
    pieces = []

    def __init__(self):
        self.init_test_pieces()

    def init_test_pieces(self):
        piece = Piece([0, 0])
        self.pieces.append(piece)
        piece = Piece([2, 5])
        self.pieces.append(piece)

    def draw_pieces(self, surface):
        for piece in self.pieces:
            piece.draw(surface)