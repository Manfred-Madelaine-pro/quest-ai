import random

try:
	import entity
except ImportError:
	from back import entity


VERBOSE = False


class GenericGrid:
	def __init__(self, width, length):
		self.width = width
		self.length = length
		self.init_cells()

	def __str__(self):
		title = f"\tGrid ({self.width}, {self.length})"
		grid = ''
		for x in range(self.width):
			if len(grid) > 0 : grid += '\n'
			for y in range(self.length):
				grid += '{:5}'.format(self.cells[(x, y)].water)

		return grid + title

	def init_cells(self):
		self.cells = {}
		for x in range(self.width):
			for y in range(self.length):
				c = entity.Cell(x, y)
				self.cells[(x, y)] = c

	def generate_cells(self):
		for x in range(self.width):
			for y in range(self.length):
				self.cells[(x, y)].generate()

	def update_cells(self):
		for x in range(self.width):
			for y in range(self.length):
				self.cells[(x, y)].update()

	def out_of_boud(self, x, y):
		return (x < 0 or x >= self.width) or (y < 0 or y >= self.length)

# --------------------------------------------------------------------------

class Model(GenericGrid):
	def __init__(self, width, length, conf={}):
		super().__init__(width, length)
		self.nb_entities = conf['nb_entities'] if conf else 2
		self.init_life()

	def init_cells(self):
		self.turn = 0
		self.is_complete = False
		super().init_cells()

	def init_life(self):
		self.generate_cells()
		self.generate_beings()

# --------------------------------------------------------------------------

	def generate_beings(self):
		self.beings = {}
		self.dead_names = []

		for i in range(self.nb_entities):
			x, y = self.get_random_pos()
			self.beings[i] = entity.Being(i, x, y, self)

	def get_random_pos(self):
		x = random.randint(0, self.width-1)
		y = random.randint(0, self.length-1)
		return x, y

# --------------------------------------------------------------------------

	def start(self):
		self.is_complete = False

	def stop(self):
		verbose_print("End Simulation.")
		self.is_complete = True

	def update(self):
		verbose_print(f'---- turn : {self.turn} ----')
		self.remove_beings()
		self.dead_names = []

		self.update_beings()
		# self.update_cells() TODO
		self.turn += 1

# --------------------------------------------------------------------------

	def update_beings(self):
		for being in self.beings.values():
			being.update()

			if not being.alive:
				self.register_dead_being(being)

		if len(self.beings) == 0:
			self.stop()

	def register_dead_being(self, being):
		self.dead_names += [being.u_name]

	def remove_beings(self):
		for name in self.dead_names:
			dead = self.beings.pop(name)

# --------------------------------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None

def test_Grid():
	width = 2
	grid = GenericGrid(width, width)
	grid.generate_cells()
	print(grid)

def test_Model():
	width = 5
	length = width
	model = Model(width, length)
	print(model)

	for i in range(5):
		model.update()
		print(model)


if __name__ == '__main__':
	test_Grid()
	test_Model()

