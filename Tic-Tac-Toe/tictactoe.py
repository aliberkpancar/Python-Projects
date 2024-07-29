"""
Tic Tac Toe Player
"""
from copy import deepcopy
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
	possible_actions = set()
	for i in range (len(board)):
		for j in range (len(board[i])):
			if board[i][j] == "EMPTY":
				possible_actions.add((i,j))
	return possible_actions if len(possible_actions) > 0 else None
			

def result(board, action):
	"""
	Returns the board that results from making move (i, j) on the board.
	"""
	if action not in actions(board):
		raise Exception
	backup_board = deepcopy(board)
 
	return board



def winner(board):
	"""
	Returns the winner of the game, if there is one.
	"""
	print (range(len(board)))
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == "EMPTY":
				return None
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][0] == board[i][1] == board[i][2]:
				return board[i][0]
			elif board[0][j] == board[1][j] == board[2][j]:
				return board[0][j]
			elif board[0][0] == board[1][1] == board[2][2]:
				return board[0][0]
			elif board[0][2] == board[1][1] == board[2][0]:
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


def minimax(board):
	"""
	Returns the optimal action for the current player on the board.
	"""
	# If the board is a terminal board, the minimax function should return None
