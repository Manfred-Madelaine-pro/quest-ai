from functools import reduce

try:
	import generic_ai
except ImportError:
	from ai import generic_ai 
	from back import entity 


SELF_AWARENESS = ['pos_x', 'pos_y', 'water_lvl']
VISION = ['up', 'down', 'current', 'left', 'right']
CAPTORS_TYPE = ['water']

CONSCIOUSNESS = SELF_AWARENESS
CONSCIOUSNESS += reduce(lambda x, y: x+y, [list(map(lambda v: f"{c} {v}", VISION)) for c in CAPTORS_TYPE])


CAPTORS = len(CONSCIOUSNESS)
CHOICES = len(VISION) + len(CAPTORS_TYPE)
NEURONES = 10
LAYER = 2


class AI(generic_ai.GenericAI, entity.Being):
	def __init__(self, world, x=0, y=0, name=None, 
			captors=CAPTORS, neurones=NEURONES, choices=CHOICES, layer=LAYER):
		generic_ai.GenericAI.__init__(self, captors, neurones, choices, layer)
		
		if name: self.name = name
		entity.Being.__init__(self, self.name, x, y, world)
		
	def __str__(self):
		return entity.Being.__str__(self)

# -------------------------------------------------

	def check_life(self):
		self.heath_check()

# -------------------------------------------------

	def action(self):
		near_data = self.gather_data()
		analysis = self.analyse(near_data)
		thoughts = self.think(analysis)
		choice = self.choose(thoughts)
		
		self.move(choice) if choice < 4 else self.idle()
		self.water -= 1

	def act(self, choice):
		possible_actions = {
        	0 : self.up,
        	1 : self.down,
        	2 : self.left,
        	3 : self.right,
        	4 : self.idle,
        	5 : self.drink,
    	}
		possible_actions.get(choice, self.idle)()

	def gather_data(self):
		# print(self.world)

		collected_data = [_ for _ in range(self.captors)]
		# predict best action ?
		return collected_data

# -------------------------------------------------

	def move(self, direction_id):
		direction = self.pick_direction(direction_id)
		self.step(direction)

	def idle(self):
		print(f"{self} stayed idle !")

	def drink(self):
		print(f"{self} drank {'!'*10}")

# -------------------------------------------------
	
	def crossover(self, parent, ai_name):
		ai = AI(self.world, name=ai_name)
		ai.brain = self.brain.crossover(parent.brain)
		return ai

	def clone(self, name):
		clone = AI(self.world, name=name)
		clone.brain = self.brain.clone()
		return clone
