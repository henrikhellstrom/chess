#The move handler is responsible for retrieving which moves are possible for
#different pieces, using the pieces internal methods
class MoveHandler:
    def __init__(self):
        pass

    # Returns possible moves for piece
    def get_moves(self, piece, piece_handler):
        #Get all moves possible given an empty board
        moves = piece.get_all_moves()
        other_pieces = piece_handler.get_pieces_at_positions(moves)
        #Remove all moves that are blocked by movement
        moves = piece.remove_blocked_moves(other_pieces)
        #Remove all moves that are blocked by check
        moves = self.remove_checked_moves(piece, piece_handler, moves)

        return moves

    # Returns possible moves for piece without checking if it will be self-checking.
    # Only used internally, private method.
    def get_moves_without_check(self, piece, piece_handler):
        # Get all moves possible given an empty board
        moves = piece.get_all_moves()
        other_pieces = piece_handler.get_pieces_at_positions(moves)
        # Remove all moves that are blocked by movement
        moves = piece.remove_blocked_moves(other_pieces)

        return moves

    # Removes all moves that are blocked by check
    def remove_checked_moves(self, piece, piece_handler, moves):
        ret = moves[:]
        original_location = piece.pos
        print("moves:")
        print(moves)
        for move in moves:
            #Capture piece
            captured_piece = piece_handler.get_piece_at_pos(move)
            #Move the piece
            piece.move(move)
            if(captured_piece != None and captured_piece.type != "king"):
                piece_handler.remove_piece(captured_piece)
            print("move:")
            print(move)
            print(self.is_there_check(not piece.white, piece_handler))
            if(self.is_there_check(not piece.white, piece_handler) is True):
                ret.remove(move)
            #Replace the captured piece
            if (captured_piece != None and captured_piece.type != "king"):
                piece_handler.add_piece(captured_piece)
        piece.move(original_location)
        return ret

    # Returns true if there is a check on the board for player specified by white
    def is_there_check(self, white, piece_handler):
        king = piece_handler.get_king(not white)
        all_opponent_pieces = piece_handler.get_pieces_with_color(white)
        for opponent_piece in all_opponent_pieces:
            opponent_moves = self.get_moves_without_check(opponent_piece, piece_handler)

            for opponent_move in opponent_moves:
                if opponent_move == king.pos:
                    return True
        return False

    # Returns possibles moves for all pieces of color white
    def get_all_moves(self, piece_handler, white):
        all_possible_moves = []
        for piece in piece_handler.get_all_pieces():
            if(piece.white == white):
                piece_moves = self.get_moves(piece, piece_handler)
                all_possible_moves.append(piece_moves)
        return all_possible_moves

    def move_piece(self, piece, destination, piece_handler):
        piece_at_destination = piece_handler.get_piece_at_pos(destination)
        if piece_at_destination != None:
            piece_handler.remove_piece(piece_at_destination)
        piece.move(destination)