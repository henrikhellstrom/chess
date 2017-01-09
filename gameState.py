from pieceHandler import PieceHandler
from moveHandler import MoveHandler

class GameState:
    def __init__(self):
        self.piece_handler = PieceHandler()
        self.move_handler = MoveHandler()
        self.selected_piece = None

    def draw_pieces(self, surface):
        for piece in self.piece_handler.get_all_pieces():
            piece.draw(surface)

    #Returns possible moves for the selected piece
    def get_moves(self, white_turn):
        if self.selected_piece != None and self.selected_piece.white == white_turn:
            possible_moves = self.move_handler.get_moves(self.selected_piece, self.piece_handler)
            return possible_moves
        return None

    def select_piece(self, square):
        self.selected_piece = self.piece_handler.get_piece_at_pos(square)

    #Moves the selected piece to square
    def move_selected_piece(self, square):
        self.move_handler.move_piece(self.selected_piece, square, self.piece_handler)

