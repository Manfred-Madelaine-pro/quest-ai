import random

try:
	import network
except ImportError:
	from back import entity
	try:
		from ai import network
	except ImportError:
		from back.ai import network


VERBOSE = __name__ == '__main__'


class GenericAI:
	def __init__(self, captors=4, neurones=4, choices=5, layer=2):
		self.score = 0
		
		self.year = 0
		self.alive = True
		
		self.name = random.choice([f"ent-{i}" for i in range(20)])

		self.layer = layer
		self.captors = captors
		self.brain = network.Network(captors, neurones, choices, self.layer)

	def __str__(self):
		return f"{self.name}"

# -------------------------------------------------

	def turn(self):
		if not self.alive:
			return 
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
		return self.act(choice)

	def gather_data(self):
		collected_data = [random.random() for _ in range(self.captors)]
		# predict best action ?
		return collected_data

# -------------------------------------------------

	def analyse(self, data):
		return self.brain.analyse(data)

	def think(self, thoughts):
		''' 
			GenericAI's thoughts become its options, they then become potential choices
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
			verbose_print(f"\t{self.name} is facing a dilemma !")
			return random.choice(choices)
		return choices[0]

# -------------------------------------------------

	def act(self, choice):
		switch_case = {
        	0 : self.up,
        	1 : self.down,
        	2 : self.left,
        	3 : self.right,
        	4 : self.idle
        }
		switch_case.get(choice, self.idle)()

	def up(self):
		verbose_print("move up !")
	def down(self):
		verbose_print("move down !")
	def left(self):
		verbose_print("move left !")
	def right(self):
		verbose_print("move right !")
	def idle(self):
		verbose_print("stay idle !")

# -------------------------------------------------

	def mutate(self, mutation_rate):
		verbose_print(f"{self} mutate !")
		self.brain.mutate(mutation_rate)

	def crossover(self, parent):
		ai = GenericAI(self.layer)
		ai.brain = self.brain.crossover(parent.brain)
		return ai

	def clone(self):
		ai = GenericAI(self.layer)
		ai.brain = self.brain.clone()
		return ai

# -------------------------------------------------

	def calculate_fitness(self):
		self.score += self.year*1
		verbose_print(f"{self.name} : fitness = {round(self.score, 4)}")

# -------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None


if __name__ == '__main__':
	captors = 8
	neurones = 10
	choices = 5
	layer = 2
	ai = GenericAI(captors, neurones, choices, layer)
	print(ai)

	ai.action()
