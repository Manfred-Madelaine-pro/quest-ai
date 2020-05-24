import random


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

	def mutate(self):
		pass

	def crossover(self):
		pass

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


if __name__ == '__main__':
	m = Matrix(2, 5)
	print(m)
	print(f"to_array : {m.to_array()}")

	array = [i for i in range(5)]
	m = array_to_single_col_matrix(array)
	print(m)
