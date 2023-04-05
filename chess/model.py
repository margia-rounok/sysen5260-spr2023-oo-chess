"""Chess Game model."""
from typing import Optional

import re

class Board:
    def __init__(self):
        self._squares = dict()

    def get(self, location:str) -> Optional['Piece']:
        return self._squares.get(location, None)

    def set(self, location:str, piece: Optional['Piece']):
        self._squares[location] = piece

class Piece:
    """Abstract base class for chess pieces."""
    def __init__(self, is_white: bool) -> None:
        self._is_white = is_white

    def __hash__(self):
        return hash((type(self), self._is_white))

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)
    
    def type_enum(self) -> int:
        return 0
    
    def valid_moves(self, moves:str) -> list:
        return []


class Pawn(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    def __hash__(self):
        super().__hash__()

    def __eq__(self, other):
        super().__eq__(other)
    
    def type_enum(self) -> int:
        return 1
    
    def valid_moves(self, moves:str) -> list:
        return ['TODO']

class Bischop(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    def __hash__(self):
        super().__hash__()

    def __eq__(self, other):
        super().__eq__(other)

    def type_enum(self) -> int:
        return 2

    def valid_moves(self, position:str) -> list:
        x, y = position[0], int(position[1])
        moves = []

        # diagonal up-right
        while ord(x) < ord('h') and y < 8:
            x, y = chr(ord(x) + 1), y + 1
            moves.append(x + str(y))

        # diagonal up-left
        x, y = position[0], int(position[1])
        while ord(x) > ord('a') and y < 8:
            x, y = chr(ord(x) - 1), y + 1
            moves.append(x + str(y))

        # diagonal down-right
        x, y = position[0], int(position[1])
        while ord(x) < ord('h') and y > 1:
            x, y = chr(ord(x) + 1), y - 1
            moves.append(x + str(y))

        # diagonal down-left
        x, y = position[0], int(position[1])
        while ord(x) > ord('a') and y > 1:
            x, y = chr(ord(x) - 1), y - 1
            moves.append(x + str(y))

        return moves

class Rook(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    def __hash__(self):
        super().__hash__()

    def __eq__(self, other):
        super().__eq__(other)

    def type_enum(self) -> int:
        return 3

    def valid_moves(self, position:str) -> list:
        x, y = position[0], int(position[1])
        moves = []
        
        # Check all possible x-axis moves
        for i in range(ord('a'), ord('i')):
            if chr(i) != x:
                moves.append(chr(i) + str(y))
        
        # Check all possible y-axis moves
        for j in range(1, 9):
            if j != y:
                moves.append(x + str(j))
        
        return moves

class Queen(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    def __hash__(self):
        super().__hash__()

    def __eq__(self, other):
        super().__eq__(other)

    def type_enum(self) -> int:
        return 4

    def valid_moves(self, position:str) -> list:
        x, y = position[0], int(position[1])

        # Generate all valid positions on the x-axis
        x_positions = [chr(i) + str(y) for i in range(ord('a'), ord('i'))]

        # Generate all valid positions on the y-axis
        y_positions = [x + str(i) for i in range(1, 9)]

        # Generate all valid positions on the diagonal
        diagonal_positions = []
        for i in range(1, 9):
            if ord(x) + i <= ord('h') and y + i <= 8:
                diagonal_positions.append(chr(ord(x) + i) + str(y + i))
            if ord(x) - i >= ord('a') and y - i >= 1:
                diagonal_positions.append(chr(ord(x) - i) + str(y - i))
            if ord(x) + i <= ord('h') and y - i >= 1:
                diagonal_positions.append(chr(ord(x) + i) + str(y - i))
            if ord(x) - i >= ord('a') and y + i <= 8:
                diagonal_positions.append(chr(ord(x) - i) + str(y + i))

        # Combine all valid positions and return the result
        return list(set(x_positions + y_positions + diagonal_positions))


class Game:
    def __init__(self):
        self.board = Board()
        self.white_to_play = True
        self.game_over = False

    def check_input(self, move):
        pattern = r"[a-h][1-8][a-h][1-8]"
        return re.match(pattern, move)
    
    def get_source_pos(self, move: str) -> str:
        return move[0:2]

    def get_source_piece(self, source: str):
        return self.board.get(source)
    
    def get_source_type(self, move:str):
        source_pos = self.get_source_pos(move)
        print(source_pos)
        source_piece = self.get_source_piece(source_pos)
        print(source_piece.type_enum())
        return source_piece.type_enum()
    
    def get_dest_pos(self, move: str) -> str:
        return move[2:]

    def get_dest_piece(self, dest: str):
        return self.board.get(dest)

    def check_moved_op(self, move):
        source = self.get_source_pos(move)
        source_piece = self.get_source_piece(source)
        return source_piece is None or \
        source_piece._is_white == self.white_to_play #valid iff they differ, did not move op
    
    # def check_move_exist(self, move):
    #     source = move[0:2]
    #     source_piece = self.board.get(source)
    #     return source_piece is None

    def check_no_piece_override(self,move):
        dest = self.get_dest_pos(move)
        dest_piece = self.get_dest_piece(dest)
        return dest_piece is None or \
        dest_piece._is_white == self.white_to_play 

    def move_bischop(self,move):
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() == 2 and \
            dest in source_piece.valid_moves(source): #check that id is bischop
                self.accept_move(move)
                return True
        return False

    def move_rook(self,move):
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() == 3 and \
            dest in source_piece.valid_moves(source): #check that id is rook
                self.accept_move(move)
                return True
        return False

    def move_queen(self,move):
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() == 4 and \
            dest in source_piece.valid_moves(source): #check that id is rook
                self.accept_move(move)
                return True
        return False

    def accept_move(self, move):
        # TODO: Implement updating the board with the give move
        self.white_to_play = not self.white_to_play
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        #dest_piece = self.get_dest_piece(dest) #only important if dest_piece is king and captured
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() == 2:
            self.board.set(source, None)
            self.board.set(dest, source_piece)
        elif source_piece.type_enum() == 3:
            self.board.set(source, None)
            self.board.set(dest, source_piece)
        elif source_piece.type_enum() == 4:
            self.board.set(source, None)
            self.board.set(dest, source_piece)

        
    def set_up_pieces(self):
        """Place pieces on the board as per the initial setup."""
        # empty is white and filled is black
        for col in 'abcdefgh':
            #set up pawns
            self.board.set(f'{col}2', Pawn(is_white=True))
            self.board.set(f'{col}7', Pawn(is_white=False))
        
        # setting up bischops
        self.board.set('c1', Bischop(is_white=True))
        self.board.set('f1', Bischop(is_white=True))
        self.board.set('c8', Bischop(is_white=False))
        self.board.set('f8', Bischop(is_white=False))

        #setting up rooks
        self.board.set('a1', Rook(is_white=True))
        self.board.set('h1', Rook(is_white=True))
        self.board.set('a8', Rook(is_white=False))
        self.board.set('h8', Rook(is_white=False))

        #setting up queen
        self.board.set('d1', Queen(is_white=True))
        self.board.set('d8', Queen(is_white=False))

