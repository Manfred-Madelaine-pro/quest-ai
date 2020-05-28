
try:
	import matrix
except ImportError:
	from ai import matrix 


def store_values_in_grid(*args):
	grid = []
	titles = []
	max_row = max([mat.nb_row for mat in args])

	for mat in args:
		titles += [f"{mat.name} ({mat.nb_row}, {mat.nb_col})"]
		lines = mat.get_lines_str()

		for r in range(max_row):
			if r >= len(grid):
				grid += [[]]
			grid[r] += lines[r] if (r < len(lines)) else [' '*8]

	return [titles] + grid

def h_arrangement(*args):
	grid = store_values_in_grid(*args)
	return to_string(grid)


def to_string(grid):
	txt = ''
	for row in grid:
		if len(txt) > 0 : txt += '\n'
		for cell in row:
			txt += '{:^15}'.format(cell)

	return txt

# -------------------------------------------------

def test(input, output):
	input_array = [i for i in range(input)]
	output_array = [i for i in range(output)]

	input_matrix = matrix.array_to_single_col_matrix(input_array)
	output_matrix = matrix.array_to_single_col_matrix(output_array)

	print(h_arrangement(input_matrix, output_matrix))

# -------------------------------------------------

if __name__ == '__main__':
	test_args = [(3, 3), (10, 5), (5, 10)]
	# test_args = [(2, 3)]
	for args in test_args:
		test(*args)