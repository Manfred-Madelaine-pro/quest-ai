import random

import network

class AI:
	def __init__(self, world, captors=4, neurones=4, choices=5, layer=2):
		self.score = 0
		
		self.year = 0
		self.alive = True
		
		self.name = random.choice([f"ent-{i}" for i in range(20)])

		self.layer = layer
		self.captors = captors
		self.brain = network.Network(captors, neurones, choices, self.layer)

		self.world = world

	def __str__(self):
		return f"{self.name}"

# -------------------------------------------------

	def turn(self):
		print(f"{self} play turn !")
		self.action()

		self.year += 1
		self.check_life()

	def check_life(self):
		# TODO check for out of bound 
		if self.year > 2 :
			self.alive = False

# -------------------------------------------------

	def action(self):
		near_data = self.gather_data()
		analysis = self.analyse(near_data)
		thoughts = self.think(analysis)
		choice = self.choose(thoughts)
		self.act(choice)

	def gather_data(self):
		collected_data = [random.random() for _ in range(self.captors)]
		# predict best action ?
		return collected_data

# -------------------------------------------------

	def analyse(self, data):
		return self.brain.analyse(data)

	def think(self, thoughts):
		''' 
			AI's thoughts become its options, they then become potential choices
			to eventually turn into actions.
		'''
		best, options = self.best_options(thoughts)
		return self.filter(best, options)

	def best_options(self, thoughts):
		def rank(item):
			return item[1]

		# enumerate all options
		options = dict(enumerate(thoughts))

		# sort options by rank 
		ordered_options = dict(sorted(options.items(), key=rank, reverse=True))
		best = next(iter(ordered_options.values()))
		return best, ordered_options
		
	def filter(self, best, options):
		def get_best_choices(options, best):
		    return [choice for choice, opt in options.items() if opt == best]

		return get_best_choices(options, best)

# -------------------------------------------------

	def choose(self, choices):
		# handle indecision
		if len(choices) > 1:
			print(f"{self} is facing a dilemma !")
			return random.choice(choices)
		return choices[0]

# -------------------------------------------------

	def act(self, choice):
		switch_case = {
          0 : self.idle,
          1 : self.up,
          2 : self.down,
          3 : self.left,
          4 : self.right
        }
		switch_case.get(choice, self.idle)()

	def up(self):
		print("move up !")
	def down(self):
		print("move down !")
	def left(self):
		print("move left !")
	def right(self):
		print("move right !")
	def idle(self):
		print("stay idle !")

# -------------------------------------------------

	def mutate(self, mutation_rate):
		print(f"{self} mutate !")
		self.brain.mutate(mutation_rate)

	def crossover(self, parent):
		e = AI(self.layer)
		e.brain = self.brain.crossover(parent.brain)
		return e

	def clone(self):
		e = AI(self.layer)
		e.brain = self.brain.clone()
		return e

# -------------------------------------------------

	def calculate_fitness(self):
		self.score += self.year*random.random()
		print(f"{self} fitness = {round(self.score, 4)}")

# -------------------------------------------------


if __name__ == '__main__':
	captors = 8
	neurones = 10
	choices = 5
	layer = 2
	ai = AI(captors, neurones, choices, layer)
	print(ai)

	ai.action()
