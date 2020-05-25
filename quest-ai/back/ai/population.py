import random

import entity


class Population:
	def __init__(self, size):
		self.gen = 0
		self.size = size
		self.mutation_rate = 0.2

		self.create_entities()

	def __str__(self):
		return '\n'.join([str(e) for e in self.entities])

# -------------------------------------------------

	def create_entities(self):
		self.entities = []
		self.best_entity = None
		self.best_score_history = []

		for i in range(self.size):
			self.entities += [entity.Entity()]

	def have_living_beings(self):
		for e in self.entities:
			if e.alive:
				return True
		return False

# -------------------------------------------------

	def update(self):
		# shuffle list ??
		for e in self.entities:
			e.turn()

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
			child = self.get_a_parent().crossover(self.get_a_parent())
			child.mutate(self.mutation_rate)
			new_gen += [child]

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
		print(f"minimum_score for breed : {minimum_score}")
		for e in self.entities:
			print(f"suitor score = {e.score}")
			if e.score > minimum_score:
				return e

		print("return best as default !!!!!!!")
		return self.best_entity

# -------------------------------------------------


if __name__ == '__main__':
	p = Population(2)

	turn = 0
	while p.have_living_beings():
		print(f"-- turn {turn} --")
		p.update()
		turn += 1

	print("\n\t/!\\ Population extinction /!\\\n")
	p.trigger_fitness_calculation()
	p.natural_selection()

	# best score

