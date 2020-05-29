from tkinter import *

from back import back

try:
	import screen
	import colors
except ImportError:
	from front import screen 
	from front import colors


	
class Front(screen.GenericScreen):

	def __init__(self, back_model, width, length, conf={}):
		self.margin = conf['margin']
		screen_conf = conf['screen'].values()
		super().__init__(width, length, *screen_conf)

		self.f.title('Quest AI')
		self.back_model = back_model

		self.being_size = self.cell_size
		self.being_step = self.being_size

		self.init_entities()
		super().create_access_buttons()
		super().bind_shortcuts()
		
		self.f.mainloop()
		

	def init_entities(self):
		self.front_beings = {}

		self.front_cells = {}
		for i in range(self.width):
			for j in range(self.length):
				x0 = i*self.cell_size + self.margin
				y0 = j*self.cell_size + self.margin
				x1 = self.cell_size*self.width - self.margin
				y1 = self.cell_size*self.width - self.margin
				rect_id = self.canvas.create_rectangle(x0, y0, x1, y1, fill='white')

				self.canvas.itemconfig(rect_id, tags=(str(i+1), str(j+1)))
				self.front_cells[(i,j)] = rect_id


# ------------------------- Overrided Methods --------------------------------
	
	def init_world(self):
		self.back_model.init_life()

	def update(self):
		self.back_model.update()
		self.draw_beings()
		self.draw_cells()

# --------------------------------------------------------------------------

	def draw_beings(self):
		# self.back_model.update()
		# self.back_model.next_generation()
		for being in self.back_model.population.entities:
			if not being.alive:
				self.remove_beings(id(being))
			elif id(being) not in self.front_beings:
				self.create_beings(being)
			else:
				self.change_pos(id(being), being.x, being.y)

	def draw_beings_old(self):
		for being in self.back_model.beings.values():
			if being.u_name in self.back_model.dead_names:
				self.remove_beings(being.u_name)
			elif being.u_name not in self.front_beings:
				self.create_beings(being)
			else:
				self.change_pos(id(being), being.x, being.y)

	def remove_beings(self, uid):
		if uid in self.front_beings:
			print(f"Removed {uid}!")
			self.canvas.delete(self.front_beings[uid])
			del self.front_beings[uid]

	def create_beings(self, being):
		front_x, front_y = self.get_front_pos(being.x, being.y)
		being_id = self.canvas.create_oval(
			front_x,
			front_y,
			front_x + self.being_size,
			front_y + self.being_size,
			fill=self.get_being_color()
		)
		print(f"Add {id(being)}!")
		self.front_beings[id(being)] = being_id
	
	def get_being_color(self):
		return colors.random_color_in_list([colors.RED, colors.YELLOW])
	
	# ----
	
	def get_front_pos(self, x, y):
		return x*self.being_step, y*self.being_step

	def change_pos(self, uid, new_x, new_y):
		old_x, old_y, old_x2, old_y2 = self.canvas.coords(self.front_beings[uid])
		front_x, front_y = self.get_front_pos(new_x, new_y)
		
		d_x, d_y = self.get_delta_pos(old_x, old_y, front_x, front_y)
		self.canvas.move(self.front_beings[uid], d_x, d_y)

	def get_delta_pos(self, old_x, old_y, new_x, new_y):
		return new_x - old_x, new_y - old_y


# ---------------------------------------------------------

	def draw_cells(self):
		for i in range(self.width):
			for j in range(self.length):
				label = self.back_model.cells[(i,j)].label
				if label == 'water':
					self.change_color(i, j, colors.BLUE, rand=True)
				elif label == 'plant':
					self.change_color(i, j, colors.GREEN)
				else:
					self.change_color(i, j, colors.BROWN)


	def change_color(self, row, column, color_hue, rand=False):
		if rand:
			color_hex = colors.get_color_with_random_lightness(color_hue)
		else:
			color_hex = colors.get_hex(color_hue)
		self.canvas.itemconfig(self.front_cells[(row, column)], fill=color_hex)


# ---------------------------------------------------------

if __name__ == '__main__':
	width = 9
	length = width

	back_model = back.Model(width, length)
	front = Front(width, length, back_model)


	