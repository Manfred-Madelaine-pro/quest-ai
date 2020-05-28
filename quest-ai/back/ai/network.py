
try:
	import matrix
except ImportError:
	from ai import matrix 


VERBOSE = __name__ != '__main__'


class Network:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, hidden_layers):
		self.input_nodes  = input_nodes

		self.hidden_layers = hidden_layers
		self.hidden_nodes = hidden_nodes
		
		self.output_nodes = output_nodes

		self.create_weights()

	def __str__(self):
		net = ''
		for w in self.weights:
			net += str(w) + '\n'

		return net

# -------------------------------------------------

	def create_weights(self):
		self.weights = []
		for i in range(self.hidden_layers+1):
			layer_name = self.get_layer_name(i)

			row = self.output_nodes if (i == self.hidden_layers) else self.hidden_nodes
			col = self.input_nodes if (i == 0) else self.hidden_nodes
			
			# weights = [(hidden, input), (hidden, hidden), ..., (output, hidden)]
			self.weights += [matrix.Matrix(row, col, layer_name + " Weights")]

	def get_layer_name(self, layer_id):
		name = 'Input' if (layer_id == 0) else 'Hidden'
		return name if (layer_id != self.hidden_layers) else 'Output' 

# -------------------------------------------------

	def analyse(self, input_array):
		input_matrix = matrix.array_to_single_col_matrix(input_array)
		input_matrix.name = "Input Array"
		verbose_print(input_matrix)
		bias = input_matrix.add_bias()

		for i in range(self.hidden_layers):
			hidden_input = self.weights[i].dot_product(bias).activate()
			bias = hidden_input.add_bias()

		output = self.weights[-1].dot_product(bias)
		output = output.activate(mode='sigmoid')
		output.name = "Output Array"
		verbose_print(output)
		return output.to_array()

# -------------------------------------------------

	def mutate(self, mutation_rate):
		for w in self.weights:
			w.mutate(mutation_rate)

	def crossover(self, partner):
		child = Network(self.input_nodes, self.hidden_nodes, self.output_nodes, self.hidden_layers)
		for i, w in enumerate(self.weights):
			child.weights[i] = w.crossover(partner.weights[i])
		return child

	def clone(self):
		clone = Network(self.input_nodes, self.hidden_nodes, self.output_nodes, self.hidden_layers)
		for i, w in enumerate(self.weights):
			clone.weights[i] = w.clone()
		return clone

# -------------------- Display -----------------------------

def print_network(nn):
	network = create_network(nn)
	horizontal_print(network)

def create_network(nn):
	network = []
	layer_template = "[{}]"
	# Input nodes | mat_hw_1 | Hidden nodes 1 | mat_hw_i | Hidden nodes i | mat_hw_n | Output nodes 
	input_nodes = matrix.array_to_single_col_matrix([0 for x in range(nn.input_nodes)])
	input_nodes.name = layer_template.format("Input")
	network += [input_nodes]

	for i in range(nn.hidden_layers+1):
		mat_hw_i = nn.weights[i]
		network += [mat_hw_i]

		nb_nodes = nn.hidden_nodes if (i < nn.hidden_layers) else nn.output_nodes
		array = [0 for x in range(nb_nodes)]
		
		hidden_nodes_i = matrix.array_to_single_col_matrix(array)
		if (i < nn.hidden_layers):
			hidden_nodes_i.name = layer_template.format(f"Hidden {i+1}")
		else:
			hidden_nodes_i.name = layer_template.format("Output")

		network += [hidden_nodes_i]
	
	return network
	
def horizontal_print(network):
	merged = []
	for layer in network:
		if len(merged) == 0:
			merged += [[]]
		merged[0] += [layer.name]

		lines = layer.get_lines_str()
		for r, line in enumerate(lines):
			if len(merged) <= r+1:
				merged += [[]]
			merged[r+1] += line
		
		for i in range(len(lines)+1, len(merged)):
			merged[i] += [' ']

	for c in range(len(merged[0])):
		size = 0
		for r in range(len(merged)):
			if len(merged[r][c]) > size:
				size = len(merged[r][c])
			if merged[r][c] == ' ':
				merged[r][c] = ' '*size

		if (size - len(merged[0][c])) > 1:
			tab = ' '*int((size - len(merged[0][c]))/2)
			merged[0][c] = tab + merged[0][c] + tab

	matr = ''
	for _, r in enumerate(merged):
		matr += '\n' if _ > 0 else ''
		for c in r:
			matr += '{:^14}'.format(c)
	verbose_print(matr)

# -------------------------------------------------

def mutate_and_crossover():
	input, output = 4, 3
	hidden, layers = 2, 2	

	nn = Network(input, hidden, output, layers)
	print_network(nn)

	tab = '\t'*6
	verbose_print(f"{tab}----- mutation -----\n")
	nn.mutate(0.5)
	print_network(nn)

	verbose_print(f"{tab}----- crossover -----\n")
	mother = Network(input, hidden, output, layers)
	print_network(mother)

	child = nn.crossover(mother)
	print_network(child)


verbose_print = print if VERBOSE else lambda *a, **k: None

# -------------------------------------------------

if __name__ == '__main__':
	input, output = 4, 3
	hidden, layers = 2, 2	

	nn = Network(input, hidden, output, layers)
	print_network(nn)

	tab = '\t'*6
	verbose_print(f"{tab}----- output -----\n")
	input_array = [i for i in range(4)]
	nn.analyse(input_array)
