# import pytest
from chess.model_2 import Game, Board, Piece, Pawn, Rook, Knight, Bishop, Queen, King
from chess.rules import Rules 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']


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
    game.board.set('d3', Pawn(is_white=False))

    move = 'e2d3'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == 'd3'

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


def test_pawn_capture_en_passant():
    # Arrange
    game = Game()
    game.set_up_pieces()
    captured_pawn = Pawn(is_white=False)
    captured_pawn.has_moved = True
    captured_pawn.just_moved_two_squares = True
    game.board.set('d5', Pawn(is_white=True))
    game.board.set('e5', captured_pawn)

    move = 'd5e6'

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Valid move.'
    assert captured_piece_location == 'e5'