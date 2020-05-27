try:
	import generic_ai
except ImportError:
	from ai import generic_ai 
	from back import entity 


class AI(generic_ai.Generic_AI, entity.Being):
	def __init__(self, world, name=None, captors=4, neurones=4, choices=5, layer=2):
		generic_ai.Generic_AI.__init__(self, captors, neurones, choices, layer)
		x, y = 0, 0
		if name: self.name = name
		entity.Being.__init__(self, self.name, x, y, world)
		
	def __str__(self):
		return entity.Being.__str__(self)

# -------------------------------------------------

	def action(self):
		near_data = self.gather_data()
		analysis = self.analyse(near_data)
		thoughts = self.think(analysis)
		choice = self.choose(thoughts)
		
		self.move(choice) if choice < 4 else self.idle()
		self.water -= 1

	def check_life(self):
		self.heath_check()

	# def gather_data(self):
	# 	pass

# -------------------------------------------------

	def move(self, direction_id):
		direction = self.pick_direction(direction_id)
		self.step(direction)

	def idle(self):
		print(f"{self} stayed idle !")

# -------------------------------------------------
	