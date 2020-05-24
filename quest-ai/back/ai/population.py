import entity

class Population:
	def __init__(self, size):
		self.gen = 0
		self.size = size
		self.entities = []
		self.best_entity = None

		self.best_score_history = []

		for i in range(size):
			self.entities += [entity.Entity()]


	def __str__(self):
		return '\n'.join([str(e) for e in self.entities])


	def update(self):
		# shuffle list ??
		for e in self.entities:
			e.turn()

	# ???
	def mutate(self):
		for e in self.entities:
			e.mutate()

	def trigger_fitness_calculation(self):
		print("-- trigger fitness calculation --")
		for e in self.entities:
			e.calculate_fitness()

	def have_living_beings(self):
		for e in self.entities:
			if e.alive:
				return True
		return False

	def get_a_parent(self):
		# 	get a parent from last gen
		# 		best / with fitness > (rand?) threshold / randomly ?
		return self.best_entity

	def natural_selection(self):
		print("\nNatural Selection")
		self.best_entity = self.get_best_entity()
		new_gen = []

		# save best in new gen
		new_gen += [self.best_entity]

		# complete remaining slots with mutated ent
		for i in range(1, self.size):
			# crossocer with another parent ?
			child = self.get_a_parent().crossover(self.get_a_parent())
			child.mutate()
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

