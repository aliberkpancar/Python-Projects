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
	X = "X"
	O = "O"
	if board == initial_state():
		return X
	X_count = sum(row.count(X) for row in board)
	O_count = sum(row.count(O) for row in board)
	return X if X_count == O_count else O


def actions(board):
	"""
	Returns set of all possible actions (i, j) available on the board.
	"""
	if terminal(board):
		return None
	possible_actions = set()
	for i in range (3):
		for j in range (3):
			if board[i][j] == EMPTY:
				possible_actions.add((i,j))
	return possible_actions
	

def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	if action not in actions(board):
		raise Exception
	backup_board = copy.deepcopy(board)
	backup_board[action[0]][action[1]] = player(board)
	return backup_board


def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	for i in range(3):
		if board[i][0] == board[i][1] == board[i][2] != EMPTY:
			return board[i][0]
		if board[0][i] == board[1][i] == board[2][i] != EMPTY:
			return board[0][i]
	if board[0][0] == board[1][1] == board[2][2] != EMPTY:
		return board[0][0]
	if board[0][2] == board[1][1] == board[2][0] != EMPTY:
		return board[0][2]
	return None


def terminal(board):
	"""
	Returns True if game is over, False otherwise.
	"""
	return True if winner(board) != None else False


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
		successor = result(board, act)
		opt_value, _ = optimal_min(successor)
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
		value, move = optimal_max(board)
	else:
		value, move = optimal_min(board)
	return move