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
		name_handler = name.Names()
		settlers = [AI(self.world, name=name_handler.baptise()) for _ in range(self.size)]
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

		print("\n\t/!\\ Generation extinction /!\\\n")
		self.trigger_fitness_calculation()
		self.gen += 1
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
		new_gen = [self.clone(self.best_entity)]

		for i in range(1, self.size):
			mother = self.get_a_parent()
			father = self.get_a_parent()
			new_gen += [self.crossover(mother, father)]

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
		for e in self.entities:
			if e.score > minimum_score:
				print(f"suitor {e.name} : score = {e.score}")
				return e

		print("return best as default !!!!!!!")
		return self.best_entity

# -------------------------------------------------
	
	def crossover(self, mother, father):
		child_name = mother.name.crossover(father.name)
		child = mother.crossover(father, child_name)
		child.mutate(self.mutation_rate)
		return child

	def clone(self, entity):
		clone_name = entity.name.clone()
		clone = entity.clone(clone_name)
		return clone


# -------------------------------------------------

def test():
	class World:
		def __init__(self):
			self.width = 2
			self.length = 2

	size = 5
	gen_max = 20
	world = World()
	p = Population(world, size)

	while p.gen < gen_max:
		p.run_generation()
		p.natural_selection()
	p.run_generation()


if __name__ == '__main__':
	test()


