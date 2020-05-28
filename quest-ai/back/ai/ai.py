import operator
from functools import reduce

try:
	import generic_ai
except ImportError:
	from ai import generic_ai 
	from back import entity 


VERBOSE = __name__ == '__main__'

# TODO clean

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (0,1)
CURRENT = (0,0)

SELF_AWARENESS = ['pos_x', 'pos_y', 'water_lvl']
VISIONS = [UP, DOWN, CURRENT, LEFT, RIGHT]
CAPTORS_TYPE = ['water']

CONSCIOUSNESS = SELF_AWARENESS
CONSCIOUSNESS += reduce(lambda x, y: x+y, [list(map(lambda v: f"{v}: {c}", VISIONS)) for c in CAPTORS_TYPE])


CAPTORS = len(CONSCIOUSNESS)
CHOICES = len(VISIONS) + len(CAPTORS_TYPE)
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
		consumed = generic_ai.GenericAI.action(self)
		self.water -= consumed

	def act(self, choice):
		possible_actions = {
        	0 : self.up,
        	1 : self.down,
        	2 : self.left,
        	3 : self.right,
        	4 : self.idle,
        	5 : self.drink,
    	}
		if choice < 4 :
			return self.move(choice)
		return possible_actions.get(choice, self.idle)()

# -------------------------------------------------

	def gather_data(self):
		self_awareness = [self.x, self.y, self.water]
		surroundings_data = self.inspect_surroundings()
		return self_awareness + surroundings_data

	def inspect_surroundings(self):
		surroundings = []
		for vision in VISIONS:
			neighbourg = tuple(map(operator.add, (self.x, self.y), vision))
			if not self.world.out_of_boud(*neighbourg):
				surroundings += [self.world.cells[neighbourg].water]
			else:
				surroundings += [0]
		return surroundings

# -------------------------------------------------

	def move(self, direction_id):
		direction = self.pick_direction(direction_id)
		self.step(direction)
		return 1


	def idle(self):
		verbose_print(f"{self} stayed idle !")
		return 1

	def drink(self):
		return entity.Being.drink(self)


# -------------------------------------------------
	
	def crossover(self, parent, ai_name):
		ai = AI(self.world, name=ai_name)
		ai.brain = self.brain.crossover(parent.brain)
		return ai

	def clone(self, name):
		clone = AI(self.world, name=name)
		clone.brain = self.brain.clone()
		return clone



verbose_print = print if VERBOSE else lambda *a, **k: None
