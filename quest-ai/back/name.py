import random


VERBOSE = __name__ == '__main__'

NAMES = [
	"Paul",
	"Marko",
	"Peder",
	"Vernet",
	"Acacia",
	"Amande",
	"Europa",
	"Répine",
	"Vassili",
	"Odalisque",
	"John Martin",
	"José Ferraz",
	"Leon Gerome",
	"Rosa Bonheur",
	"Winslow Homer",
	"Alfred Sisley",
	"August Renoir",
	"Mariana Millais",
	"Gustave Courbet",
	"Eugène Delacroix",
	"Johannes Vermeer",
	"Théodore Géricault",
	"Orazio Gentileschi",
	"Artemisia Gentileschi",
	"Edward-Mitchell Bannister",
]

# affixes
SUFFIX = ['Jr.', 'Oz']

# TODO
PREFIX = ['de', 'Da', 'Di', 'El', 'Van', 'Von']
HONOR_P = ['Dr.', 'Maitre', 'Professeur', "Saint", "Don", "Mage"
	"Sa Majestée", "Votre Honneur", "Votre Altesse", 
	"Compte", "Prince", "Baron", "Empereur", "Tsar", 
	"Lord", "Amiral", "Camarade", "Vizir", "Emir", "Sultan"]
HONOR_S = ['Sensei', 'San', 'Kun', "L'honorable", "Le béni", 
	"Le grand", "Le vénérable", "Krama"]


class Names:
	def __init__(self):
		self.names = NAMES.copy()

	def baptise(self):
		random.shuffle(self.names)
		name = self.names.pop().split()
		child = Name(name[0], '' if len(name) < 2 else name[1])
		return child 

# -------------------------------------------------

class Name:
	def __init__(self, first_name, last_name='', roman=0, suffixes=[]):
		self.first_name = first_name
		self.last_name = last_name
		self.suffixes = suffixes
		self.roman = roman

	def __str__(self):
		name = [self.first_name, self.last_name] if self.last_name else [self.first_name] 
		roman = [int_to_Roman(self.roman)] if self.roman > 0 else []
		full_name = name \
					+ self.suffixes \
					+ roman
		return ' '.join(full_name)

# -------------------------------------------------

	def clone(self):
		child_fn, roman, suffixes = self.handle_affixes()
		child = Name(child_fn, self.last_name, roman, suffixes)
		return child

	def crossover(self, parent):
		verbose_print(self)
		verbose_print(parent)
		child_fn, roman, suffixes = self.handle_affixes(parent)
		last_name = parent.last_name if not self.last_name else self.last_name
		child = Name(child_fn, last_name, roman, suffixes)
		verbose_print(child)
		return child


	def handle_affixes(self, parent=None):
		roman = self.roman
		suffixes = self.suffixes.copy()
		
		parents_fn = [self.first_name] if not parent else [parent.first_name, self.first_name]

		child_fn = random.choice(parents_fn + [random_first_name()])
		if child_fn in parents_fn:
			verbose_print("using parent name !")
			sfx = random.choice(SUFFIX)
			if not suffixes and not roman:
				suffixes += [sfx]
			else:
				verbose_print("introduce Roman convention !")
				# remove sfx
				suffixes = []

				if parent and (child_fn == parent.first_name): roman = parent.roman
				roman += 1
		
		return child_fn, roman, suffixes

# -------------------------------------------------

def random_first_name():
	name = random.choice(NAMES)
	return get_first_name(name)

def get_first_name(full_name):
	# remove prefixes
	return full_name.split()[0]

# -------------------------------------------------

VAL = [ 1000, 900, 500, 400,
		100, 90, 50, 40,
		10, 9, 5, 4,
		1
	]
SYB = [ "M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"
	]

def int_to_Roman(num):
	roman_num = ''
	i = 0
	while num > 0:
		for _ in range(num // VAL[i]):
			roman_num += SYB[i]
			num -= VAL[i]
		i += 1
	return roman_num

def roman_to_int(r):
		rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		int_val = 0
		for i in range(len(r)):
			if i > 0 and (rom_val[r[i]] > rom_val[r[i - 1]]):
				int_val += rom_val[r[i]] - 2 * rom_val[r[i - 1]]
			else:
				int_val += rom_val[r[i]]
		return int_val

# -------------------------------------------------


verbose_print = print if VERBOSE else lambda *a, **k: None


if __name__ == '__main__':
	f = Name("toto")
	m = Name("tata")
	for _ in range(5):
		print('--------- gen name')
		m = m.crossover(f)