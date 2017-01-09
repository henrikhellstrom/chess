#The move handler is responsible for retrieving which moves are possible for
#different pieces, using the pieces internal methods
class MoveHandler:
    def __init__(self):
        pass

    # Returns possible moves for piece
    def get_moves(self, piece, piece_handler):
        moves = piece.get_all_moves()
        other_pieces = piece_handler.get_pieces_at_positions(moves)
        possible_moves = piece.get_possible_moves(other_pieces)
        return possible_moves

    # Returns possibles moves for all pieces
    def get_all_moves(self, piece_handler):
        all_possible_moves = []
        for piece in piece_handler.get_all_pieces():
            piece_moves = self.get_moves(piece, piece_handler)
            all_possible_moves.append(piece_moves)
        return all_possible_moves

    def move_piece(self, piece, destination, piece_handler):
        piece_at_destination = piece_handler.get_piece_at_pos(destination)
        if piece_at_destination != None:
            piece_handler.remove_piece(piece_at_destination)
        piece.move(destination)