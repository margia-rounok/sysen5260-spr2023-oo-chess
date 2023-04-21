from chess.model import Game, Board, Piece, Pawn, Rook, Knight, Bishop, Queen, King
from chess.rules import Rules 

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8']

def test_fool_mate():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('f2f3',None)
    game.accept_move('e7e5',None)
    game.accept_move('g2g4',None)
    # game.accept_move('d8h4',None)

    move = 'd8h4' #checkmate

    # Act
    legal_move, message, captured_piece_location = Rules.validate_move(move, game)

    # Assert
    assert legal_move == True
    assert message == 'Vaild move.'
    assert captured_piece_location == None

    game.accept_move(move,None)

# def test_variant():
#     # Arrange
#     game = Game()
#     game.set_up_pieces()
#     game.accept_move('e2e4',None)
#     game.accept_move('b8c6',None)
#     game.accept_move('g2g4',None)
#     game.accept_move('g2g4',None)
#     game.accept_move('c6d4',None)
#     game.accept_move('g1e2',None)

#     move = 'd4f3' #checkmate

#     # Act
#     legal_move, message, captured_piece_location = Rules.validate_move(move, game)

#     # Assert
#     assert legal_move == True
#     assert message == 'Checkmate!'
#     assert captured_piece_location == None

