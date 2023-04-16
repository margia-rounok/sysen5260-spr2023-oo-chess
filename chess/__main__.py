import chess.model_2 as model
import chess.view_2 as view

import chess.rules as rules

rules = rules.Rules()
game = model.Game()
game.set_up_pieces()

board_lst = []
while not game.game_over:
    print("")
    print(view.board_to_text(game.board))
    prompt = "White to play:" if game.white_to_play else "Black to play:"
    move = input(prompt)
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    if legal_move:
        game.accept_move(move,captured_piece_location)
        board_lst.append(game.board)
    elif move == 'backup':
        game.do_backup(move)
        break
    else:
        print(message)
