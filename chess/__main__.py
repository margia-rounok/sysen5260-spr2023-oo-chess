import chess.model as model
import chess.view as view

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
        # print(move)
        if game.check_input(move) is None or not game.check_moved_op(move): #valid move
            # and not game.check_move_exist(move)
            # print("here")
            print("ERROR: Improper source move. Please try again.")
        elif not game.check_no_piece_override(move):
            print("ERROR: Improper destination move. Please try again.")
        else:
            source_type = game.get_source_type(move)
            if source_type == 1 and (not game.check_no_piece_override(move) or \
                not game.check_piece(move, source_type)):
                    print("ERROR: Improper destination move for pawn. Please try again.")
            elif source_type == 2 and (not game.check_no_piece_override(move) or \
                not game.check_piece(move, source_type)):
                    print("ERROR: Improper destination move for bischop. Please try again.")
            elif source_type == 3 and (not game.check_no_piece_override(move) \
                or not game.check_piece(move, source_type)):
                    print("ERROR: Improper destination move for rook. Please try again.")
            elif source_type == 4 and (not game.check_no_piece_override(move) \
                or not game.check_piece(move, source_type)):
                    print("ERROR: Improper destination move for queen. Please try again.")
            elif source_type == 5 and not game.check_piece(move, source_type): 
                #knight does not need to check for override per game rules
                print("ERROR: Improper destination move for knight. Please try again.")
            elif source_type == 6 and not game.check_piece(move, source_type): 
                #knight does not need to check for override per game rules
                print("ERROR: Improper destination move for king. Please try again.")
            else:
                print("in else")
                break
        
    # prompt = "White to play:" if game.white_to_play else "Black to play:"
    # move = input(prompt)
    # game.accept_move(move)
