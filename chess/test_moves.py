
import pytest
from chess import rules
from chess.model import Game, Board, Piece, Pawn, Rook, Knight, Bishop, Queen, King

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']


def test_pawn_move_one_square_forward():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'e2e4'

    # Act
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == None
    assert captured_piece_location == None

def test_pawn_move_two_squares_forward():
    # Arrange
    game = Game()
    game.set_up_pieces()
    move = 'e2e4'

    # Act
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == None
    assert captured_piece_location == None

def test_pawn_move_one_square_forward_to_occupied_square():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.board.set('e3', Pawn(is_white=True))

    move = 'e2e3'

    # Act
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == None
    assert captured_piece_location == None

def test_pawn_move_two_squares_forward_to_occupied_square():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.board.set('e4', Pawn(is_white=True))

    move = 'e2e4'

    # Act
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'ERROR: Improper destination move. Please try again.'
    assert captured_piece_location == None

def test_pawn_capture_diagonally():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.board.set('d3', Pawn(is_white=False))

    move = 'e2d3'

    # Act
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == None
    assert captured_piece_location == 'd4'

def test_pawn_capture_diagonally_to_empty_square():
    # Arrange
    game = Game()
    game.set_up_pieces()

    move = 'e2d3'

    # Act
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    # Assert
    assert legal_move == False
    assert message == 'ERROR: Improper destination move. Please try again.'
    assert captured_piece_location == None