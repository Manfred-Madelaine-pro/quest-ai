from tkinter import *

from back import back

try:
	import screen
	import colors
except ImportError:
	from front import screen 
	from front import colors


MARGIN = 2


class Front(screen.GenericScreen):

	def __init__(self, width, length):
		super().__init__(width, length)

		self.f.title('Quest AI')
		self.being_size = self.cell_size/2
		self.being_step = self.being_size/2

		self.init_entities()
		super().create_access_buttons()
		super().bind_shortcuts()
		
		self.f.mainloop()
		

	def init_entities(self):
		self.front_cells = {}
		self.front_beings = {}

		for i in range(self.width):
			for j in range(self.length):
				x0 = i*self.cell_size + MARGIN
				y0 = j*self.cell_size + MARGIN
				x1 = self.cell_size*self.width - MARGIN
				y1 = self.cell_size*self.width - MARGIN
				rect_id = self.canvas.create_rectangle(x0, y0, x1, y1, fill='white')

				self.canvas.itemconfig(rect_id, tags=(str(i+1), str(j+1)))
				self.front_cells[(i,j)] = rect_id


# ------------------------- Overrided Methods --------------------------------
	
	def init_world(self):
		self.back_model = back.Model(self.width, self.length)

	def update(self):
		self.back_model.update()
		self.draw_beings()
		self.draw_cells()

# --------------------------------------------------------------------------

	def draw_beings(self):
		for being in self.back_model.beings.values():
			if being.u_name in self.back_model.dead_names:
				self.remove_beings(being.u_name)
			elif being.u_name not in self.front_beings:
				self.create_beings(being)
			else:
				self.change_pos(being.u_name, being.x, being.y)

	def create_beings(self, being):
		being_id = self.canvas.create_oval(
			being.x*self.being_step, 
			being.y*self.being_step, 
			being.x*self.being_step + self.being_size,
			being.y*self.being_step + self.being_size,
			fill=self.get_being_color()
		)
		self.front_beings[being.u_name] = being_id
	
	def get_being_color(self):
		return colors.random_color_in_list([colors.RED, colors.YELLOW])

	def remove_beings(self, u_name):
		print(f"Removed {u_name}!")
		self.canvas.delete(self.front_beings[u_name])
		del self.front_beings[u_name]
	
	def change_pos(self, u_name, new_x, new_y):
		self.canvas.move(self.front_beings[u_name], new_x, new_y)


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
	front = Front(width, length)


	