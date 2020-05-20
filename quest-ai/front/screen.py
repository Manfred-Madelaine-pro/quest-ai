from tkinter import *


PAD_X = 0
PAD_Y = 0

WINDOW_SIZE = 600

REFRESH_DELAY = 200


class GenericScreen:

	def __init__(self, width, length):
		self.f = Tk()
		
		self.width = width
		self.length = length
		self.cell_size = WINDOW_SIZE/self.width


		top_frame = Frame(self.f, relief=GROOVE)
		top_frame.pack(side=TOP, padx=PAD_X, pady=PAD_Y)

		# ----
		main_frame = Frame(top_frame, relief=GROOVE)
		main_frame.pack(side=LEFT, padx=PAD_X, pady=PAD_Y)

		self.canvas = Canvas(
						main_frame, 
						width=self.width * self.cell_size, 
						height=self.length * self.cell_size, 
						background='white')
		self.canvas.pack(side=LEFT, padx=PAD_X, pady=PAD_Y)


		# ----
		right_frame = Frame(top_frame, relief=GROOVE)
		right_frame.pack(side=RIGHT, padx=PAD_X, pady=PAD_Y)

		# ----
		stat_frame = Frame(right_frame, borderwidth=2, relief=GROOVE)
		stat_frame.pack(side=TOP, padx=PAD_X, pady=PAD_Y)

		Label(stat_frame, text="Stats").pack(side=TOP, padx=PAD_X, pady=PAD_Y)

		# ----
		history_frame = Frame(right_frame, borderwidth=2, relief=GROOVE)
		history_frame.pack(side=TOP, padx=PAD_X, pady=PAD_Y)

		Label(history_frame, text="History").pack(side=TOP, padx=PAD_X, pady=PAD_Y)

		# ----
		self.option_bar = Frame(self.f, relief=GROOVE)
		self.option_bar.pack(side=BOTTOM, padx=PAD_X, pady=PAD_Y)


	def create_access_buttons(self):

		def create_button(f, txt, command, s):
			b = Button(f, text=txt, command=command)
			b.pack(side=s, padx=5, pady=5)

		create_button(self.option_bar, 'Bring to Life', self.init_univers, LEFT)
		create_button(self.option_bar, 'Play', self.update_creation, LEFT)
		create_button(self.option_bar, 'Stop', self.stop_creation, LEFT)

	def init_univers(self):
		self.init_world()
		self.update_creation()
	def update_creation(self):
		self.back_model.start()
		self.f.after(REFRESH_DELAY, self.update_screen)
	def stop_creation(self):
		self.back_model.stop()


	def update_screen(self):
		self.update()

		# callback
		if not self.back_model.is_complete:
			self.f.after(REFRESH_DELAY, self.update_screen)


	def init_world(self):
		pass
	def update(self):
		pass

# ---------------------------------------------------------

	def bind_shortcuts(self):
		self.f.bind('<q>', self.quit)
		self.f.bind('<Escape>', self.quit)
		self.f.bind('<b>', self.update_creation_bind)
		self.f.bind('<x>', self.start_bind)
		self.f.bind('<space>', self.stop_bind)

	def update_creation_bind(self, key):
		self.init_univers()
	def start_bind(self, key):
		self.play_creation()
	def stop_bind(self, key):
		self.stop_creation()
	def quit(self, key):
		self.f.destroy()

