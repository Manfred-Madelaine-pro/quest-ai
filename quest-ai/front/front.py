from tkinter import *

from back import back

try:
	import colors
except ImportError:
	from front import colors


# grid
WIDTH = 9
LENGTH = WIDTH

MARGIN = 2
WINDOW_SIZE = 600

# colors
BACKGROUND = 'white'
MIDDLEGROUD = 'grey'
FOREGROUD = 'black'


REFRESH_DELAY = 100


class FrontGrid:
	def __init__(self, width, length):
		self.f = Tk()
		self.f.title('Generic Grid')
		
		self.width = width
		self.length = length
		self.cell_size = WINDOW_SIZE/self.width
		
		self.being_size = self.cell_size/2
		self.being_step = self.being_size/2

		self.canvas = Canvas(
						self.f, 
						width=self.width * self.cell_size, 
						height=self.length * self.cell_size, 
						background=BACKGROUND)
		self.canvas.pack()
		
		self.__init_entities()
		self.__create_access_buttons()
		self.__bind_shortcuts()
		
		self.f.mainloop()
		

	def __init_entities(self):
		self.front_cells = {}
		self.front_beings = {}

		for i in range(self.width):
			for j in range(self.length):
				x0 = i*self.cell_size + MARGIN
				y0 = j*self.cell_size + MARGIN
				x1 = self.cell_size*self.width - MARGIN
				y1 = self.cell_size*self.width - MARGIN
				rect_id = self.canvas.create_rectangle(x0, y0, x1, y1, fill=BACKGROUND)

				self.canvas.itemconfig(rect_id, tags=(str(i+1), str(j+1)))
				self.front_cells[(i,j)] = rect_id

	def __create_access_buttons(self):

		def create_button(f, txt, command, s):
			b = Button(f, text=txt, command=command)
			b.pack(side=s, padx=5, pady=5)

		create_button(self.f, 'Bring to Life', self.__init_univers, LEFT)
		create_button(self.f, 'Play', self.__update_creation, LEFT)
		create_button(self.f, 'Stop', self.__stop_creation, LEFT)

	def __init_univers(self):
		self.back_grid = back.GenericGrid(self.width, self.length)
		self.__update_creation()
	def __update_creation(self):
		self.back_grid.start()
		self.f.after(REFRESH_DELAY, self.__update_screen)
	def __stop_creation(self):
		self.back_grid.stop()


	def __update_screen(self):
		# update grid
		self.back_grid.update()
		self.__draw_beings()
		self.__draw_cells()

		# callback
		if not self.back_grid.is_complete:
			self.f.after(REFRESH_DELAY, self.__update_screen)
	

# ---------------------------------------------------------

	def __draw_beings(self):
		for being in self.back_grid.beings.values():
			if being.u_name in self.back_grid.dead_names:
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
			fill='red'
		)
		self.front_beings[being.u_name] = being_id
	
	def remove_beings(self, u_name):
		print(f"Removed {u_name}!")
		self.canvas.delete(self.front_beings[u_name])
		del self.front_beings[u_name]
	
	def change_pos(self, u_name, new_x, new_y):
		self.canvas.move(self.front_beings[u_name], new_x, new_y)


# ---------------------------------------------------------

	def __draw_cells(self):
		for i in range(self.width):
			for j in range(self.length):
				label = self.back_grid.cells[i][j].label
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

	def __bind_shortcuts(self):
		self.f.bind('<q>', self.__quit)
		self.f.bind('<Escape>', self.__quit)
		self.f.bind('<b>', self.__update_creation_bind)
		self.f.bind('<x>', self.__start_bind)
		self.f.bind('<space>', self.__stop_bind)

	def __update_creation_bind(self, key):
		self.__init_univers()
	def __start_bind(self, key):
		self.__play_creation()
	def __stop_bind(self, key):
		self.__stop_creation()
	def __quit(self, key):
		self.f.destroy()



# ---------------------------------------------------------

if __name__ == '__main__':
	FrontGrid = FrontGrid(WIDTH, LENGTH)


	