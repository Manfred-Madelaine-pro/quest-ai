import random

try:
	import entity
except ImportError:
	from back import entity


VERBOSE = False


class Model:

	def __init__(self, width, length, conf={}):
		self.width = width
		self.length = length
		self.nb_entities = conf['nb_entities']

		self.init_cells()
		self.init_life()

	def init_cells(self):
		self.turn = 0
		self.cells = {}
		self.is_complete = False

		for x in range(self.width):
			for y in range(self.length):
				c = entity.Cell(x, y)
				self.cells[(x, y)] = c

	def init_life(self):
		self.generate_cells()
		self.generate_beings()

# --------------------------------------------------------------------------

	def generate_cells(self):
		for x in range(self.width):
			for y in range(self.length):
				self.cells[(x, y)].generate()

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

	def update_cells(self):
		for x in range(self.width):
			for y in range(self.length):
				self.cells[(x, y)].update()

# --------------------------------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None


if __name__ == '__main__':
	width = 5
	length = width
	model = Model(width, length)

	for i in range(5):
		model.update()

