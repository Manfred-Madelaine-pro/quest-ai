from tkinter import *


WINDOW_SIZE = 600

REFRESH_DELAY = 100


class GenericScreen:

	def __init__(self, width, length):
		self.f = Tk()
		
		self.width = width
		self.length = length
		self.cell_size = WINDOW_SIZE/self.width

		self.canvas = Canvas(
						self.f, 
						width=self.width * self.cell_size, 
						height=self.length * self.cell_size, 
						background='white')
		self.canvas.pack()


	def create_access_buttons(self):

		def create_button(f, txt, command, s):
			b = Button(f, text=txt, command=command)
			b.pack(side=s, padx=5, pady=5)

		create_button(self.f, 'Bring to Life', self.init_univers, LEFT)
		create_button(self.f, 'Play', self.update_creation, LEFT)
		create_button(self.f, 'Stop', self.stop_creation, LEFT)

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

