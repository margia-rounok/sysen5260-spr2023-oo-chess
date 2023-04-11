# Python3 program to implement the above approach

# Function to check if any of the two
# kings is unsafe or not
board = []

def get_piece(piece_id, color): 
	return [] #TODO: returns list of all pieces of this color 

def checkBoard(is_white_to_play, king_pos, curr_color: bool):
  i = king_pos[0]
  j = king_pos[1]

  # Check for Knight
  if checkKnight('N', i, j):
    return True

  # Check for Pawn
  if checkPawn('P', i, j):
    return True

  # Check for Rook
  if lookForr('R', i, j):
    return 1

  # Check for Bishop
  if lookForb('B', i, j):
    return 1

  # Check for Queen
  if lookForq('Q', i, j):
    return 1

  # Check for King
  if lookFork('K', i, j):
    return 1


def checkKnight(c, i, j, curr_color):
	# Store all possible moves of the king
	x = [ -1, -1, -1, 0, 0, 1, 1, 1 ]
	y = [ -1, 0, 1, -1, 1, -1, 0, 1 ]

	for k in range(8):
		# incrementing index values
		m = i + x[k]
		n = j + y[k]
		pos = str(m) + str(n)
		# checking boundary conditions
		# and character match
		if inBounds(m, n) and self.board.get(pos)._is_white is not curr_color:
			return True
	return False

# Function to check if Queen can attack the King
def lookForq(board, c, i, j):

	# Queen's moves are a combination
	# of both the Bishop and the Rook
	if lookForb(board, c, i, j) or lookForr(board, c, i, j):
		return True
	return False

# Function to check if bishop can attack the king
def lookForb(board, c, i, j):
	# Check the lower right diagonal
	k = 0
	while inBounds(i + ++k, j + k):
		if board[i + k][j + k] == c:
			return True
		if board[i + k][j + k] != '-':
			break

	# Check the lower left diagonal
	k = 0
	while inBounds(i + ++k, j - k):
		if board[i + k][j - k] == c:
			return True
		if board[i + k][j - k] != '-':
			break

	# Check the upper right diagonal
	k = 0
	while inBounds(i - ++k, j + k):
		if board[i - k][j + k] == c:
			return True
		if board[i - k][j + k] != '-':
			break

	# Check the upper left diagonal
	k = 0
	while inBounds(i - ++k, j - k):
		if board[i - k][j - k] == c:
			return True
		if board[i - k][j - k] != '-':
			break

	return False

# Check if
def lookForr(board, c, i, j):
	# Check downwards
	k = 0
	while inBounds(i + ++k, j):
		if board[i + k][j] == c:
			return True
		if board[i + k][j] != '-':
			break

	# Check upwards
	k = 0
	while inBounds(i + --k, j):
		if board[i + k][j] == c:
			return True
		if board[i + k][j] != '-':
			break

	# Check right
	k = 0
	while inBounds(i, j + ++k):
		if board[i][j + k] == c:
			return True
		if board[i][j + k] != '-':
			break

	# Check left
	k = 0
	while inBounds(i, j + --k):
		if board[i][j + k] == c:
			return True
		if board[i][j + k] != '-':
			break
	return False

# Check if the knight can attack the king
def lookForn(board, c, i, j):
	# All possible moves of the knight
	x = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
	y = [ 1, -1, 1, -1, 2, -2, 2, -2 ]

	for k in range(8):
		# Incrementing index values
		m = i + x[k]
		n = j + y[k]

		# Checking boundary conditions
		# and character match
		if inBounds(m, n) and board[m][n] == c:
			return True
	return False

# Function to check if pawn can attack the king
def checkPawn(c, i, j):
	if c == True:
		# Check for white pawn
		lookFor = get_piece(1, c)
		if inBounds(i + 1, j - 1) and self.board.get(str(i + 1) + str(j-1)) in lookFor:
			return True

		if inBounds(i + 1, j + 1) and self.board.get(str(i + 1) + str(j+1)) in lookFor:
			return True
	else:
		# Check for black pawn
		lookFor = get_piece(1, not c)
		if inBounds(i - 1, j - 1) and self.board.get(str(i - 1) + str(j-1)) in lookFor:
			return True
		if inBounds(i - 1, j + 1) and self.board.get(str(i - 1) + str(j+1)) in lookFor:
			return True
	return False

# Check if the indices are within
# the matrix or not
def inBounds(i, j):
	# Checking boundary conditions
	return i >= 0 and i < 8 and j >= 0 and j < 8
