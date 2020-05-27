import random

class Names:
	def __init__(self):
		self.names = [
			"Marko",
			"Paul",
			"Peder",
			"Vernet ",
			"John Martin",
			"Théodore Géricault",
			"Acacia",
			"Amande",
			"Europa",
			"Vassili ",
			"Orazio Gentileschi",
			"Artemisia Gentileschi",
			"Répine ",
			"Winslow Homer",
			"Alfred Sisley ",
			"Eugène delacroix",
			"Gustave Courbet",
			"August Renoir ",
			"Edward Mitchell Bannister",
			"José Ferraz",
			"Johannes Vermeer",
			"Rosa Bonheur",
			"Mariana Millais",
			"Odalisque",
			"Leon Gerome",
		]

	def baptise(self):
		random.shuffle(self.names)
		return self.names.pop()


if __name__ == '__main__':
	n = Names()
	print(n.baptise())
