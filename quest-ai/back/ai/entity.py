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

	def turn(self):
		print(f"{self} play turn !")
		
		self.year += 1
		self.score += self.year*random.random()

		self.check_life()

	def check_life(self):
		if self.year > 2 :
			self.alive = False

	def mutate(self):
		print(f"{self} mutate !")
		self.brain.mutate()

	def calculate_fitness(self):
		print(f"{self} fitness = {round(self.score, 4)}")

	def clone(self):
		e = Entity(self.layer)
		e.brain = self.brain.clone()
		return e

	def crossover(self, parent):
		e = Entity(self.layer)
		e.brain = self.brain.crossover(parent)
		return e


if __name__ == '__main__':
	e = Entity()
	print(e)
