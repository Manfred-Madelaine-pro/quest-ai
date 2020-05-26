import random

import numpy as np


VERBOSE = False


class Matrix:
	def __init__(self, nb_row, nb_col, name="Matrix"):
		self.name = name
		self.nb_row = nb_row
		self.nb_col = nb_col
		self.randomize()

# -------------------------------------------------

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

# -------------------------------------------------

	def randomize(self):
		self.matrix = {}
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				self.matrix[(r,c)] = random.uniform(-1, 1)

	def normalize(self, r, c):
		if self.matrix[(r,c)] > 1:
			self.matrix[(r,c)] = 1
		if self.matrix[(r,c)] < -1:
			self.matrix[(r,c)] = -1

# -------------------------------------------------

	def dot_product(self, mat):
		result = Matrix(self.nb_row, mat.nb_col)
		
		if mat.nb_row != self.nb_col:
			print(f"Dot product is imossible : B.row ({mat.nb_row}) != A.col({self.nb_col})")
			return result

		for i in range(self.nb_row):
			for j in range(mat.nb_col):
				sum = 0
				for k in range(self.nb_col):
					sum += self.matrix[(i,k)]*mat.matrix[(k,j)]

				result.matrix[(i,j)] = sum

		return result

# -------------------------------------------------

	def add_bias(self):
		bias = Matrix(self.nb_row, 1)
		
		for r in range(self.nb_row):
			bias.matrix[(r,0)] = self.matrix[(r,0)]
		
		# bias.matrix[(self.nb_row, 0)] = 1
		return bias

	def activate(self, mode='relu'):
		activated = Matrix(self.nb_row, self.nb_col)

		for r in range(self.nb_row):
			for c in range(self.nb_col):
				activated.matrix[(r,c)] = activation_mode(self.matrix[(r,c)], mode)
		return activated

# -------------------------------------------------

	def mutate(self, mutation_rate):
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				successful_mutation = random.random() <= mutation_rate
				if successful_mutation:
					mutation = random.gauss(0, 0.2)
					verbose_print(f"{self.name} mutate ({(r,c)}): {mutation} !")
					self.matrix[(r,c)] += mutation
					self.normalize(r, c)

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
		clone = Matrix(self.nb_row, self.nb_col)

		for r in range(self.nb_row):
			for c in range(self.nb_col):
				clone.matrix[(r,c)] = self.matrix[(r,c)]
		return clone

# -------------------------------------------------

	def to_array(self):
		array = []
		for r in range(self.nb_row):
			for c in range(self.nb_col):
				array += [self.matrix[(r,c)]]

		return array

# --------------------------------------------------------------------------

def activation_mode(val, mode):
	if mode == 'relu':
		return relu(val)
	if mode == 'sigmoid':
		return sigmoid(val)

def relu(x):
	return max(0, x)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def array_to_single_col_matrix(array):
	m = Matrix(len(array), 1)
	for i, val in enumerate(array):
		m.matrix[(i,0)] = val
	return m

verbose_print = print if VERBOSE else lambda *a, **k: None

# --------------------------------------------------------------------------


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

	print("\n----- bias -----")
	bias = child.add_bias()
	bias.name = "Bias"
	print(bias)

	print("\n----- dot product -----")
	a = Matrix(2, 3)
	a.name = "A"
	print(a)
	b = Matrix(3, 1)
	b.name = "B"
	print(b)

	res = a.dot_product(b)
	res.name = "Result"
	print(res)
	