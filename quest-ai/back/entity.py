import random


VERBOSE = False

MAX_WATER = 10
MAX_PLANT = 10

WATER_LABEL = 'water'
PLANT_LABEL = 'plant'


UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (0,1)

VERTICAL = [UP, DOWN]
HORIZONTAL = [LEFT, RIGHT]
DIRECTIONS = VERTICAL + HORIZONTAL


class Entity:
	def __init__(self, x, y, water=0):
		self.x = x
		self.y = y

		self.u_name = ''
		self.water = water

	def __repr__(self):
		return "{}".format(self.v)

	def __str__(self):
		return f"{self.u_name}({self.x},{self.y})-" + "{" + f"water:{self.water}" + "}"


# ---------------------------------------------------------

class Cell (Entity):
	def __init__(self, x, y):
		super().__init__(x, y)

		self.u_name = 'cell'
		self.label = ''
		self.plant = 0


	def generate(self):
		self.water = random.randint(0, MAX_WATER)
		self.plant = random.randint(0, MAX_PLANT)
		self.update_label()


	def update_label(self):
		if self.water > self.plant:
			self.label = WATER_LABEL
		elif self.water < self.plant:
			self.label = PLANT_LABEL


	def get_water(self, sip):
		s = min(sip, self.water)
		self.water -= s
		return s


# ---------------------------------------------------------

class Being (Entity):
	def __init__(self, u_name, x, y, world):
		super().__init__(x, y, water=MAX_WATER)

		# TODO get random unique name
		self.age = 0
		self.sip = 1
		self.alive = True
		self.world = world
		self.u_name = u_name

	# -----

	def update(self):
		self.action()
		self.age += 1

		self.check_borders()
		self.check_water_lvl()

	def action(self):
		action_point = 1
		if random.random() > 0.5:
			self.random_move()
		elif random.random() > 0.5:
			self.drink()
			action_point = 0
		else:
			verbose_print(f"{self} stayed iddling.")

		self.water -= action_point

	# -----

	def check_borders(self):
		if (self.x < 0 or self.x >= self.world.width) or (self.y < 0 or self.y >= self.world.length):
			self.is_dead('fell off the world')

	def check_water_lvl(self):
		if self.water <= 0:
			self.is_dead('died of thirst')

	def is_dead(self, reason='is dead'):
		self.alive = False
		verbose_print(f"\t{self.u_name} {reason} at the age of {self.age}.")

	# -----

	def random_move(self, diagonal=False):
		if diagonal:
			self.random_step(horizontal=True)
			self.random_step(horizontal=False)
		else:
			self.random_step(random.getrandbits(1))

	def random_step(self, horizontal=True):
		dir = random.choice(HORIZONTAL) if horizontal else random.choice(VERTICAL)
				
		verbose_print(f"{self} moved by {dir}!")
		self.x += dir[0]
		self.y += dir[1]

	# -----

	def drink(self):
		cell = self.world.cells[(self.x, self.y)]
		if cell.water >= 1:
			old_cell = str(cell)
			sip = cell.get_water(self.sip)
			verbose_print(f"{self}(+{sip}) drinked in {old_cell}(-{sip})")
			self.water += sip
		else:
			verbose_print(f"{self} tryed to drink but {cell} is completely dry ! [FAILED]")



verbose_print = print if VERBOSE else lambda *a, **k: None