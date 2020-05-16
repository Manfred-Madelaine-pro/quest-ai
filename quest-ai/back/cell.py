import random


MAX_WATER = 10
MAX_PLANT = 10

WATER_LABEL = 'water'
PLANT_LABEL = 'plant'


class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.label = ''

		self.water = 0
		self.plant = 0

	def __repr__(self):
		return "{}".format(self.v)

	def __str__(self):
		return "({},{})".format(self.x, self.y)


	def generate(self):
		self.water = random.randint(0, MAX_WATER)
		self.plant = random.randint(0, MAX_PLANT)
		self.update_label()


	def update_label(self):
		if self.water > self.plant:
			self.label = WATER_LABEL
		elif self.water < self.plant:
			self.label = PLANT_LABEL


	def update(self):
		pass

	def reset(self):
		pass