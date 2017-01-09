from pieceHandler import PieceHandler

class GameState:
    def __init__(self):
        self.piece_handler = PieceHandler()
        self.selected_piece = None

    def draw_pieces(self, surface):
        for piece in self.piece_handler.get_all_pieces():
            piece.draw(surface)

    #Returns possible moves for the selected piece
    def get_moves(self, white_turn):
        if self.selected_piece != None and self.selected_piece.white == white_turn:
            moves = self.selected_piece.get_all_moves()
            other_pieces = self.piece_handler.get_pieces_at_positions(moves)
            possible_moves = self.selected_piece.get_possible_moves(other_pieces)
            return possible_moves
        return None

    def select_piece(self, square):
        self.selected_piece = self.piece_handler.get_piece_at_pos(square)

    #Moves the selected piece to square
    def move_selected_piece(self, square):
        piece_at_target = self.piece_handler.get_piece_at_pos(square)
        if piece_at_target != None:
            self.piece_handler.remove_piece(piece_at_target)
        self.selected_piece.move(square)

