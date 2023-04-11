# Python3 program to implement the above approach

# Function to check if any of the two
# kings is unsafe or not
board = []

#TODO: convert to our game code and then slowly integrate everything
#TODO: change x to letters
def get_piece(piece_id, is_white): 
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
  nums = [1,2,3,4,5,6,7,8]
  pieces = []
  for x in letters:
    for y in nums:
        pos = x + str(y)
        curr_piece = self.board.get(pos)
        if curr_piece is not None:
          if(curr_piece._is_white == is_white and curr_piece.type_enum() == piece_id):
            pieces.append(curr_piece)

  return pieces #TODO: returns list of all pieces of this color 

def checkBoard(is_white_to_play, king_pos, curr_color: bool):
  i = king_pos[0]
  j = king_pos[1]

  # Check for Knight
  if checkKnight(is_white, i, j):
    return True

  # Check for Pawn
  if checkPawn(is_white, i, j):
    return True

  # Check for Rook
  if checkRook(is_white, i, j):
    return 1

  # Check for Bishop
  if checkBishop(is_white, i, j):
    return 1

  # Check for Queen
  if checkQueen(is_white, i, j):
    return 1

  # Check for King
  if checkKing(is_white, i, j):
    return 1

def checkKnight(c, i, j):
    # All possible moves of the knight
    x = [ 2, 2, -2, -2, 1, 1, -1, -1 ]
    y = [ 1, -1, 1, -1, 2, -2, 2, -2 ]
 
    for k in range(8):
        # Incrementing index values
        m = i + x[k]
        n = j + y[k]
        pos = str(m) + str(n)
        # Checking boundary conditions
        # and character match
        if inBounds(m, n) and self.board.get(pos)._is_white == c:
            return True
    return False

def checkKing(curr_color, i, j):
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
def checkQueen(c, i, j):

	# Queen's moves are a combination
	# of both the Bishop and the Rook
	if checkBishop(c, i, j) or checkRook(c, i, j):
		return True
	return False

# Function to check if bishop can attack the king
def checkBishop(board, c, i, j):
	# Check the lower right diagonal
	k = 0
	while inBounds(i + ++k, j + k):
		if self.board.get(str(i+k) + str(j+k))._is_white == c:
			return True
		if self.board.get(str(i+k) + str(j+k)) != None:
			break

	# Check the lower left diagonal
	k = 0
	while inBounds(i + ++k, j - k):
		if self.board.get(str(i+k) + str(j-k))._is_white == c:
			return True
		if self.board.get(str(i+k) + str(j-k)) != None:
			break

	# Check the upper right diagonal
	k = 0
	while inBounds(i - ++k, j + k):
		if self.board.get(str(i-k) + str(j+k))._is_white == c:
			return True
		if self.board.get(str(i-k) + str(j+k))._is_white != None:
			break

	# Check the upper left diagonal
	k = 0
	while inBounds(i - ++k, j - k):
		if self.board.get(str(i-k) + str(j-k))._is_white == c:
			return True
		if self.board.get(str(i-k) + str(j-k)) != None:
			break

	return False

# Check if
def checkRook(c, i, j):
	# Check downwards
	k = 0
	while inBounds(i + ++k, j):
		if self.board.get(str(i+k) + str(j))._is_white == c:
			return True
		if self.board.get(str(i+k) + str(j)) != None:
			break

	# Check upwards
	k = 0
	while inBounds(i + --k, j):
		if self.board.get(str(i+k) + str(j))._is_white == c:
			return True
		if self.board.get(str(i+k) + str(j)) != None:
			break

	# Check right
	k = 0
	while inBounds(i, j + ++k):
		if self.board.get(str(i) + str(j+k))._is_white == c:
			return True
		if self.board.get(str(i) + str(j+k)) != None:
			break

	# Check left
	k = 0
	while inBounds(i, j + --k):
		if self.board.get(str(i) + str(j+k))._is_white:
			return True
		if self.board.get(str(i) + str(j+k)) != None:
			break
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
