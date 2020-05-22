'''

----- Population ----
	best score
	gen
	best id

	update
		update all the entities for the turn 

	best entity
		conpare fitness & save best entity's id

	natural selection
		get best ent
		create new gen list
		save best in new gen
		complete remaining slots with mutated ent
			get a parent from last gen
				best / with fitness > (rand?) threshold / randomly ?
			crossocer with another parent 
			mutate resulting child
			add child in gen

		keep track of best score to print
		gen +=1 



	mutate

	calculateFitness


----- Entity ----
	init
		brain = new NeuralNet(24, HIDDEN_NODES, 4, layer);

	clone 
		Snake clone = new Snake(HIDDEN_LAYERS);
		clone.brain = brain.clone();

	cross
		Snake child = new Snake(HIDDEN_LAYERS);
	    child.brain = brain.crossover(parent.brain);

	mute
		brain.mutate(mutationRate); 

	calculate fitness
		years old

	turn
		look arround
			collect near cell's data (4 adjacents / 8 nearest / 2 cells away...)
				collect data (tupple Delta Direction)
					current pos + delta
					return [all data]
				water lvl
				is out of border ?

				next nearest cell algo ?
					pos initial + direction * vision 
					until vision = 0
		process
			decision = brain.output(vision); <-----------------------------
			
			get max output id
			map id to action

		action
		idle / direction / drink



----- Network ----
	nb input  nodes = 2*4 (mur, water)
	nb hidden nodes = ?
	nb output nodes = 5 (idle, direction)


	creation des poids (et les biais ?)
		Liste de matrices de taille n = nb hidden + 1
			0 : Matrice input (hidden x input)
			...
			i : Matrice hidden (hidden x hidden)
			...
			n : Matrice output (output x hidden)

		randomize all matrices in list

	mutate (mutation rate)
		mutate all weight matrices using mutation rate 

	!!!!!
	output (input array)
		convert input array to matrix
		add biais and store it in curr_biais
			get biaises ??
		loop over all layers' wheight except last
			dot product of weight and biaises => for each row multiply by biais
			activate resulting matrice
			add biais and store it curr_biais
		
		dot product with last weight and curr biais
		activate result
		return output as an array


	cross
		reuse all parent's attributes to create child
			NeuralNet child = new NeuralNet(iNodes,hNodes,oNodes,hLayers);

		cross all weight matrices and store them in child weight list
			child.weights[i] = weights[i].crossover(partner.weights[i]);
		
		return child

	clone
		create a clone with same attributes
		and clone all weights
			clone.weights[i] = weights[i].clone();

	load ?
		save all weights from given list to network's weights list

	pull ?
		clone the weights

	show
		draw the network


----- Matrix ----
	(rows, columns)
	define your own matrice
		create all possible action on matrice

	dot (product ?)
	randomize

	toArray
	singleColumnMatrixFromArray ========> class method 

	addBias
		create matrix with 1 col
		cp first col content into it
		set last line value to 1 ??? biais ???

	activate
		loop over all cells 
			apply activation function
				relu : max (0, cell value)

	mutate
	crossover
	clone




----- ? ----




'''