import random


VERBOSE = __name__ == '__main__'


MAX_WATER = 10
MAX_PLANT = 10

BEING_INITIAL_WATER = 3

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (0,1)

VERTICAL = [UP, DOWN]
HORIZONTAL = [LEFT, RIGHT]
DIRECTIONS = dict(enumerate(VERTICAL + HORIZONTAL))


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
	def __init__(self, x, y, max_water=MAX_WATER, max_plant=MAX_PLANT):
		super().__init__(x, y)

		self.u_name = 'cell'
		self.label = ''
		self.plant = 0

		self.max_water = max_water
		self.max_plant = max_plant

	def generate(self):
		self.water = random.randint(0, self.max_water)
		self.plant = random.randint(0, self.max_plant)
		self.update_label()

	def update_label(self):
		if self.water > self.plant:
			self.label = 'water'
		elif self.water < self.plant:
			self.label = 'plant'

	def get_water(self, sip):
		s = min(sip, self.water)
		self.water -= s
		return s

# ---------------------------------------------------------

class Being (Entity):
	def __init__(self, u_name, x, y, world):
		super().__init__(x, y, water=BEING_INITIAL_WATER)

		# TODO get random unique name
		self.year = 0
		self.sip = 1
		self.alive = True
		self.world = world
		self.u_name = u_name

# -------------------------------------------------

	def update(self):
		self.action()
		self.year += 1
		
		self.heath_check()

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

# -------------------------------------------------

	def heath_check(self):
		self.check_borders()
		self.check_water_lvl()

	def check_borders(self):
		if self.world.out_of_boud(self.x, self.y):
			self.is_dead('fell off the world')

	def check_water_lvl(self):
		if self.water <= 0 and self.alive:
			self.is_dead('died of thirst')

	def is_dead(self, reason='is dead'):
		self.alive = False
		verbose_print(f"\t{self.u_name} {reason} at the age of {self.year}.")

# -------------------------------------------------

	def random_move(self, diagonal=False):
		if diagonal:
			self.random_step(horizontal=True)
			self.random_step(horizontal=False)
		else:
			self.random_step(random.getrandbits(1))

	def random_step(self, horizontal=True):
		direction = random.choice(HORIZONTAL) if horizontal else random.choice(VERTICAL)
		self.step(direction)

	def pick_direction(self, key):
		return DIRECTIONS.get(key)

	def step(self, direction):
		verbose_print(f"{self} moved by {direction}!")
		self.x += direction[0]
		self.y += direction[1]

# -------------------------------------------------

	def drink(self):
		cell = self.world.cells[(self.x, self.y)]
		if cell.water >= 1:
			old_cell = str(cell)
			sip = cell.get_water(self.sip)
			verbose_print(f"{self}(+{sip}) drank in {old_cell}(-{sip})")
			self.water += sip
			return 0

		verbose_print(f"{self} tryed to drink but {cell} is completely dry ! [FAILED]")
		return 1


verbose_print = print if VERBOSE else lambda *a, **k: None