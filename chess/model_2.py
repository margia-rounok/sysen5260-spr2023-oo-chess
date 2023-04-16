"""Chess Game model."""
from typing import Optional

class Board:
    def __init__(self):
        self._squares = dict()

    def get(self, location:str) -> Optional['Piece']:
        return self._squares.get(location, None)

    def set(self, location:str, piece: 'Piece'):
        self._squares[location] = piece

    def move(self, source:str, dest:str):
        piece = self.get(source)
        self.set(source, None)
        self.set(dest, piece)

    def king_location(self, is_white: bool) -> str:
        for location, piece in self._squares.items():
            if piece is not None and piece.type_enum == 6 and piece._is_white == is_white:
                return location
        return ""
    
    def get_piece_locations(self, is_white: bool) -> list[str]:
        locations=[]
        for location, piece in self._squares.items():
            if piece is not None and piece._is_white == is_white:
                locations.append(location)
        return locations

class Piece:
    """Abstract base class for chess pieces."""
    def __init__(self, is_white: bool) -> None:
        self._is_white = is_white
        self.has_moved = False

    def __hash__(self):
        return hash((type(self), self._is_white))

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)
    
    @property
    def type_enum(self) -> int:
        return 0
    
    def valid_moves(self, position:str) -> list:
        return []
    
    def get_path(self, source: str, dest: str) -> list[str]:
        path = []
        return path
    
    def discard_invalid_moves(self, positions: list[str]) -> list[str]:
        ## Discard moves (positions) that are off the board
        valid_moves=[]
        for position in positions:
            if position[0] in 'abcdefgh' and position[1] in '12345678':
                valid_moves.append(position)
        return valid_moves
        
    def remove_source_and_dest_from_path(self, path: list[str], source: str, dest: str) -> list[str]:
        if(source in path):
            path.remove(source)
        if(dest in path):
            path.remove(dest)
        return path

class Pawn(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)
        self.just_moved_two_squares = False

    @property
    def type_enum(self) -> int:
        return 1
    
    def valid_moves(self, current_position: str) -> list[str]:
        """Return a list of valid moves for this piece."""
        moves=[]
        if self._is_white:
            moves.append(f'{current_position[0]}{int(current_position[1])+1}')
            if self.has_moved is False:
                moves.append(f'{current_position[0]}{int(current_position[1])+2}')
        else:
            moves.append(f'{current_position[0]}{int(current_position[1])-1}')
            if self.has_moved is False:
                moves.append(f'{current_position[0]}{int(current_position[1])-2}')
        valid_moves = self.discard_invalid_moves(moves)
        return valid_moves

    def get_path(self, current_position: str, destination: str) -> list[str]:
        """Return a list of squares traversed by this piece from current_position to destination."""
        
        path=[]
        if self._is_white:
            if int(current_position[1])+1 == int(destination[1]):
                path.append(f'{current_position[0]}{int(current_position[1])+1}')
            elif int(current_position[1])+2 == int(destination[1]):
                path.append(f'{current_position[0]}{int(current_position[1])+1}')
                path.append(f'{current_position[0]}{int(current_position[1])+2}')
        else:
            if int(current_position[1])-1 == int(destination[1]):
                path.append(f'{current_position[0]}{int(current_position[1])-1}')
            elif int(current_position[1])-2 == int(destination[1]):
                path.append(f'{current_position[0]}{int(current_position[1])-1}')
                path.append(f'{current_position[0]}{int(current_position[1])-2}')
        path = self.remove_source_and_dest_from_path(path, current_position, destination)
        return path
    
