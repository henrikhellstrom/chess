from piece import Piece
from pawn import Pawn

class GameState:
    def __init__(self):
        self.pieces = []
        self.init_pawns()
        self.selected_piece = None

    def init_pawns(self):
        for x in range(0, 8):
            white_pawn = Pawn(True, [x, 6])
            self.pieces.append(white_pawn)
            black_pawn = Pawn(False, [x, 1])
            self.pieces.append(black_pawn)

    def draw_pieces(self, surface):
        for piece in self.pieces:
            piece.draw(surface)

    #Returns possible moves for the selected piece
    def get_moves(self):
        if self.selected_piece != None:
            moves = self.selected_piece.get_all_moves()
            other_pieces = self.get_pieces_at_positions(moves)
            possible_moves = self.selected_piece.get_possible_moves(other_pieces)
            return possible_moves
        return None

    #Returns a list of pieces placed at list of positions
    def get_pieces_at_positions(self, positions):
        pieces = []
        for pos in positions:
            piece = self.get_piece_at_pos(pos)
            if piece != None:
                pieces.append(piece)
        return pieces

    #Returns piece at pos
    def get_piece_at_pos(self, pos):
        for piece in self.pieces:
            if piece.pos[0] == pos[0] and piece.pos[1] == pos[1]:
                return piece
        return None

    def select_piece(self, square):
        self.selected_piece = None
        for piece in self.pieces:
            if piece.pos[0] == square[0] and piece.pos[1] == square[1]:
                self.selected_piece = piece

    def move_selected_piece(self, square):
        self.selected_piece.move(square)