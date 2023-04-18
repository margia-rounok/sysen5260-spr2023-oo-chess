from chess.model import Board, Pawn, King

def test_board_ctor():
    board = Board()
    board.set('e2', Pawn(is_white=True))
    assert board.get('e2') == Pawn(is_white=True)
    assert board.get('e4') == None


# Path: tests\test_model.py



def test_board_set_and_get():
    board = Board()
    new_pawn = Pawn(is_white=True)
    board.set('e2', new_pawn)

    assert board.get('e2') == new_pawn
    assert board.get('e4') == None


def test_board_duplicate():
    board = Board()
    new_pawn = Pawn(is_white=True)
    board.set('e2', new_pawn)

    duplicate_board = board.duplicate()
    assert duplicate_board.get('e2') != None 
    assert duplicate_board.get('e2').type_enum == 1
    assert duplicate_board.get('e4') == None

    duplicate_board.set('e2', None)
    assert duplicate_board.get('e2') == None
    assert board.get('e2') == new_pawn


def test_board_get_all_piece_locations():
    board = Board()
    new_pawn = Pawn(is_white=True)
    board.set('e2', new_pawn)

    white_piece_locations = board.get_piece_locations(is_white=True)
    assert len(white_piece_locations) == 1
    assert white_piece_locations[0] == 'e2'

    black_piece_locations = board.get_piece_locations(is_white=False)
    assert len(black_piece_locations) == 0


def test_board_king_location():
    board = Board()
    white_king = King(is_white=True)
    black_king = King(is_white=False)
    board.set('e1', white_king)
    board.set('e8', black_king)

    assert board.king_location(is_white=True) == 'e1'
    assert board.king_location(is_white=False) == 'e8'