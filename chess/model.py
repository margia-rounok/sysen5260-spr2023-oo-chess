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
    
    def type_enum(self) -> int:
        return 1
    
    def valid_moves(self, position:str) -> list:
        is_white = self._is_white
        # print("valid moves")
        # print(is_white)
        x, y = position[0], int(position[1])
        print(x, y)
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
        if ((y == 4 and is_white) or (y == 5 and not is_white)):
            # Check if there is a neighboring pawn that moved two squares ahead in the previous move
            print("ords: ", ord(x))
            print('y', y)
            left_neighbor = chr(ord(x)+1) + str(y)
            right_neighbor = chr(ord(x)+1) + str(y)
            print(left_neighbor, right_neighbor)
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
        self.head = move_node()
        self.piece_head = piece_node()
        # self.king_pos = "e1" if self.white_to_play else "e8"

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

    # return piece or space that was captured by a move
    # def piece_list_append(self, move):
    #     dest = self.get_dest_pos(move)
    #     print("new piece node 1: ", self.get_dest_piece(dest))
    #     print("dest: ", dest)
    #     new_piece_node = piece_node(self.get_dest_piece(dest))
    #     print("new piece node: ", new_piece_node)
    #     cur = self.piece_head
    #     while cur.next != None:
    #         cur = cur.next
    #     cur.next = new_piece_node
    
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
        source = self.get_source_pos(move)
        dest = self.get_dest_pos(move)
        source_piece = self.get_source_piece(source)
        if source_piece.type_enum() == id and \
            dest in source_piece.valid_moves(source): #get correct moves per id/enum/type
                path = source_piece.get_path(source, dest) #get the necessary empty path for everything but knight
                if id in [1,2,3,4] and not self.check_no_path_override(path): #then check if path is unobstructed
                    self.accept_move(move) #finally move
                    return True
                if id == 5 or id == 6:
                    self.accept_move(move) #knight can move
                    # if(id == 6): #king
                    #     self.king_pos == move
                    return True
        return False

    def accept_move(self, move):
        # print("in accept_move")
        self.white_to_play = not self.white_to_play
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

    def get_piece(self, op_color): 
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        nums = [1,2,3,4,5,6,7,8]
        location = []
        for x in letters:
            for y in nums:
                pos = x + str(y)
                curr_piece = self.board.get(pos)
                if curr_piece is not None:
                    if(curr_piece._is_white == op_color):
                        location.append(pos)
        # print(location)
        return location
    
    def check_one_hop_king(self, enemy_type, enemy_path):
        # print("check_one_hop_king")
        # print(enemy_type)
        # print(enemy_path)
        if enemy_type in [1,2,3,4]:
        #    print("correct type")
           for pos in enemy_path:
                pos_piece = self.board.get(pos)
                if pos_piece is not None:
                        return False
        # else: 
        #     for pos in enemy_path:
        #         pos_piece = self.board.get(pos)
        #         if self.board.get(pos) is not None:
        #                 return False
        return True

    def undo_move(self, source, source_piece, dest):
        self.board.set(source, source_piece)
        self.board.set(dest, None)
        # self.white_to_play = not self.white_to_play

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


    def get_my_king_pos(self, color):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        nums = [1,2,3,4,5,6,7,8]
        for x in letters:
            for y in nums:
                pos = x + str(y)
                curr_piece = self.board.get(pos)
                if curr_piece is not None:
                    if(curr_piece.type_enum() == 6 and curr_piece._is_white == color):
                        return pos
        return ""


    def check_king(self, move):
        # your king is in check if you make a move that allows easy access from other piece to king
        print("in check king")
        op_color = not self.white_to_play
        # self.white_to_play = not self.white_to_play
        source_pos = self.get_source_pos(move)
        source_piece = self.board.get(source_pos)
        dest = self.get_dest_pos(move)
        ############################## WTF ####################################
        valid_source_movements = source_piece.valid_moves(source_pos)
        dest_pos = self.get_dest_pos(move)
        self.board.set(source_pos, None)
        self.board.set(dest, source_piece)
        king_pos = self.get_my_king_pos(self.white_to_play)
        enemy_pieces_loc = self.get_piece(op_color)
        # print(enemy_pieces_loc)
        for loc in enemy_pieces_loc:
            enemy_piece = self.get_source_piece(loc)
            enemy_movements = enemy_piece.valid_moves(loc)
            if king_pos in enemy_movements:
                # print("dest in enemy movements")
                # print(enemy_movements)
                # print(enemy_piece)
                enemy_path = enemy_piece.get_path(loc, king_pos)
                # print(enemy_path)
                enemy_type = enemy_piece.type_enum()
                if(self.check_one_hop_king(enemy_type, enemy_path)): 
                    #a valid next-hop path to my king exists
                    self.undo_move(source_pos, source_piece, dest)
                    # print("ayo king is one hop away")
                    return True
        # self.board.set(source_pos, source_piece)
        # self.board.set(dest, None)
        self.undo_move(source_pos, source_piece, dest)
        return False
    
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