class Bishop(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    @property
    def type_enum(self) -> int:
        return 2

    def valid_moves(self, current_position: str) -> list[str]:
        """Return a list of valid moves for this piece."""
        moves=[]

        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])+i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])-i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])+i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])-i}')
        valid_moves = self.discard_invalid_moves(moves)
        return valid_moves
    
    def get_path(self, current_position: str, destination: str) -> list[str]:
        """Return a list of squares traversed by this piece from current_position to destination."""
        path=[]
        if ord(current_position[0]) < ord(destination[0]) and int(current_position[1]) < int(destination[1]):
            for i in range(1, int(destination[1])-int(current_position[1])+1):
                path.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])+i}')
        elif ord(current_position[0]) < ord(destination[0]) and int(current_position[1]) > int(destination[1]):
            for i in range(1, int(current_position[1])-int(destination[1])+1):
                path.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])-i}')
        elif ord(current_position[0]) > ord(destination[0]) and int(current_position[1]) < int(destination[1]):
            for i in range(1, int(destination[1])-int(current_position[1])+1):
                path.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])+i}')
        elif ord(current_position[0]) > ord(destination[0]) and int(current_position[1]) > int(destination[1]):
            for i in range(1, int(current_position[1])-int(destination[1])+1):
                path.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])-i}')
        
        path = self.remove_source_and_dest_from_path(path, current_position, destination)
        return path

class Knight(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)
    
    @property
    def type_enum(self) -> int:
        return 3

    def valid_moves(self, current_position: str) -> list[str]:
        """Return a list of valid moves for this piece."""
        moves=[]
        moves.append(f'{chr(ord(current_position[0])+1)}{int(current_position[1])+2}')
        moves.append(f'{chr(ord(current_position[0])+1)}{int(current_position[1])-2}')
        moves.append(f'{chr(ord(current_position[0])-1)}{int(current_position[1])+2}')
        moves.append(f'{chr(ord(current_position[0])-1)}{int(current_position[1])-2}')
        moves.append(f'{chr(ord(current_position[0])+2)}{int(current_position[1])+1}')
        moves.append(f'{chr(ord(current_position[0])+2)}{int(current_position[1])-1}')
        moves.append(f'{chr(ord(current_position[0])-2)}{int(current_position[1])+1}')
        moves.append(f'{chr(ord(current_position[0])-2)}{int(current_position[1])-1}')
        valid_moves = self.discard_invalid_moves(moves)
        return valid_moves
    def get_path(self, current_position: str, destination: str) -> list[str]:
        """Return a list of squares traversed by this piece from current_position to destination."""
        path=[]
        return path

