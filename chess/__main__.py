import chess.model as model
import chess.view as view

import chess.rules as rules

rules = rules.Rules()
game = model.Game()
game.set_up_pieces()

while not game.game_over:
    print("")
    print(view.board_to_text(game.board))
    prompt = "White to play:" if game.white_to_play else "Black to play:"
    move = input(prompt)
    legal_move, message, captured_piece_location = rules.validate_move(move, game)

    if legal_move:        
        game.accept_move(move,captured_piece_location)
        game.node_list_append(game.board)
        if rules.check_if_king_is_currently_in_check(game):
            print("check")
        if rules.check_if_own_king_is_in_checkmate(game):
            print("checkmate")
            game.game_over=True
            print(game.checkmate)
            break
    elif move == 'backup':
        game.reverse_game_state()
        print(view.board_to_text(game.board))
    else:
        print(message)
