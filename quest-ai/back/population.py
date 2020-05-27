import random

import name
from ai.ai import *


class Population:
	def __init__(self, world, size, mutation_rate=0.2):
		self.world = world
		
		self.gen = 0
		self.size = size
		self.mutation_rate = mutation_rate

		self.create_first_settlers()

	def __str__(self):
		return '\n'.join([str(e) for e in self.entities])

# -------------------------------------------------

	def create_first_settlers(self):
		self.best_entity = None
		self.best_score_history = []
		n = name.Names()
		settlers = [AI(self.world, name=n.baptise()) for i in range(self.size)]
		self.entities = settlers

	def healthy_generation(self):
		for e in self.entities:
			if e.alive:
				return True
		return False

# -------------------------------------------------

	def run_generation(self):
		self.turn = 0
		while self.healthy_generation():
			self.update()

		print("\n\t/!\\ Population extinction /!\\\n")
		self.trigger_fitness_calculation()
		self.gen += 1
		self.natural_selection()
		# best score

# -------------------------------------------------

	def update(self):
		print(f"-- turn {self.turn} --")
		# shuffle list ??
		for e in self.entities: e.turn()
		self.turn += 1

	# not used...
	def mutate(self):
		for e in self.entities:
			e.mutate()

# -------------------------------------------------

	def trigger_fitness_calculation(self):
		print("-- trigger fitness calculation --")
		for e in self.entities:
			e.calculate_fitness()

	def natural_selection(self):
		print("\nNatural Selection")
		self.best_entity = self.get_best_entity()
		new_gen = [self.best_entity.clone()]

		for i in range(1, self.size):
			father = self.get_a_parent()
			mother = self.get_a_parent()

			child = father.crossover(mother)
			child.name = name.new_born(mother.name, father.name)
			child.mutate(self.mutation_rate)

			new_gen += [child]

		self.best_score_history += [self.best_entity.score]
		self.entities = new_gen
	
	def get_best_entity(self):
		max = 0
		best = None
		for e in self.entities:
			if e.score >= max:
				max = e.score
				best = e
		return best

	def get_a_parent(self):
		# 	get a parent from last gen
		# 		best / with fitness > (rand?) threshold / randomly ?
		minimum_score = self.best_entity.score 
		minimum_score -= minimum_score*random.random()
		print(f"minimum_score for breed : {minimum_score}")
		for e in self.entities:
			if e.score > minimum_score:
				print(f"suitor score = {e.score}")
				return e

		print("return best as default !!!!!!!")
		return self.best_entity

# -------------------------------------------------

def test():
	class World:
		def __init__(self):
			self.width = 2
			self.length = 2

	size = 2
	world = World()
	p = Population(world, size)
	p.run_generation()


if __name__ == '__main__':
	test()


