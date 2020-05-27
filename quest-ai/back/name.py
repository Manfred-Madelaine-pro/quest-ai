import random

class Names:
	def __init__(self):
		self.names = [
			"Marko",
			"Paul",
			"Peder",
			"Vernet",
			"John Martin",
			"Théodore Géricault",
			"Acacia",
			"Amande",
			"Europa",
			"Vassili",
			"Orazio Gentileschi",
			"Artemisia Gentileschi",
			"Répine",
			"Winslow Homer",
			"Alfred Sisley",
			"Eugène delacroix",
			"Gustave Courbet",
			"August Renoir",
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


def new_born(mother_name, father_name=None):
	n = mother_name.split()
	n = list(filter(lambda a: a != 'Jr.', n))

	post = father_name if father_name == 'Jr.' else ''

	try:
		count = roman_to_int(n[-1]) + 1
		n.pop(-1)
		post = [post, int_to_Roman(count)] if post else [int_to_Roman(count)]
		return ' '.join(n + post)
	except Exception as e:
		return f"{' '.join(n + [post])} {int_to_Roman(1)}"


def int_to_Roman(num):
	val = [
		1000, 900, 500, 400,
		100, 90, 50, 40,
		10, 9, 5, 4,
		1
		]
	syb = [
		"M", "CM", "D", "CD",
		"C", "XC", "L", "XL",
		"X", "IX", "V", "IV",
		"I"
		]
	roman_num = ''
	i = 0
	while  num > 0:
		for _ in range(num // val[i]):
			roman_num += syb[i]
			num -= val[i]
		i += 1
	return roman_num


def roman_to_int(s):
		rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
		int_val = 0
		for i in range(len(s)):
			if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
				int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
			else:
				int_val += rom_val[s[i]]
		return int_val


if __name__ == '__main__':
	n = Names()
	nm = n.baptise()
	print(nm)

	nb = new_born(nm, 'Jr.')
	print(nb)
	nb = new_born(nm, n.baptise())
	print(nb)
	nb = new_born(nb, n.baptise())
	print(nb)
	nb = new_born(nb, 'Jr.')
	print(nb)