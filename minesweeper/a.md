if no = 0 
	{arround of cell} mark_safe

if cell.nearby.count == no 
	{all of them} mark_mine

if no == marked_mine && cell.nearby.count > no 
	{others} mark_safe

def unopened_nearby_cells(self):
	"""
	Returns a list of groups of unopened cells of the same size.
	"""
	unopened_cells = []
	for i in range(self.height):
		for j in range(self.width):
			if self.board[i][j] is None:
				unopened_cells.append((i, j))
	
	# Group cells by size (if applicable)
	# Assuming size refers to the number of adjacent cells
	size_groups = {}
	for cell in unopened_cells:
		size = self.get_adjacent_cells_count(cell)
		if size not in size_groups:
			size_groups[size] = []
		size_groups[size].append(cell)
	
	return size_groups
		
def get_adjacent_cells_count(self, cell):
	"""
	Returns the count of adjacent cells for a given cell.
	"""
	count = 0
	for i in range(cell[0] - 1, cell[0] + 2):
		for j in range(cell[1] - 1, cell[1] + 2):
			if 0 <= i < self.height and 0 <= j < self.width and (i, j) != cell:
				count += 1
	return count