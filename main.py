import time
a = time.time()

def findNextEmpty(puzzle):
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == 0:
				return r, c
	return None, None

def isValid(puzzle, guess, row, col):
	row_vals = puzzle[row]
	if guess in row_vals:
		return False

	col_vals = [puzzle[i][col] for i in range(9)]
	if guess in col_vals:
		return False

	rowStart = (row // 3) * 3
	colStart = (col // 3) * 3

	for r in range(rowStart, rowStart + 3):
		for c in range(colStart, colStart + 3):
			if puzzle[r][c] == guess:
				return False

	return True

def solveSudoku(puzzle):
	row, col = findNextEmpty(puzzle)

	if row is None:
		return True 

	for guess in range(1, 10):
		if isValid(puzzle, guess, row, col):
			puzzle[row][col] = guess
			if solveSudoku(puzzle):
				return True		
		puzzle[row][col] = 0

	return False

if __name__ == '__main__':
	'''example_board = [
		[3, 9, 0,   0, 5, 0,   0, 0, 0],
		[0, 0, 0,   2, 0, 0,   0, 0, 5],
		[0, 0, 0,   7, 1, 9,   0, 8, 0],

		[0, 5, 0,   0, 6, 8,   0, 0, 0],
		[2, 0, 6,   0, 0, 3,   0, 0, 0],
		[0, 0, 0,   0, 0, 0,   0, 0, 4],

		[5, 0, 0,   0, 0, 0,   0, 0, 0],
		[6, 7, 0,   1, 0, 5,   0, 4, 0],
		[1, 0, 9,   0, 0, 0,   2, 0, 0]
	]'''
	example_board = [
		[7, 0, 6,   4, 0, 0,   8, 0, 3],
		[0, 4, 0,   0, 8, 0,   0, 2, 0],
		[0, 0, 0,   0, 0, 0,   0, 0, 0],

		[2, 0, 0,   0, 0, 0,   5, 0, 0],
		[0, 8, 0,   0, 5, 0,   0, 9, 0],
		[0, 0, 3,   0, 0, 0,   0, 0, 7],

		[0, 0, 0,   0, 0, 0,   0, 0, 0],
		[0, 5, 0,   0, 9, 0,   0, 6, 0],
		[3, 0, 1,   0, 0, 5,   7, 0, 4]
	]
	for i in range(9):
		for j in range(9):
			print(example_board[i][j], " ", end="")
			if j == 2 or j == 5:
				print("\t", end="")
		print()
		if i == 2 or i == 5:
			print()
	print(solveSudoku(example_board))
	print("--------------------------")
	for i in range(9):
		for j in range(9):
			print(example_board[i][j], " ", end="")
			if j == 2 or j == 5:
				print("\t", end="")
		print()
		if i == 2 or i == 5:
			print()

	b = time.time()
	print()
	print("TIME = " + str(b - a))
