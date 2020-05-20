import random


MAX_WATER = 10
MAX_PLANT = 10

WATER_LABEL = 'water'
PLANT_LABEL = 'plant'

SPEED = 1
MAX_MOVE = 1


class Entity:
	def __init__(self, x, y, water=0):
		self.x = x
		self.y = y

		self.water = water

	def __repr__(self):
		return "{}".format(self.v)

	def __str__(self):
		return "({},{})".format(self.x, self.y)


# ---------------------------------------------------------

class Cell (Entity):
	def __init__(self, x, y):
		super().__init__(x, y)

		self.label = ''

		self.plant = 0


	def generate(self):
		self.water = random.randint(0, MAX_WATER)
		self.plant = random.randint(0, MAX_PLANT)
		self.update_label()


	def update_label(self):
		if self.water > self.plant:
			self.label = WATER_LABEL
		elif self.water < self.plant:
			self.label = PLANT_LABEL


	def reset(self):
		pass



# ---------------------------------------------------------

class Being (Entity):
	def __init__(self, u_name, x, y):
		super().__init__(x, y, water=10)

		# TODO get random unique name
		self.age = 0
		self.u_name = u_name

		self.max_move = MAX_MOVE


	def update(self):
		# self.move_random()
		# self.move_fix()
		self.age += 1


	def move_fix(self):
		self.y += 1
		pass

	def move_random(self):
		dx = random.randint(0, self.max_move)*SPEED
		dy = random.randint(0, self.max_move)*SPEED

		self.x = move(self.x, dx)
		self.y = move(self.y, dy)


def move(coord, delta_coord):
	if (coord >= delta_coord):
		coord = (coord+delta_coord) if (random.randint(0, 10) > 5) else (coord-delta_coord)
	else:
		coord += delta_coord
	return coord