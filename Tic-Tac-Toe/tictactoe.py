"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
	"""
	Returns starting state of the board.
	"""
	return [[EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY],
			[EMPTY, EMPTY, EMPTY]]


def player(board):
	"""
	Returns player who has the next turn on a board.
	"""
	X_count = sum(row.count(X) for row in board)
	O_count = sum(row.count(O) for row in board)
	return X if X_count <= O_count else O


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	if terminal(board):
		return None
	return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}
	

def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	if action not in actions(board):
		raise Exception("Invalid action")
	new_board = copy.deepcopy(board)
	new_board[action[0]][action[1]] = player(board)
	return new_board


def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
			return board[i][0]
		if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
			return board[0][i]
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
		return board[0][0]
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
		return board[0][2]
	return None


def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	return winner(board) is not None or not any(EMPTY in row for row in board)


def utility(board):
	"""
	Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
	"""
	if winner(board) == "X":
		return 1
	elif winner(board) == "O":
		return -1
	else:
		return 0

def optimal_max(board):
	if terminal(board):
		return utility(board), None
	value = float('-inf')
	best_move = None
	for act in actions(board):
		temp = result(board, act)
		opt_value, _ = optimal_min(temp)
		if opt_value > value:
			value = opt_value
			best_move = act
			if value == 1:
				break
	return value, best_move

def optimal_min(board):
	if terminal(board):
		return utility(board), None
	value = float('inf')
	best_move = None
	for act in actions(board):
		successor = result(board, act)
		opt_value, _ = optimal_max(successor)
		if opt_value < value:
			value = opt_value
			best_move = act
			if value == -1:
				break
	return value, best_move

def minimax(board):
	"""
	Returns the optimal action for the current player on the board.
	"""
	if terminal(board):
		return None
	if player(board) == X:
		_, best_move = optimal_max(board)
	else:
		_, best_move = optimal_min(board)
	return best_move