import random

import network

class Entity:
	def __init__(self, layer=2):
		self.score = 0
		
		self.year = 0
		self.alive = True
		
		self.name = random.choice([f"ent-{i}" for i in range(20)])

		self.layer = layer
		self.brain = network.Network(4, 4, 4, self.layer)

	def __str__(self):
		return f"{self.name}"

# -------------------------------------------------

	def turn(self):
		print(f"{self} play turn !")
		self.year += 1
		self.check_life()

	def check_life(self):
		if self.year > 2 :
			self.alive = False

# -------------------------------------------------

	def action(self):
		vision_array = []
		# predict best action ?
		self.brain.predict(vision_array)

# -------------------------------------------------

	def mutate(self, mutation_rate):
		print(f"{self} mutate !")
		self.brain.mutate(mutation_rate)

	def crossover(self, parent):
		e = Entity(self.layer)
		e.brain = self.brain.crossover(parent.brain)
		return e

	def clone(self):
		e = Entity(self.layer)
		e.brain = self.brain.clone()
		return e

# -------------------------------------------------

	def calculate_fitness(self):
		self.score += self.year*random.random()
		print(f"{self} fitness = {round(self.score, 4)}")

# -------------------------------------------------


if __name__ == '__main__':
	e = Entity()
	print(e)
