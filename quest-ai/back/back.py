import random

try:
	import entity
except ImportError:
	from back import entity


class Model:

	def __init__(self, width, length):
		global WIDTH
		global LENGTH

		WIDTH = width
		LENGTH = length

		self.init_cells()
		self.init_life()


	def init_cells(self):
		self.cells = {}
		self.is_complete = False

		for x in range(WIDTH):
			for y in range(LENGTH):
				c = entity.Cell(x, y)
				self.cells[(x, y)] = c


	def init_life(self):
		self.generate_cells()
		self.generate_beings()


# --------------------------------------------------------------------------

	def generate_cells(self):
		for x in range(WIDTH):
			for y in range(LENGTH):
				self.cells[(x, y)].generate()


	def generate_beings(self):
		self.beings = {}
		self.dead_names = []

		for i in range(3):
			x, y = self.get_random_pos()
			self.beings[i] = entity.Being(i, x, y)


	def get_random_pos(self):
		x = random.randint(0, WIDTH)
		y = random.randint(0, LENGTH)
		return x, y

# --------------------------------------------------------------------------

	def start(self):
		self.is_complete = False

	def stop(self):
		print("End Simulation.")
		self.is_complete = True

	def update(self):
		self.remove_beings()
		self.dead_names = []

		self.update_beings()
		# self.update_cells() TODO


# --------------------------------------------------------------------------

	def update_beings(self):
		for being in self.beings.values():
			being.update()

			if self.out_of_bound(being):
				self.save_dead_being(being)

	def out_of_bound(self, being):
		return being.x/3 > WIDTH or being.y/3 > LENGTH

	def save_dead_being(self, being):
		self.dead_names += [being.u_name]

	def remove_beings(self):
		for name in self.dead_names:
			dead = self.beings.pop(name)
			
			print(f"{dead.u_name} ({dead.x}, {dead.y}) died at the age of {dead.age}!")


# --------------------------------------------------------------------------

	def update_cells(self):
		# TODO
		# update water (specific pattern)
		# update food

		for x in range(WIDTH):
			for y in range(LENGTH):
				self.cells[(x, y)].update()