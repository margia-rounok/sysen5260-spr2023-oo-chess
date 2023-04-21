# import pytest
from chess.model import Game, Board, Piece, Pawn, Rook, Knight, Bishop, Queen, King
from chess.rules import Rules 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

def test_invalid_cmd():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'r3454r4343'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Enter a valid command.'
    assert captured_piece_location == None

def test_no_piece():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'e3e4'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'No piece at source position.'
    assert captured_piece_location == None

def test_move_opponent_piece():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'e7e6'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Wrong color piece at source position.'
    assert captured_piece_location == None

def test_pawn_move_one_square_forward():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'e2e4'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_pawn_move_two_squares_forward():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'e2e4'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_pawn_move_one_square_forward_to_occupied_square():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.board.set('e3', Pawn(is_white=True))

    move = 'e2e3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Wrong color piece at destination position.'
    assert captured_piece_location == 'e3'

def test_pawn_move_two_squares_forward_to_occupied_square():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.board.set('e4', Pawn(is_white=True))

    move = 'e2e4'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Wrong color piece at destination position.'
    assert captured_piece_location == 'e4'

def test_pawn_capture_diagonally():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',game)
    game.accept_move('d7d5',game)

    move = 'e4d5'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == 'd5'

def test_pawn_capture_diagonally_to_empty_square():
    # Arrange
    game = Game()
    game.set_up_pieces()

    move = 'e2d3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Invalid move for piece.'
    assert captured_piece_location == None

def test_king_in_check():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("d2", "d4")
    game.make_normal_move("e7", "e5")
    game.make_normal_move("b1", "c3")
    game.make_normal_move("f8", "b4")

    move = "c3d5"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Move puts own king in check.'
    assert captured_piece_location == None

def test_path_obstructed_move():
    # Arrange
    game = Game()
    game.set_up_pieces()

    move = 'c1e3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_king_in_check():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("d2", "d4")
    game.make_normal_move("e7", "e5")
    game.make_normal_move("b1", "c3")
    game.make_normal_move("f8", "b4")

    move = "c3d5"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Move puts own king in check.'
    assert captured_piece_location == None

def test_biscop_valid_multiple_forward_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("d2", "d4")
    game.make_normal_move("e7", "e5")

    move = "c1f4"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_biscop_valid_multiple_backward_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("d2", "d4")
    game.make_normal_move("e7", "e5")
    game.make_normal_move("c1", "f4")

    move = "f4d2"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_biscop_invalid_multiple_backward_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("d2", "d4")
    game.make_normal_move("e7", "e5")
    game.make_normal_move("c1", "f4")
    game.make_normal_move("a7", "a5")
    game.make_normal_move("d1", "d2")
    game.make_normal_move("h7", "h6")

    move = "f4c1"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_rook_valid_multiple_vertical_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("a2", "a6") # skips valid mult pawn movements

    move = "a1a4"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_rook_valid_multiple_horizontal_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("a2", "a6") # skips valid mult pawn movements
    game.make_normal_move("a1", "a4") # rook moves vertically

    move = "a4b4" # rook moves horizontally

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_rook_invalid_multiple_vertical_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("a2", "a6") # skips valid mult pawn movements
    game.make_normal_move("b1", "a3")
    move = "a1a4"

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_rook_valid_multiple_horizontal_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.make_normal_move("a2", "a4") 
    game.make_normal_move("b2", "b3") 
    game.make_normal_move("a1", "a3") 

    move = "a3c3" # rook moves horizontally

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_pawn_capture_en_passant():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('d7d5',None)
    game.accept_move('e4d5',None)
    game.accept_move('e7e5',None)

    move = 'd5e6'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == 'e5'

def test_castle_king_side():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('f1c4',None)
    game.accept_move('b8c6',None)
    game.accept_move('g1f3',None)
    game.accept_move('g8f6',None)

    move = 'e1g1'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_castle_queen_side():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('e7e5',None)
    game.accept_move('c1f4',None)
    game.accept_move('b8c6',None)
    game.accept_move('b1c3',None)
    game.accept_move('h7h6',None)
    game.accept_move('d1d2',None)
    game.accept_move('g8f6',None)

    move = 'e1c1'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None


