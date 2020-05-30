from tkinter import *

PAD_X = 0
PAD_Y = 0


class GenericScreen:
	def __init__(self, width, length, window_size=600):
		self.screen = Tk()

		self.bind_shortcuts()

		self.cofigure_settings(width, length, window_size)
		
		self.create_main_frame(self.screen)

		self.screen.mainloop()

# ---------------------------------------------------------

	def bind_shortcuts(self):
		self.screen.bind('<q>', self.quit)
		self.screen.bind('<Escape>', self.quit)

	def quit(self, key):
		self.screen.destroy()

# ---------------------------------------------------------

	def cofigure_settings(self, width, length, window_size):
		self.width = width
		self.length = length
		self.cell_size = window_size/self.width

# ---------------------------------------------------------

	def create_main_frame(self, container, side=TOP):
		self.main_frame = self.get_frame(container, side)

	def get_frame(self, container, side, fixed=False):
		frame = Frame(container, relief=GROOVE)
		if fixed:
			frame.pack(side=side, padx=PAD_X, pady=PAD_Y)
		else:
			frame.pack(fill=BOTH, expand=1, side=side, padx=PAD_X, pady=PAD_Y)
		return frame

# ---------------------------------------------------------

class GridScreen(GenericScreen):
	def __init__(self, width, length, window_size=600):
		super().__init__(width, length)

	def create_main_frame(self, container, side=TOP):
		super().create_main_frame(container, LEFT)
		self.create_buttons(self.main_frame, TOP)
		self.create_grid(self.main_frame, BOTTOM)

	def create_grid(self, container, side):
		self.grid_frame = self.get_frame(container=container, side=side)
		
		width=self.width * self.cell_size, 
		height=self.length * self.cell_size, 
		self.get_canvas(self.grid_frame, width, height, 'grey')

	def get_canvas(self, container, width, height, background):
		self.canvas = Canvas(
						container,
						width=width,
						height=height,
						background=background)
		self.canvas.pack(fill=BOTH, expand=1)

	def create_buttons(self, container, side):
		def create_button(container, txt, command, s):
			b = Button(container, text=txt, command=command)
			b.pack(side=s, padx=5, pady=5)

		self.button_frame = self.get_frame(container=container, side=side, fixed=True)
		for i in range(3):
			create_button(self.button_frame, f'Button {i}', lambda : print("Button"), LEFT)

# ---------------------------------------------------------

class PersonalizedScreen(GridScreen):
	def __init__(self, width, length, window_size=600):
		super().__init__(width, length)

	def create_main_frame(self, container, side=TOP):
		super().create_main_frame(container, LEFT)
		self.second_frame = self.create_side_frame(container, "History", LEFT)
		self.third_frame = self.create_side_frame(container, "Statistics", LEFT)

	def create_side_frame(self, container, name, side):
		side_frame = self.get_frame(container=container, side=side)
		width=5 * self.cell_size
		height=self.length * self.cell_size + 3*10

		Label(side_frame, text=name).pack(side=TOP, padx=PAD_X, pady=PAD_Y)
		self.get_canvas(side_frame, width, height, 'grey')

# ---------------------------------------------------------


if __name__ == '__main__':
	width = 9
	length = width

	front = PersonalizedScreen(width, length)


	