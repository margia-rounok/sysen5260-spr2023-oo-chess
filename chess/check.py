# Python3 program to implement the above approach

# Function to check if any of the two
# kings is unsafe or not
def checkBoard(board, is_white_to_play):

	# Find the position of both the kings
	for i in range(8):
		for j in range(8):
		
			# Check for all pieces which
			# can attack White King
			if board[i][j] == 'k':
			
				# Check for Knight
				if lookForn(board, 'N', i, j):
					return 1

				# Check for Pawn
				if lookForp(board, 'P', i, j):
					return 1

				# Check for Rook
				if lookForr(board, 'R', i, j):
					return 1

				# Check for Bishop
				if lookForb(board, 'B', i, j):
					return 1

				# Check for Queen
				if lookForq(board, 'Q', i, j):
					return 1

				# Check for King
				if lookFork(board, 'K', i, j):
					return 1

			# Check for all pieces which
			# can attack Black King
			if board[i][j] == 'K':
				# Check for Knight
				if lookForn(board, 'n', i, j):
					return 2

				# Check for Pawn
				if lookForp(board, 'p', i, j):
					return 2

				# Check for Rook
				if lookForr(board, 'r', i, j):
					return 2

				# Check for Bishop
				if lookForb(board, 'b', i, j):
					return 2

				# Check for Queen
				if lookForq(board, 'q', i, j):
					return 2

				# Check for King
				if lookFork(board, 'k', i, j):
					return 2
	return 1

def lookFork(board, c, i, j):
	# Store all possible moves of the king
	x = [ -1, -1, -1, 0, 0, 1, 1, 1 ]
	y = [ -1, 0, 1, -1, 1, -1, 0, 1 ]

	for k in range(8):
		# incrementing index values
		m = i + x[k]
		n = j + y[k]

		# checking boundary conditions
		# and character match
		if inBounds(m, n) and board[m][n] == c:
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
def lookForp(board, c, i, j):
	if ord(c) >= 65 and ord(c) <= 90:
		# Check for white pawn
		lookFor = 'P'
		if inBounds(i + 1, j - 1) and board[i + 1][j - 1] == lookFor:
			return True

		if inBounds(i + 1, j + 1) and board[i + 1][j + 1] == lookFor:
			return True
	else:
		# Check for black pawn
		lookFor = 'p'
		if inBounds(i - 1, j - 1) and board[i - 1][j - 1] == lookFor:
			return True
		if inBounds(i - 1, j + 1) and board[i - 1][j + 1] == lookFor:
			return True
	return False

# Check if the indices are within
# the matrix or not
def inBounds(i, j):
	# Checking boundary conditions
	return i >= 0 and i < 8 and j >= 0 and j < 8

# Chessboard instance
board = [ [ '-', '-', '-', 'k', '-', '-', '-', '-' ],
[ 'p', 'p', 'p', '-', 'p', 'p', 'p', 'p' ],
[ '-', '-', '-', '-', '-', 'b', '-', '-' ],
[ '-', '-', '-', 'R', '-', '-', '-', '-' ],
[ '-', '-', '-', '-', '-', '-', '-', '-' ],
[ '-', '-', '-', '-', '-', '-', '-', '-' ],
[ 'P', '-', 'P', 'P', 'P', 'P', 'P', 'P' ],
[ 'K', '-', '-', '-', '-', '-', '-', '-' ] ]

if checkBoard(board) == 0:
print("No king in danger")
elif checkBoard(board) == 1:
print("White king in danger")
else:
print("Black king in danger")

# This code is contributed by divyeshrabadiya07.