class Rook(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    @property
    def type_enum(self) -> int:
        return 4
    
    def valid_moves(self, current_position: str) -> list[str]:
        """Return a list of valid moves for this piece."""
        moves=[]
        for i in range(1,9):
            moves.append(f'{current_position[0]}{i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])+i)}{current_position[1]}')
        valid_moves = self.discard_invalid_moves(moves)
        return valid_moves
    
    def get_path(self, current_position: str, destination: str) -> list[str]:
        """Return a list of squares traversed by this piece from current_position to destination."""
        path=[]
        if current_position[0] == destination[0]:
            if int(current_position[1]) < int(destination[1]):
                for i in range(int(current_position[1]), int(destination[1])+1):
                    path.append(f'{current_position[0]}{i}')
            else:
                for i in range(int(current_position[1]), int(destination[1])-1, -1):
                    path.append(f'{current_position[0]}{i}')
        elif current_position[1] == destination[1]:
            if ord(current_position[0]) < ord(destination[0]):
                for i in range(ord(current_position[0]), ord(destination[0])+1):
                    path.append(f'{chr(i)}{current_position[1]}')
            else:
                for i in range(ord(current_position[0]), ord(destination[0])-1, -1):
                    path.append(f'{chr(i)}{current_position[1]}')

        path = self.remove_source_and_dest_from_path(path, current_position, destination)
        return path

class Queen(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    @property
    def type_enum(self) -> int:
        return 5

    def valid_moves(self, current_position: str) -> list[str]:

        moves=[]
        for i in range(1,9):
            moves.append(f'{current_position[0]}{i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])+i)}{current_position[1]}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])+i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])-i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])+i}')
        for i in range(1,9):
            moves.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])-i}')
        valid_moves = self.discard_invalid_moves(moves)
        return valid_moves
    
    def get_path(self, current_position: str, destination: str) -> list[str]:
        """Return a list of squares traversed by this piece from current_position to destination."""
        path=[]
        if current_position[0] == destination[0]:
            if int(current_position[1]) < int(destination[1]):
                for i in range(1, int(destination[1])-int(current_position[1])+1):
                    path.append(f'{current_position[0]}{int(current_position[1])+i}')
            else:
                for i in range(1, int(current_position[1])-int(destination[1])+1):
                    path.append(f'{current_position[0]}{int(current_position[1])-i}')
        elif int(current_position[1]) == int(destination[1]):
            if ord(current_position[0]) < ord(destination[0]):
                for i in range(1, ord(destination[0])-ord(current_position[0])+1):
                    path.append(f'{chr(ord(current_position[0])+i)}{current_position[1]}')
            else:
                for i in range(1, ord(current_position[0])-ord(destination[0])+1):
                    path.append(f'{chr(ord(current_position[0])-i)}{current_position[1]}')
        elif ord(current_position[0]) < ord(destination[0]) and int(current_position[1]) < int(destination[1]):
            for i in range(1, int(destination[1])-int(current_position[1])+1):
                path.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])+i}')
        elif ord(current_position[0]) < ord(destination[0]) and int(current_position[1]) > int(destination[1]):
            for i in range(1, int(current_position[1])-int(destination[1])+1):
                path.append(f'{chr(ord(current_position[0])+i)}{int(current_position[1])-i}')
        elif ord(current_position[0]) > ord(destination[0]) and int(current_position[1]) < int(destination[1]):
            for i in range(1, int(destination[1])-int(current_position[1])+1):
                path.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])+i}')
        elif ord(current_position[0]) > ord(destination[0]) and int(current_position[1]) > int(destination[1]):
            for i in range(1, int(current_position[1])-int(destination[1])+1):
                path.append(f'{chr(ord(current_position[0])-i)}{int(current_position[1])-i}')
        
        path = self.remove_source_and_dest_from_path(path, current_position, destination)
        return path

class King(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)
        self.is_in_check=False

    @property
    def type_enum(self) -> int:
        return 6

    def valid_moves(self, current_position: str) -> list[str]:
        """Return a list of valid moves for this piece."""
        moves=[]
        moves.append(f'{current_position[0]}{int(current_position[1])+1}')
        moves.append(f'{current_position[0]}{int(current_position[1])-1}')
        moves.append(f'{chr(ord(current_position[0])+1)}{current_position[1]}')
        moves.append(f'{chr(ord(current_position[0])-1)}{current_position[1]}')
        moves.append(f'{chr(ord(current_position[0])+1)}{int(current_position[1])+1}')
        moves.append(f'{chr(ord(current_position[0])+1)}{int(current_position[1])-1}')
        moves.append(f'{chr(ord(current_position[0])-1)}{int(current_position[1])+1}')
        moves.append(f'{chr(ord(current_position[0])-1)}{int(current_position[1])-1}')
        valid_moves = self.discard_invalid_moves(moves)
        return valid_moves
    def get_path(self, current_position: str, destination: str) -> list[str]:
        """Return a list of squares traversed by this piece from current_position to destination."""
        path=[]
        return path

class move_node:
    def __init__(self, move=None):
        self.move = move
        self.next = None

class piece_node:
    def __init__(self, piece=None):
        self.piece = piece
        self.next = None

