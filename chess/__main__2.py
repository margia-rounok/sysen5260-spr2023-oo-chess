import chess.model as model
import chess.view as view

import chess.rules as rules
ruleset = rules.RuleSet()
rules = rules.Rules()
game = model.Game()
game.set_up_pieces()

while not game.game_over:
    print("")
    print(view.board_to_text(game.board))
    prompt = "White to play:" if game.white_to_play else "Black to play:"
    move = input(prompt)
    legal_move, message, captured_piece_location = rules.validate_move(move, game)
    # validation = ruleset.validate_move(move, game)
    # print(validation)
    if legal_move:
        game.accept_move(move,captured_piece_location)
    else:
        print(message)
