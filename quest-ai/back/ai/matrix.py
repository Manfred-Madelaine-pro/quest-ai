import random


VERBOSE = False


class Matrix:
	def __init__(self, nb_row, nb_col, name="Matrix"):
		self.name = name
		self.nb_row = nb_row
		self.nb_col = nb_col
		self.randomize()

	def __str__(self):
		title = f"\t{self.name} ({self.nb_row}, {self.nb_col})"

		mat = ''
		for r in range(self.nb_row):
			mat += '\n'
			for c in range(self.nb_col):
				mat += '{:8}'.format(round(self.matrix[(r,c)], 3))
		return title + mat

	def get_lines_str(self):
		lines_str = []
		for r in range(self.nb_row):
			lines_str.append([])
			line = ''
			for c in range(self.nb_col):
				line += '{:^8}'.format(round(self.matrix[(r,c)], 3))
			lines_str[r] += [line]
		return lines_str


	def randomize(self):
		self.matrix = {}
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				self.matrix[(r,c)] = random.uniform(-1, 1)


	def dot_product(self):
		pass

	def output(self):
		pass

	def add_bias(self):
		pass


	def activate(self):
		pass

	def mutate(self, mutation_rate):
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				successful_mutation = random.random() <= mutation_rate
				if successful_mutation:
					mutation = random.gauss(0, 0.2)
					verbose_print(f"{self.name} mutate ({(r,c)}): {mutation} !")
					self.matrix[(r,c)] += mutation
					self.normalize(r, c)

	def normalize(self, r, c):
		if self.matrix[(r,c)] > 1:
			self.matrix[(r,c)] = 1
		if self.matrix[(r,c)] < -1:
			self.matrix[(r,c)] = -1


	def crossover(self, partner):
		child = Matrix(self.nb_row, self.nb_col)

		rand_r = random.randint(0, self.nb_row-1)
		rand_c = random.randint(0, self.nb_col-1)

		verbose_print(f"crossover limit : {(rand_r,rand_c)}")
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				if r <= rand_r and c <= rand_c:
					child.matrix[(r,c)] = self.matrix[(r,c)]
				else:
					child.matrix[(r,c)] = partner.matrix[(r,c)]

		return child


	def clone(self):
		pass

	def to_array(self):
		array = []
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				array += [self.matrix[(r,c)]]

		return array


def array_to_single_col_matrix(array):
	m = Matrix(len(array), 1)
	for i, val in enumerate(array):
		m.matrix[(i,0)] = val
	return m


# --------------------------------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None


if __name__ == '__main__':
	print("\n----- mutation -----")
	m = Matrix(2, 5)
	print(m)
	m.mutate(0.5)
	m.name = "Mutated"
	print(m)

	print("\n----- crossover -----")
	father = Matrix(2, 5, 'Father')
	print(father)
	mother = Matrix(2, 5, 'Mother')
	print(mother)
	child = father.crossover(mother)
	child.name = 'Child'
	print(child)
