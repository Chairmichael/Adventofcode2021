
def is_bingo(board):
	for row in board:
		if sum(row) == len(row):
			return True
	for i in range(len(board)):
		if sum(row[i] for row in board) == len(board):
			return True
	return False


def evaluate_board(board, drawings):
	size = len(board)
	score_board = [[False for x in row] for row in board]
	matches = 0
	for amount_drawn, num in enumerate(drawings):
		for i in range(size):
			for j in range(size):
				if board[i][j] == num:
					score_board[i][j] = True
					matches += 1
					if matches >= size and is_bingo(score_board):
						sumation = 0
						for i, row in enumerate(board):
							for j, el in enumerate(row):
								if not score_board[i][j]:
									sumation += int(el)
						return [amount_drawn+1, sumation * int(num)]
	return 0


def main():
	drawings = []
	winning_boards = []
	with open('input.txt') as input:
		data = input.readlines()
		data.append('\n') # So the last board can be evaluated
		drawings = data[0].strip().split(',')
		new_board = []
		for line in data[2:]:
			if line != '\n':
				new_board.append(line.strip().split())
			else:
				board_evaluation = evaluate_board(new_board, drawings)
				if board_evaluation != 0:
					winning_boards.append(board_evaluation)
				new_board = []

	win = sorted(winning_boards, key=lambda i:i[0])[-1]
	print(len(winning_boards))
	print(win)

if __name__ == '__main__':
	main()