def test_castle_king_side_invalid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('f1c4',None)
    game.accept_move('b8c6',None)
    game.accept_move('g1f3',None)
    game.accept_move('g8f6',None)
    game.accept_move('e1e2',None)
    game.accept_move('e8e7',None)
    game.accept_move('e2e1',None)
    game.accept_move('e7e8',None)

    move = 'e1g1'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Invalid move for piece.'
    assert captured_piece_location == None

def test_queen_valid_multiple_vertical_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)

    move = 'd1d3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_queen_valid_multiple_horizontal_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)
    game.accept_move('d1d3',None)
    game.accept_move('h5h4',None)

    move = 'd3f3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_queen_valid_multiple_diagonal_forward_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)
    game.accept_move('d1d3',None)
    game.accept_move('h5h4',None)

    move = 'd3b5'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_queen_valid_multiple_diagonal_backwards_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)
    game.accept_move('d1d3',None)
    game.accept_move('h5h4',None)
    game.accept_move('d3b5',None)
    game.accept_move('h4h3',None)

    move = 'b5d3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_queen_invalid_multiple_verticle_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)

    move = 'd1d5'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_queen_invalid_multiple_diagonal_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    move = 'd8f6'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_queen_invalid_multiple_horizontal_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)
    game.accept_move('d1d3',None)
    game.accept_move('h5h4',None)
    game.accept_move('e2e3',None)
    game.accept_move('h4h3',None)

    move = 'd3g3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_queen_invalid_multiple_diagonal_moves():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    move = 'd8f6'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Path is not clear.'
    assert captured_piece_location == None

def test_knight_valid_horizontal():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)
    move = 'b1d2'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_knight_valid_horizontal():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'b1c3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_knight_valid_horizontal():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('h7h5',None)
    move = 'b1d2'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_knight_invalid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'b1d2'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Wrong color piece at destination position.'

def test_king_vertical_move_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)

    move = 'e1e2'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_vertical_move_invalid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)

    move = 'e1e3'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Invalid move for piece.'
    assert captured_piece_location == None

def test_king_horizontal_move_right_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)

    move = 'e3f3'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_horizontal_move_left_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)

    move = 'e3d3'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None


def test_king_horizontal_move_invalid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'b1d2'
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)

    move = 'e3g3'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Invalid move for piece.'
    assert captured_piece_location == None

def test_king_diagonal_move_right_up_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)

    move = 'e3f4'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_diagonal_move_left_up_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)

    move = 'e3d4'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_diagonal_move_right_down_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)
    game.accept_move('f2f4',None)
    game.accept_move('h5h4',None)

    move = 'e3f2'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_diagonal_move_right_down_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)
    game.accept_move('f2f4',None)
    game.accept_move('h5h4',None)

    move = 'e3f2'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_diagonal_move_left_down_valid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)
    game.accept_move('d2d4',None)
    game.accept_move('h5h4',None)

    move = 'e3d2'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == None

def test_king_diagonal_invalid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)
    game.accept_move('d2d4',None)
    game.accept_move('h5h4',None)

    move = 'e3g5'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Invalid move for piece.'
    assert captured_piece_location == None

def test_king_diagonal_path_invalid():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('e2e4',None)
    game.accept_move('e7e5',None)
    game.accept_move('e1e2',None)
    game.accept_move('h7h6',None)
    game.accept_move('e2e3',None)
    game.accept_move('h6h5',None)

    move = 'e3f2'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Wrong color piece at destination position.'

def test_invalid_move_king_does_not_check():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('e7e5',None)
    game.accept_move('b1c3',None)
    game.accept_move('f8b4',None)

    move = 'c3d5'
    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'Move puts own king in check.'
    assert captured_piece_location == None

def test_resign():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.accept_move('e7e5',None)
    game.accept_move('b1c3',None)
    game.accept_move('f8b4',None)
    game.accept_move('c3d5',None)

    move = 'resign'
    # Act
    if move == 'resign':
        game.resign_move()

    # Assert
    assert game.game_over == True