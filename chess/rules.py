import re

class Rules:
    def __init__(self):
        pass

    @classmethod
    def validate_move(cls, move, game):
        """Check if a move is valid using all the rules of chess.
        Returns a tuple of (is_valid, reason,captured_piece_square).
        """
        board = game.board
        white_to_play = game.white_to_play
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        source_piece = board.get(source)
        dest_piece = board.get(dest)
        
        if dest_piece is not None and dest_piece._is_white != white_to_play:
            captured_piece_location = dest
        else:
            captured_piece_location = None
        

        if cls.check_input(move) is None:
            return (False, 'Enter a valid command.',captured_piece_location)

        # check if source piece is valid
        if source_piece is None:
            return (False,'No piece at source position.',captured_piece_location)

        # check if source piece is the right color
        if source_piece._is_white != white_to_play:
            return (False, 'Wrong color piece at source position.',captured_piece_location)
        
        # check if dest piece is the same color
        if dest_piece is not None and dest_piece._is_white == white_to_play:
            captured_piece_location = dest
            return (False, 'Wrong color piece at destination position.',captured_piece_location)

        #check that path is clear
        if not cls.check_path_is_clear(move, board):
            return (False, 'Path is not clear.',captured_piece_location)

        # get valid moves for source piece
        valid_moves = source_piece.valid_moves(source)

        #check if move is a pawn special case
        if(source_piece.type_enum ==1 and cls.check_pawn_capture(move, board, white_to_play)):
            #add pawn special cases to valid moves if conditions hold
            captured_piece_location = dest
            valid_moves.append(move[2:])

        en_passant_is_legal,adjacent_square = cls.check_pawn_en_passant(move, board, white_to_play)
        if(en_passant_is_legal):
            #add pawn special cases to valid moves if conditions hold
            valid_moves.append(move[2:])
            captured_piece_location = adjacent_square

        #check if move is a castle
        if(source_piece.type_enum == 6 and cls.is_castle_move(move)):
            castling_is_legal  = cls.check_castle(move, board, white_to_play)
            if castling_is_legal:
            #add castle to valid moves if conditions hold
                valid_moves.append(move[2:])

        #check if move is a valid move according to piece movement rules
        if dest not in valid_moves:
            return (False, 'Invalid move for piece.',captured_piece_location)
        
        # if cls.check_dest_piece_is_not_king(move, board) is False:
        #     return (False, 'Cannot actually capture King.',captured_piece_location)
        #check if move puts own king in check
        if cls.check_if_move_leaves_own_king_in_check(move, game):
            return (False, 'Move puts own king in check.',captured_piece_location)
                
        return (True, 'Valid move.', captured_piece_location)
    
    @classmethod
    def is_castle_move(cls, move):
        """Check if a move is a castle move."""
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        if source == 'e1' and dest in ('c1', 'g1'):
            return True
        if source == 'e8' and dest in ('c8', 'g8'):
            return True
        return False

    @classmethod
    def check_path_is_clear(cls,move,board):
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        source_piece = board.get(source)
        if(source_piece is not None and source_piece.type_enum!= 3):
            path = source_piece.get_path(source,dest)
            for square in path:
                if board.get(square) is not None and square != dest:
                    return False
        return True

    
    @classmethod
    def check_dest_piece_is_not_king(cls,move,board):
        dest = cls.get_dest_pos(move)
        dest_piece = board.get(dest)
        if(dest_piece is not None and dest_piece.type_enum == 6):
            return False
        return True
    
    @classmethod
    def check_if_move_leaves_own_king_in_check(cls, move, game):
        board = game.board
        white_to_play = game.white_to_play
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        dest_piece = board.get(dest)

        game.move_piece(source, dest)
        if white_to_play:
            king_pos = board.king_location(is_white=True)
        else:
            king_pos = board.king_location(is_white=False)
        enemy_pieces_loc = board.get_piece_locations(is_white= not white_to_play)
        for loc in enemy_pieces_loc:
            enemy_piece = board.get(loc)
            enemy_movements = enemy_piece.valid_moves(loc)
            if(enemy_piece.type_enum == 5):
                print('Queen moves')

                print(enemy_movements)
                print('King pos')
                print(king_pos)
            if king_pos in enemy_movements and cls.check_path_is_clear(loc+king_pos, board):
                print('King is in check!')
                print(loc+king_pos)
                game.move_piece(dest, source)
                board.set(dest, dest_piece)
                return True
        game.move_piece(dest, source)
        board.set(dest, dest_piece)
        return False

    
    @classmethod
    def check_if_own_king_is_in_checkmate(cls, game):
        board = game.board
        white_to_play = game.white_to_play

        own_pieces_loc = board.get_piece_locations(is_white= white_to_play)
        for loc in own_pieces_loc:
            own_piece = board.get(loc)
            own_movements = own_piece.valid_moves(loc)
            for move in own_movements:
                test_move = loc+move
                if cls.validate_move(test_move, game)[0] is True:
                    print(test_move)
                    print('is valid')
                    return False
                else:
                    print(test_move)
                    print('is not valid')
                    # if cls.check_if_move_leaves_own_king_in_check(loc+move, game) is False:
                    #     print(loc+move)
                    #     print('not checkmate')
                    #     return False
                
        print('checkmate')
        return True    


    @classmethod
    def check_if_king_is_currently_in_check(cls, game):
        board = game.board
        white_to_play = game.white_to_play
        if white_to_play:
            king_pos = board.king_location(is_white=True)
        else:
            king_pos = board.king_location(is_white=False)
        enemy_pieces_loc = board.get_piece_locations(is_white= not white_to_play)
        for loc in enemy_pieces_loc:
            enemy_piece = board.get(loc)
            enemy_movements = enemy_piece.valid_moves(loc)
            if king_pos in enemy_movements and cls.check_path_is_clear(loc+king_pos, board):
                return True
        return False
            
    @classmethod
    def check_pawn_capture(cls, move, board, white_to_play):
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        dest_piece = board.get(dest)
        #Check if pawn move is diagonal
        diagonal_move_boolean = abs(cls.horizontal_difference(source,dest)) == 1 and abs(cls.vertical_difference(source,dest)) == 1

        #Check if pawn move is forward
        forward_movement_boolean = cls.vertical_difference(source,dest) == 1 if white_to_play else cls.vertical_difference(source,dest) == -1

        #Check if destination square is not empty
        capture_boolean = dest_piece is not None and dest_piece._is_white != white_to_play

        #returns true if pawn capture is valid move
        return diagonal_move_boolean and forward_movement_boolean and capture_boolean

    @classmethod
    def check_pawn_en_passant(cls, move, board, white_to_play):
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        
        #Check if pawn move is diagonal
        diagonal_move_boolean = abs(cls.horizontal_difference(source,dest)) == 1 and abs(cls.vertical_difference(source,dest)) == 1

        #Check if pawn move is forward
        forward_movement_boolean = cls.vertical_difference(source,dest) == 1 if white_to_play else cls.vertical_difference(source,dest) == -1

        #Check if destination square is empty
        dest_piece = board.get(dest)
        dest_square_is_empty = dest_piece is None

        #Get horizontal difference between source and destination
        horizontal_difference = cls.horizontal_difference(source,dest)

        #Get adjacent square
        adj_square = chr(ord(source[0]) + horizontal_difference) + source[1]

        #Get piece on adjacent square
        adj_piece = board.get(adj_square)

        #Check if piece is enemy pawn that just moved
        adj_piece_is_enemy_pawn_that_just_moved = adj_piece is not None and \
                                    adj_piece.type_enum == 1 and \
                                    adj_piece._is_white != white_to_play and \
                                    adj_piece.just_moved_two_squares


        all_conditions = diagonal_move_boolean and \
                forward_movement_boolean and \
                dest_square_is_empty and \
                adj_piece_is_enemy_pawn_that_just_moved
        
        #returns true if proposed en passant is valid move
        return all_conditions, adj_square
    
    @classmethod
    def get_source_pos(self, move):
        return move[:2]
    @classmethod
    def get_dest_pos(self, move):
        return move[2:]

    @classmethod
    def check_input(self, move):
        pattern = r"[a-h][1-8][a-h][1-8]"
        return re.match(pattern, move)

    @classmethod
    def vertical_difference(cls, source, dest):
        return int(dest[1]) - int(source[1])
    
    @classmethod
    def horizontal_difference(cls, source, dest):
        return ord(dest[0]) - ord(source[0])
    
    @classmethod
    def check_castle(cls, move, board, white_to_play):
        source = cls.get_source_pos(move)
        dest = cls.get_dest_pos(move)
        source_piece = board.get(source)
        
        if source_piece is not None and source_piece.type_enum == 6:
            if white_to_play:
                if source == 'e1' and dest == 'g1' and source_piece._is_white and source_piece.has_moved is False:
                    rook_piece = board.get('h1')
                    if rook_piece is not None and rook_piece.type_enum == 4 and rook_piece.has_moved is False:
                        if board.get('f1') is None and board.get('g1') is None:
                            return True
                elif source == 'e1' and dest == 'c1' and source_piece._is_white and source_piece.has_moved is False:
                    rook_piece = board.get('a1')
                    if rook_piece is not None and rook_piece.type_enum == 4 and rook_piece.has_moved is False:
                        if board.get('b1') is None and board.get('c1') is None and board.get('d1') is None:
                            return True
            else:
                if source == 'e8' and dest == 'g8' and source_piece._is_white is False and source_piece.has_moved is False:
                    if board.get('f8') is None and board.get('g8') is None:
                        return True
                elif source == 'e8' and dest == 'c8' and source_piece._is_white is False and source_piece.has_moved is False:
                    if board.get('b8') is None and board.get('c8') is None and board.get('d8') is None:
                        return True
        return False



    # @classmethod
    # def check_stalemate(cls, move, board, white_to_play):
    #     pass

    # @classmethod
    # def check_promotion(cls, move, board, white_to_play):
    #     pass
    # @classmethod
    # def check_draw(cls, move, board, white_to_play):
    #     pass

    # @classmethod
    # def check_insufficient_material(cls, move, board, white_to_play):
    #     pass
