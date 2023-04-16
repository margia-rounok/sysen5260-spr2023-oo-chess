import chess.model as model
import chess.view as view


rules = model.Rules()

#TODO move none type 
game = model.Game()
game.set_up_pieces()
while not game.game_over:
    print("")
    print(view.board_to_text(game.board))
    move = ""
    while True: 
        prompt = "White to play: " if game.white_to_play else "Black to play: "
        move = input(prompt)
        
        #game.piece_list_append(move)
        if move == 'backup':
             game.do_backup(move)
             break
        # elif game.is_checkmate(): 
        #      print("Your king has been checkmated. Game over.")
        #      break
        elif game.check_input(move) is None or not game.check_moved_op(move): #valid move
            # and not game.check_move_exist(move)
            # print("here")
            print("ERROR: Improper source move. Please try again.")
        elif not game.check_no_piece_override(move):
            print("ERROR: Improper destination move. Please try again.")

        else:
            source_type = game.get_source_type(move)
            if game.check_king(move):
                print("ERROR: Your king is in check with this move. Please try again") 
            elif not game.check_no_piece_override(move) or not game.check_piece(move, source_type):
                    print("ERROR: Improper destination move for pawn. Please try again.")
            else:
                print("in else")
                break
        

        game.accept_move(move)
        game.move_history_append(move)
