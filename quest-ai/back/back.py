import random

try:
	import entity
	import population
except ImportError:
	from back import entity
	from back import population


VERBOSE = __name__ != '__main__'


class GenericGrid:
	def __init__(self, width, length):
		self.width = width
		self.length = length
		self.init_cells()

	def __str__(self):
		title = f"\tGrid ({self.width}, {self.length})"
		grid = ''
		for x in range(self.width):
			if len(grid) > 0 : grid += '\n'
			for y in range(self.length):
				grid += '{:5}'.format(self.cells[(x, y)].water)

		return grid + title

	def init_cells(self):
		self.cells = {}
		for x in range(self.width):
			for y in range(self.length):
				c = entity.Cell(x, y)
				self.cells[(x, y)] = c

	def generate_cells(self):
		for x in range(self.width):
			for y in range(self.length):
				self.cells[(x, y)].generate()

	def update_cells(self):
		for x in range(self.width):
			for y in range(self.length):
				self.cells[(x, y)].update()

	def out_of_boud(self, x, y):
		return (x < 0 or x >= self.width) or (y < 0 or y >= self.length)

# --------------------------------------------------------------------------

class Model(GenericGrid):
	def __init__(self, width, length, conf={}):
		super().__init__(width, length)
		self.population_size = conf['nb_entities'] if conf else 2
		self.init_life()

	def init_cells(self):
		self.is_livingful = True
		super().init_cells()

	def init_life(self):
		self.generate_cells()
		self.population = population.Population(self, self.population_size)

# --------------------------------------------------------------------------

	def start(self):
		self.is_livingful = True

	def stop(self):
		verbose_print("End Simulation.")
		self.is_livingful = False

	def update(self):
		verbose_print(f'\t-- Generation : {self.population.gen} --')
		# verbose_print(self)
		self.population.update()
		# update grid : rain

	def next_generation(self):
		self.population.next()
		self.generate_cells()
		# self.stop()


# --------------------------------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None

def test_Model():
	width = 10
	conf = {'nb_entities': 3}
	model = Model(width, width, conf=conf)

	max_gen = 10
	while model.population.gen < max_gen:
		model.update()
	model.next_generation()

	model.population.print_history()
	print(model.population.best_score_history)
	m = max(model.population.best_score_history)
	print(model.population.best_entity, model.population.best_entity.year, 'VS', m)

	# graph
	import numpy as np
	from matplotlib import pyplot as plt
	plt.style.use('seaborn-darkgrid')

	def plot_sorted_curve(x, total):
		tab = f'{"-"*20}\n'
		txt =  f'min: {min(x)}\n'
		txt += f'max: {max(x)}\n'
		txt += f'range: {np.ptp(x)}\n'
		txt += tab
		txt += f'mean: {np.mean(x):.2f}\n'
		txt += f'median : {np.median (x)}\n'
		txt += tab
		txt += f'sum: {np.sum(x)}\n'
		txt += f'var: {np.var(x):.2f}\n'
		txt += f'std: {np.std(x):.2f}\n'


		f = plt.figure('Best score per generation')
		plt.plot(x)

		plt.title(f"Population's best score for each generation (total gen={total})")
		plt.ylabel("Best score")
		plt.xlabel("Generation")

		plt.text(0.05, 0.95, txt, 
			ha='left', va='top', fontsize=12, 
			transform=plt.gca().transAxes,
			bbox=dict(facecolor='white', alpha=0.5))
		plt.show()
		# Add some stats


	plot_sorted_curve(model.population.best_score_history, model.population.gen)


if __name__ == '__main__':
	test_Model()

