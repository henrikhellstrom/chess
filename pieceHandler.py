from piece.pawn import Pawn
from piece.rook import Rook
from piece.knight import Knight
from piece.bishop import Bishop
from piece.queen import Queen
from piece.king import King

#This class holds a list of all pieces. It's respoinsibilities include intializing pieces and piece retrieval
class PieceHandler:
    def __init__(self):
        self.pieces = []
        self.init_pieces()

    def init_pieces(self):
        self.init_pawns()
        self.init_rooks()
        self.init_knights()
        self.init_bishops()
        self.init_queens()
        self.init_kings()

    def init_pawns(self):
        for x in range(0, 8):
            white_pawn = Pawn(True, [x, 6])
            self.pieces.append(white_pawn)
            black_pawn = Pawn(False, [x, 1])
            self.pieces.append(black_pawn)

    def init_queens(self):
        self.pieces.append(Queen(True, [3, 7]))
        self.pieces.append(Queen(False, [3, 0]))

    def init_rooks(self):
        self.pieces.append(Rook(True, [0, 7]))
        self.pieces.append(Rook(True, [7, 7]))
        self.pieces.append(Rook(False, [0, 0]))
        self.pieces.append(Rook(False, [7, 0]))

    def init_knights(self):
        self.pieces.append(Knight(True, [1, 7]))
        self.pieces.append(Knight(True, [6, 7]))
        self.pieces.append(Knight(False, [1, 0]))
        self.pieces.append(Knight(False, [6, 0]))

    def init_bishops(self):
        self.pieces.append(Bishop(True, [2, 7]))
        self.pieces.append(Bishop(True, [5, 7]))
        self.pieces.append(Bishop(False, [2, 0]))
        self.pieces.append(Bishop(False, [5, 0]))

    def init_kings(self):
        self.pieces.append(King(True, [4, 7]))
        self.pieces.append(King(False, [4, 0]))

    def get_all_pieces(self):
        return self.pieces

    def get_pieces_with_color(self, white):
        ret = []
        for piece in self.pieces:
            if piece.white == white:
                ret.append(piece)
        return ret

    def get_king(self, white):
        for piece in self.pieces:
            if piece.type == "king" and piece.white == white:
                return piece

    # Returns a list of pieces placed at list of positions
    def get_pieces_at_positions(self, positions):
        pieces = []
        for pos in positions:
            piece = self.get_piece_at_pos(pos)
            if piece != None:
                pieces.append(piece)
        return pieces

    # Returns piece at pos
    def get_piece_at_pos(self, pos):
        for piece in self.pieces:
            if piece.pos[0] == pos[0] and piece.pos[1] == pos[1]:
                return piece
        return None

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def add_piece(self, piece):
        self.pieces.append(piece)