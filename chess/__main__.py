import chess.model as model
import chess.view as view

import chess.rules as rules

rules = rules.Rules()
game = model.Game()
game.set_up_pieces()

board_lst = []
board_lst.insert(0, game.board)
# print(view.board_to_text(board_lst[0]))

while not game.game_over:
    if rules.check_if_king_is_in_checkmate(game):
        print("checkmate")
        game.game_over=True
        break
    print("")
    print("debug old board")
    print(view.board_to_text(game.board))
    prompt = "White to play:" if game.white_to_play else "Black to play:"
    move = input(prompt)
    legal_move, message, captured_piece_location = rules.validate_move(move, game)
    # game.move_list_append(move)
    board_lst.insert(0, game.board)
    # print(view.board_to_text(board_lst[0]))

    if rules.check_if_king_is_currently_in_check(game):
    
        print("check")
    if legal_move:
        #game.move_list_append(move)
        print("appended to node list")
        
        game.accept_move(move,captured_piece_location)
        game.node_list_append(game.board)

        
        # board_lst.prepend(game.board)
    elif move == 'backup':
        # game.do_backup(move)
        game.reverse_game_state()
        # game.board = board_lst[0]
        print("hehe")
        print(view.board_to_text(game.board))
        # break
    else:
        print(message)
