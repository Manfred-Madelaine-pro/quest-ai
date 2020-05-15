
try:
	from grid import cell
except ImportError:
	import cell


class GenericGrid:
	def __init__(self, width, length):
		global WIDTH
		global LENGTH

		WIDTH = width
		LENGTH = length

		self.__init_grid()
		self.__init_life()

	def __init_grid(self):
		self.grid = []
		self.is_complete = False

		for x in range(WIDTH):
			row = []
			for y in range(LENGTH):
				c = cell.Cell(x, y)
				row.append(c)
			self.grid.append(row)

	def __init_life(self):
		self.__init_cells()
		self.__init_entities()

	def __init_cells(self):
		for x in range(WIDTH):
			for y in range(LENGTH):
				self.grid[x][y].generate()

	def __init_entities(self):
		# TODO create living beings
		pass


	def start(self):
		self.is_complete = False

	def update(self):
		self.update_entities()

	def stop(self):
		print("End Puzzle.")
		self.is_complete = True


	def update_entities(self):
		# update entities (characters)
		# update cells
		pass

	def update_cells(self):
		# update water (specific pattern)
		# update food

		for x in range(WIDTH):
			for y in range(LENGTH):
				self.grid[x][y].update()