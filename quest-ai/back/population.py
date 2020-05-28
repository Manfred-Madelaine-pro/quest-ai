import random

import name
from ai.ai import *


VERBOSE = __name__ == '__main__'


class Population:
	def __init__(self, world, size, mutation_rate=0.2):
		self.world = world
		
		self.size = size
		self.mutation_rate = mutation_rate

		self.create_first_settlers()

	def __str__(self):
		return '\n'.join([str(e) for e in self.entities])

# -------------------------------------------------

	def create_first_settlers(self):
		self.gen = 0
		self.best_entity = None
		self.best_score_history = []
		name_handler = name.Names()
		settlers = []
		for _ in range(self.size):
			settlers += [AI(self.world, name=name_handler.baptise())]
		self.entities = settlers

	def healthy_generation(self):
		for e in self.entities:
			if e.alive:
				return True
		return False

# -------------------------------------------------

	def run_generation(self):
		self.turn = 0
		self.entities_drop_on_world()

		while self.healthy_generation():
			self.update()

		verbose_print("\n\t/!\\ Generation extinction /!\\\n")
		self.trigger_fitness_calculation()
		# best score

	def entities_drop_on_world(self):
		for e in self.entities:
			e.x, e.y = self.get_random_pos()

	def get_random_pos(self):
		x = random.randint(0, self.world.width-1)
		y = random.randint(0, self.world.length-1)
		return x, y

# -------------------------------------------------

	def update(self):
		verbose_print(f"-- turn {self.turn} --")
		# shuffle list ??
		for e in self.entities: 
			e.turn()
			verbose_print('')
		self.turn += 1

	# not used...
	def mutate(self):
		for e in self.entities:
			e.mutate()

# -------------------------------------------------

	def trigger_fitness_calculation(self):
		verbose_print("-- trigger fitness calculation --")
		for e in self.entities:
			e.calculate_fitness()

	def natural_selection(self):
		verbose_print("\nNatural Selection")
		self.best_entity = self.get_best_entity()
		new_gen = [self.clone(self.best_entity)]

		for i in range(1, self.size):
			mother = self.get_a_parent()
			father = self.get_a_parent()
			new_gen += [self.crossover(mother, father)]

		self.best_score_history += [self.best_entity.score]
		self.entities = new_gen
		self.gen += 1
	
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
				verbose_print(f"suitor {e.name} : score = {e.score}")
				return e

		verbose_print("return best as default !!!!!!!")
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
	from back import GenericGrid 

	width = 5
	world = GenericGrid(width, width)

	pop_size = 10
	gen_max = 10
	p = Population(world, pop_size)

	while p.gen < gen_max:
		verbose_print(world, "Gen: ", p.gen)
		p.run_generation()
		p.natural_selection()

# -------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None


if __name__ == '__main__':
	test()


