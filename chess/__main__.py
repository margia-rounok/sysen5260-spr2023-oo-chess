import chess.model as model
import chess.view as view

game = model.Game()
game.set_up_pieces()
while not game.game_over:
    print("")
    print(view.board_to_text(game.board))
    move = ""
    while True: 
        prompt = "White to play:" if game.white_to_play else "Black to play:"
        move = input(prompt)

        if game.check_input(move) is None or game.check_moved_op(move): #valid move
            # and not game.check_move_exist(move)
            # print("here")
            print("ERROR: Improper source move. Please try again.")
        elif not game.check_no_piece_override(move):
            print("ERROR: Improper destination move. Please try again.")
        elif not game.move_bischop(move):
            print("ERROR: Improper destination move for bischop. Please try again.")
        else:
            break
        
    # prompt = "White to play:" if game.white_to_play else "Black to play:"
    # move = input(prompt)
    # game.accept_move(move)