class Game:
    def __init__(self):
        self.board = Board()
        self.white_to_play = True
        self.game_over = False
        self.move_history = []
        self.head= move_node()
        self.piece_head= piece_node()

    def get_board(self) -> Board:
        return self.board
    def get_white_to_play(self) -> bool:
        return self.white_to_play
    def get_move_history(self) -> list[tuple[str, str]]:
        return self.move_history
    def get_dest_pos(self, move: str) -> str:
        return move[2:]
    def get_dest_piece(self, dest: str):
        return self.board.get(dest)
    def get_source_pos(self, move: str) -> str:
        return move[0:2]
    def get_source_piece(self, source: str):
        return self.board.get(source)
    def get_source_type(self, move:str):
        source_pos = self.get_source_pos(move)
        # print(source_pos)
        source_piece = self.get_source_piece(source_pos)
        # print(source_piece.type_enum())
        return source_piece.type_enum()

    def do_backup(self, move): 
        self.pop_list()
        move_list = self.display()
        piece_list = self.display_piece_list()
        piece_list_length = len(piece_list)
        move_list_length = len(move_list)
        if move_list_length == 0:
            print("Must Make a move first!")
        else:
            self.white_to_play = not self.white_to_play
            prev_move = move_list[move_list_length-1]
            prev_piece = piece_list[piece_list_length-1]
            dest = self.get_source_pos(prev_move)
            source = self.get_dest_pos(prev_move)
            # Need to check if piece was captured, if true respawn piece
            dest_piece = self.get_dest_piece(source)
            self.board.set(source, prev_piece)
            self.board.set(dest, dest_piece)
            self.pop_list()
        #print("this will backup move")

    def move_list_append(self, move):
        new_move_node = move_node(move)
        dest = self.get_dest_pos(move)
        new_piece_node = piece_node(self.get_dest_piece(dest))
        cur_move = self.head
        cur_piece = self.piece_head
        while cur_move.next != None:
            cur_move = cur_move.next
            cur_piece = cur_piece.next
        cur_move.next = new_move_node
        cur_piece.next = new_piece_node

    def pop_list(self):
        cur_move_node = self.head
        cur_piece_node = self.piece_head
        while cur_move_node.next:
            if cur_move_node.next.next == None:
                cur_move_node.next = None
                cur_piece_node.next = None
            else:
                cur_move_node = cur_move_node.next
                cur_piece_node = cur_piece_node.next
        return cur_move_node, cur_piece_node
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.move)
        return elems
    
    def display_piece_list(self):
        elems = []
        cur_node = self.piece_head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.piece)
        print("piece elems: ", elems)
        return elems
    
    def move_piece(self, source: str, dest: str):
        """Move piece from source to destination.
        Assumes move is valid.
        """
        piece = self.board.get(source)
        # Check if move is a castle move
        if self.is_castle_move(source, dest):
            self.castle(source, dest)

        # Check if move is an en passant move
        elif self.is_en_passant_move(source, dest):
            self.capture_en_passant(source, dest)

        # Check if move is a pawn promotion move
        elif self.is_promotion_move(source, dest):
            self.promote_pawn(source, dest)

        # Make normal move    
        else:
            self.make_normal_move(source, dest)

        
        self.move_history.append((source, dest))
        self.reset_pawn_just_moved_two()
        if(piece.type_enum==1 and abs(int(dest[1])-int(source[1]))==2):
            piece.just_moved_two_squares=True


    def make_normal_move(self, source: str, dest: str):
        """Make a normal move."""
        piece = self.board.get(source)
        self.board.set(dest, piece)
        self.board.set(source, None)
        piece.has_moved = True
    
    def promote_pawn(self, source: str, dest: str):
        """Make a promotion move."""
        piece = self.board.get(source)
        self.board.set(dest, piece)
        self.board.set(source, None)
        piece.has_moved = True
        if(piece.type_enum == 1 and dest[1] == '8'):
            self.board.set(dest, Queen(is_white=piece._is_white))
        elif(piece.type_enum == 1 and dest[1] == '1'):
            self.board.set(dest, Queen(is_white=piece._is_white))
        else:
            pass
    
    def is_promotion_move(self, source: str, dest: str):
        """Check if a move is a promotion move."""
        piece = self.board.get(source)
        if piece is not None and piece.type_enum == 1 and dest[1] in ('1', '8'):
            return True
        return False
    
    def is_en_passant_move(self, source: str, dest: str):
        """Check if a move is an en passant move."""
        piece = self.board.get(source)
        if piece is not None and piece.type_enum == 1:
            if piece._is_white and dest[1] == '6':
                if self.board.get(dest) is None:
                    if self.move_history[-1][1] == dest:
                        if self.move_history[-1][0][1] == dest[1]:
                            return True
            elif not piece._is_white and dest[1] == '3':
                if self.board.get(dest) is None:
                    if self.move_history[-1][1] == dest:
                        if self.move_history[-1][0][1] == dest[1]:
                            return True
        return False
    
    def capture_en_passant(self, source: str, dest: str):
        """Make an en passant move."""
        piece = self.board.get(source)
        self.board.set(dest, piece)
        self.board.set(source, None)
        self.board.set(dest[0] + source[1], None)
        piece.has_moved = True


    def reset_pawn_just_moved_two(self):
        for col in 'abcdefgh':
            for row in '12345678':
                piece = self.board.get(f'{col}{row}')
                if piece is not None and piece.type_enum == 1:
                    piece.just_moved_two_squares = False

    def is_castle_move(self, source, dest):
        """Check if a move is a castle move."""
        if source == 'e1' and dest in ('c1', 'g1'):
            return True
        if source == 'e8' and dest in ('c8', 'g8'):
            return True
        return False

    def castle(self, source,dest):
        """Make a castle move."""
        if source == 'e1' and dest == 'c1':
            self.board.set('a1', None)
            self.board.set('d1', Rook(is_white=True))
            self.board.set('e1', None)
            self.board.set('c1', King(is_white=True))
        elif source == 'e1' and dest == 'g1':
            self.board.set('h1', None)
            self.board.set('f1', Rook(is_white=True))
            self.board.set('e1', None)
            self.board.set('g1', King(is_white=True))
        elif source == 'e8' and dest == 'c8':
            self.board.set('a8', None)
            self.board.set('d8', Rook(is_white=False))
            self.board.set('e8', None)
            self.board.set('c8', King(is_white=False))
        elif source == 'e8' and dest == 'g8':
            self.board.set('h8', None)
            self.board.set('f8', Rook(is_white=False))
            self.board.set('e8', None)
            self.board.set('g8', King(is_white=False))

    def accept_move(self, move, captured_piece_location):
        # TODO: Implement updating the board with the give move
        source = move[0:2]
        dest = move[2:]
        if(captured_piece_location is not None):
            self.board.set(captured_piece_location, None)
        self.move_piece(source, dest)
        self.white_to_play = not self.white_to_play
        self.move_history.append(move)

    def set_up_pieces(self):
        """Place pieces on the board as per the initial setup."""
        for col in 'abcdefgh':
            self.board.set(f'{col}2', Pawn(is_white=True))
            self.board.set(f'{col}7', Pawn(is_white=False))
        # setting up bishops
        self.board.set('c1', Bishop(is_white=True))
        self.board.set('f1', Bishop(is_white=True))
        self.board.set('c8', Bishop(is_white=False))
        self.board.set('f8', Bishop(is_white=False))

        #setting up rooks
        self.board.set('a1', Rook(is_white=True))
        self.board.set('h1', Rook(is_white=True))
        self.board.set('a8', Rook(is_white=False))
        self.board.set('h8', Rook(is_white=False))

        #setting up queen
        self.board.set('d1', Queen(is_white=True))
        self.board.set('d8', Queen(is_white=False))

        # setting up knight
        self.board.set('b1', Knight(is_white=True))
        self.board.set('g1', Knight(is_white=True))
        self.board.set('b8', Knight(is_white=False))
        self.board.set('g8', Knight(is_white=False))

        #setting up king
        self.board.set('e1', King(is_white=True))
        self.board.set('e8', King(is_white=False))
