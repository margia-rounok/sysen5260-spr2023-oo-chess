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
        combined_hash_str = str(type(self)) + str(self._is_white)
        return hash(combined_hash_str)

    def __eq__(self, other: "Piece") -> bool:
        return hash(self) == hash(other)
    
    def type_enum(self) -> int:
        return 0
    
    def valid_moves(self, position:str) -> list:
        return []
    
    def check_path(self, source: str, dest: str) -> bool:
        return False


class Pawn(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    # def __hash__(self):
    #     super().__hash__()

    # def __eq__(self, other):
    #     super().__eq__(other)
    
    def type_enum(self) -> int:
        return 1
    
    def valid_moves(self, position:str) -> list:
        is_white = self._is_white
        # print("valid moves")
        # print(is_white)
        x, y = position[0], int(position[1])
        possible_moves = []

        # Determine the direction the pawn moves based on color
        direction = 1 if is_white else -1

        # Move one square ahead
        if (1 <= y + direction <= 8):
            possible_moves.append(x + str(y + direction))

        # Move two squares ahead if pawn is at starting position
        if ((y == 2 and is_white) or (y == 7 and not is_white)):
            if (1 <= y + 2 * direction <= 8):
                possible_moves.append(x + str(y + 2 * direction))

        # En passant
        if ((y == 5 and is_white) or (y == 4 and not is_white)):
            # Check if there is a neighboring pawn that moved two squares ahead in the previous move
            left_neighbor = chr(ord(x) - 1) + str(y)
            right_neighbor = chr(ord(x) + 1) + str(y)
        print(possible_moves)
        return possible_moves

    
    def get_path(self, source: str, dest: str) -> list:
        empty_positions = []
        x1, y1 = source[0], int(source[1])
        x2, y2 = dest[0], int(dest[1])
        color = self._is_white
        # Check for valid pawn move
        if (x1 == x2) and (y2 == y1+1) and (color):  # White pawn moving one square ahead
            empty_positions.append(x1 + str(y1+1))
        elif (x1 == x2) and (y2 == y1+2) and (color) and (y1 == 2):  # White pawn moving two squares ahead
            empty_positions.append(x1 + str(y1+1))
            empty_positions.append(x1 + str(y1+2))
        elif (x1 != x2) and (y2 == y1+1) and (color):  # White pawn capturing an opponent's pawn
            empty_positions.append(x2 + str(y2))
        elif (x1 != x2) and (y2 == y1+1) and (color) and (y1 == 5):  # White pawn making an en passant capture
            empty_positions.append(x2 + str(y2))
        
        elif (x1 == x2) and (y2 == y1-1) and not color:  # Black pawn moving one square ahead
            empty_positions.append(x1 + str(y1-1))
        elif (x1 == x2) and (y2 == y1-2) and not color and (y1 == 7):  # Black pawn moving two squares ahead
            empty_positions.append(x1 + str(y1-1))
            empty_positions.append(x1 + str(y1-2))
        elif (x1 != x2) and (y2 == y1-1) and not color:  # Black pawn capturing an opponent's pawn
            empty_positions.append(x2 + str(y2))
        elif (x1 != x2) and (y2 == y1-1) and not color and (y1 == 4):  # Black pawn making an en passant capture
            empty_positions.append(x2 + str(y2))
        
        else:
            return empty_positions  # Invalid move, return empty list
        
        return empty_positions

    
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
    
    def get_path(self, source: str, dest: str) -> list:
        src_x, src_y = ord(source[0]) - 96, int(source[1])
        dest_x, dest_y = ord(dest[0]) - 96, int(dest[1])

        # check if the move is valid
        if abs(src_x - dest_x) != abs(src_y - dest_y):
            return []

        # get the direction of the move
        x_dir = 1 if src_x < dest_x else -1
        y_dir = 1 if src_y < dest_y else -1

        empty_positions = []
        x, y = src_x + x_dir, src_y + y_dir
        while x != dest_x and y != dest_y:
            empty_positions.append(chr(x + 96) + str(y))
            x += x_dir
            y += y_dir

        return empty_positions
    
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
    
    def get_path(self, source: str, dest: str) -> list:
        src_x, src_y = ord(source[0]), int(source[1])
        dest_x, dest_y = ord(dest[0]), int(dest[1])

        positions = []
    
        # Check if rook is moving along the x-axis
        if src_x != dest_x and src_y == dest_y:
            if dest_x > src_x:
                positions = [(chr(i) + str(src_y)) for i in range(src_x+1, dest_x)]
            else:
                positions = [(chr(i) + str(src_y)) for i in range(dest_x+1, src_x)]
        
        # Check if rook is moving along the y-axis
        elif src_x == dest_x and src_y != dest_y:
            if dest_y > src_y:
                positions = [(source[0] + str(j)) for j in range(src_y+1, dest_y)]
            else:
                positions = [(source[0] + str(j)) for j in range(dest_y+1, src_y)]
        
        else:
            # Invalid move for a rook
            return []
        
        return positions

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
    
    def get_path(self, source: str, dest: str) -> list:
        start_x, start_y = source[0], int(source[1])
        dest_x, dest_y = dest[0], int(dest[1])

        # Check if the move is valid
        if start_x == dest_x or start_y == dest_y or abs(ord(start_x) - ord(dest_x)) == abs(start_y - dest_y):
            # Generate a list of all positions that need to be empty
            empty_positions = []
            if start_x == dest_x:
                # The move is vertical, so iterate over the y-axis
                for i in range(min(start_y, dest_y) + 1, max(start_y, dest_y)):
                    empty_positions.append(start_x + str(i))
            elif start_y == dest_y:
                # The move is horizontal, so iterate over the x-axis
                for i in range(ord(min(start_x, dest_x)) + 1, ord(max(start_x, dest_x))):
                    empty_positions.append(chr(i) + str(start_y))
            else:
                # The move is diagonal, so iterate over the diagonal
                x_direction = -1 if start_x > dest_x else 1
                y_direction = -1 if start_y > dest_y else 1
                x, y = ord(start_x) + x_direction, start_y + y_direction
                while x != ord(dest_x) and y != dest_y:
                    empty_positions.append(chr(x) + str(y))
                    x += x_direction
                    y += y_direction
            return empty_positions
        else:
            # The move is not valid, so return an empty list
            return []


class Knight(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    def __hash__(self):
        super().__hash__()

    def __eq__(self, other):
        super().__eq__(other)

    def type_enum(self) -> int:
        return 5

    def valid_moves(self, position:str) -> list:
        x, y = position[0], int(position[1])
        moves = []
        for dx, dy in ((-2, -1), (-1, -2), (1, -2), (2, -1),
                    (-2, 1), (-1, 2), (1, 2), (2, 1)):
            new_x, new_y = ord(x) + dx, y + dy
            if 97 <= new_x <= 104 and 1 <= new_y <= 8:
                moves.append(chr(new_x) + str(new_y))
        return moves
    
    def get_path(self, source: str, dest: str) -> list:
        return [] #knight can jump over pieces 

class King(Piece):
    def __init__(self, is_white: bool) -> None:
        super().__init__(is_white)

    def __hash__(self):
        super().__hash__()

    def __eq__(self, other):
        super().__eq__(other)

    def type_enum(self) -> int:
        return 6

    def valid_moves(self, position:str) -> list:
        x, y = position[0], int(position[1])
        moves = []

        # check all possible moves
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue  # king can't stay in the same position
                new_x, new_y = ord(x) + i, y + j
                if 97 <= new_x <= 104 and 1 <= new_y <= 8:
                    moves.append(chr(new_x) + str(new_y))

        return moves
        
    def get_path(self, source: str, dest: str) -> list:
        moves = []
        return moves.append(dest) #king moves one spot 

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
        # print(source_pos)
        source_piece = self.get_source_piece(source_pos)
        # print(source_piece.type_enum())
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

    # def check_piece_override_pawn(self,move):
    #     #true if override, false ow
    #     dest = self.get_dest_pos(move)
    #     dest_piece = self.get_dest_piece(dest)
    #     return dest_piece is None or \
    #     dest_piece._is_white == self.white_to_play 

    def check_no_piece_override(self,move):
        # true if no override
        dest = self.get_dest_pos(move)
        dest_piece = self.get_dest_piece(dest)
        print(dest_piece is None)
        print(self.white_to_play)
        return dest_piece is None or \
        dest_piece._is_white != self.white_to_play 

    def check_no_path_override(self, pos_lst):
        full = False
        for pos in pos_lst:
            pos_piece = self.board.get(pos)
            if self.board.get(pos) is not None and \
                self.white_to_play == pos_piece._is_white:
                    full = True
                    break
        return full

    def check_piece(self,move, id):
        print("in check_piece")
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() == id and \
            dest in source_piece.valid_moves(source): #get correct moves per id/enum/type
                path = source_piece.get_path(source, dest) #get the necessary empty path for everything but queen
                if id in [1,2,3,4] and not self.check_no_path_override(path): #then check if path is unobstructed
                    print("in check for path is unobstructed")
                    self.accept_move(move) #finally move
                    return True
                if id == 5 or id == 6:
                    self.accept_move(move) #knight can move
                    return True
        return False

    def accept_move(self, move):
        # TODO: Implement updating the board with the give move
        self.white_to_play = not self.white_to_play
        print("accept_move")
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        #dest_piece = self.get_dest_piece(dest) #only important if dest_piece is king and captured
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() in [1,2,3,4,6]:
            self.board.set(source, None)
            self.board.set(dest, source_piece)
        elif source_piece.type_enum() in [5,6]: #knight
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

        # setting up knight
        self.board.set('b1', Knight(is_white=True))
        self.board.set('g1', Knight(is_white=True))
        self.board.set('b8', Knight(is_white=False))
        self.board.set('g8', Knight(is_white=False))

        #setting up king
        self.board.set('e1', King(is_white=True))
        self.board.set('e8', King(is_white=False))



