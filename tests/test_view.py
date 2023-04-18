import chess.view as view
import chess.model as model
from chess.model import Game 
from chess.rules import Rules

def test_piece_to_char():
    assert '·' == view.piece_to_char(None)
    assert '♙' == view.piece_to_char(model.Pawn(is_white=True))
    assert '♟' == view.piece_to_char(model.Pawn(is_white=False))

def test_init_board():
    game = Game()
    game.set_up_pieces()
    board = game.get_board()
    assert view.board_to_text(board)[0:18] == '  a b c d e f g h\n'
    assert view.board_to_text(board)[18:37] == '8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n'
    assert view.board_to_text(board)[37:56] == '7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n'
    assert view.board_to_text(board)[56:75] == '6 · · · · · · · · \n'
    assert view.board_to_text(board)[75:94] == '5 · · · · · · · · \n'
    assert view.board_to_text(board)[94:113] == '4 · · · · · · · · \n'
    assert view.board_to_text(board)[113:132] == '3 · · · · · · · · \n'
    assert view.board_to_text(board)[132:151] == '2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n'
    assert view.board_to_text(board)[151:] == '1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n'

def test_backup_once():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.node_list_append(game.board)
    # Act
    game.reverse_game_state()
    board = game.get_board()

    # Assert
    assert view.board_to_text(board)[0:18] == '  a b c d e f g h\n'
    assert view.board_to_text(board)[18:37] == '8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n'
    assert view.board_to_text(board)[37:56] == '7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n'
    assert view.board_to_text(board)[56:75] == '6 · · · · · · · · \n'
    assert view.board_to_text(board)[75:94] == '5 · · · · · · · · \n'
    assert view.board_to_text(board)[94:113] == '4 · · · · · · · · \n'
    assert view.board_to_text(board)[113:132] == '3 · · · · · · · · \n'
    assert view.board_to_text(board)[132:151] == '2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n'
    assert view.board_to_text(board)[151:] == '1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n'

def test_backup_multiple():
    # Arrange
    game = Game()
    game.set_up_pieces()
    game.accept_move('d2d4',None)
    game.node_list_append(game.board)
    game.accept_move('h7h5',None)
    game.node_list_append(game.board)

    # Act
    game.reverse_game_state()
    board = game.get_board()

    # Assert
    assert view.board_to_text(board)[0:18] == '  a b c d e f g h\n'
    assert view.board_to_text(board)[18:37] == '8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n'
    assert view.board_to_text(board)[37:56] == '7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n'
    assert view.board_to_text(board)[56:75] == '6 · · · · · · · · \n'
    assert view.board_to_text(board)[75:94] == '5 · · · · · · · · \n'
    assert view.board_to_text(board)[94:113] == '4 · · · ♙ · · · · \n'
    assert view.board_to_text(board)[113:132] == '3 · · · · · · · · \n'
    assert view.board_to_text(board)[132:151] == '2 ♙ ♙ ♙ · ♙ ♙ ♙ ♙ \n'
    assert view.board_to_text(board)[151:] == '1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n'

    # Act
    game.reverse_game_state()
    board = game.get_board()

    # Assert -- go back to init state
    assert view.board_to_text(board)[0:18] == '  a b c d e f g h\n'
    assert view.board_to_text(board)[18:37] == '8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n'
    assert view.board_to_text(board)[37:56] == '7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n'
    assert view.board_to_text(board)[56:75] == '6 · · · · · · · · \n'
    assert view.board_to_text(board)[75:94] == '5 · · · · · · · · \n'
    assert view.board_to_text(board)[94:113] == '4 · · · · · · · · \n'
    assert view.board_to_text(board)[113:132] == '3 · · · · · · · · \n'
    assert view.board_to_text(board)[132:151] == '2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n'
    assert view.board_to_text(board)[151:] == '1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n'

    # Assert -- go back to init state
    assert view.board_to_text(board)[0:18] == '  a b c d e f g h\n'
    assert view.board_to_text(board)[18:37] == '8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n'
    assert view.board_to_text(board)[37:56] == '7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n'
    assert view.board_to_text(board)[56:75] == '6 · · · · · · · · \n'
    assert view.board_to_text(board)[75:94] == '5 · · · · · · · · \n'
    assert view.board_to_text(board)[94:113] == '4 · · · · · · · · \n'
    assert view.board_to_text(board)[113:132] == '3 · · · · · · · · \n'
    assert view.board_to_text(board)[132:151] == '2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n'
    assert view.board_to_text(board)[151:] == '1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n'
