import matrix

class Network:
	def __init__(self, input_nodes, hidden_nodes, output_nodes, hidden_layers):
		self.input_nodes  = input_nodes

		self.hidden_layers = hidden_layers
		self.hidden_nodes = hidden_nodes
		
		self.output_nodes = output_nodes

		self.weights = []
		for i in range(self.hidden_layers+1):
			name = 'Input' if (i == 0) else 'Hidden'
			if (i == self.hidden_layers):
				name = 'Output' 

			row = self.output_nodes if (i == self.hidden_layers) else self.hidden_nodes
			col = self.input_nodes if (i == 0) else self.hidden_nodes
			self.weights += [matrix.Matrix(row, col, name + " Weights")]
			# weight_matrix = (hidden, input)
			# weight_matrix = (hidden, hidden)
			# ...
			# weight_matrix = (output, hidden)


	def __str__(self):
		net = ''
		for w in self.weights:
			net += str(w) + '\n'

		return net


# -------------------------------------------------

def print_network(nn, vertical=False):
	network = create_network(nn)
	if vertical:
		vertical_print(network)
	else:
		herizontal_print(network)

def create_network(nn):
	network = []
	# Input nodes | mat_hw_1 | Hidden nodes 1 | mat_hw_i | Hidden nodes i | mat_hw_n | Output nodes 
	input_nodes = matrix.array_to_single_col_matrix([0 for x in range(nn.input_nodes)])
	input_nodes.name = "Input"
	network += [input_nodes]

	for i in range(nn.hidden_layers+1):
		mat_hw_i = nn.weights[i]
		network += [mat_hw_i]

		nb_nodes = nn.hidden_nodes if (i < nn.hidden_layers) else nn.output_nodes
		array = [0 for x in range(nb_nodes)]
		
		hidden_nodes_i = matrix.array_to_single_col_matrix(array)
		hidden_nodes_i.name = f"H. Layer {i+1}" if (i < nn.hidden_layers) else "Output"
		network += [hidden_nodes_i]
	
	return network
	
def vertical_print(network):
	for layer in network:
		print(layer)

def herizontal_print(network):
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
	print(matr)


# -------------------------------------------------

if __name__ == '__main__':
	input = 4
	hidden = 2
	output = 3
	layers = 2

	nn = Network(input, hidden, output, layers)

	print_network(nn)
