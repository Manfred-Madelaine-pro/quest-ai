try:
	import generic_ai
except ImportError:
	from ai import generic_ai 
	from back import entity 


class AI(generic_ai.Generic_AI, entity.Being):
	def __init__(self, world, name=None, captors=4, neurones=4, choices=5, layer=2):
		generic_ai.Generic_AI.__init__(self, captors, neurones, choices, layer)
		x, y = 0, 0
		entity.Being.__init__(self, self.name, x, y, world)
		if name:
			self.name = name
		

# -------------------------------------------------

	def action(self):
		print(f"{self.name} action !")

	def gather_data(self):
		pass

	def move_around(self):
		pass

# -------------------------------------------------
	