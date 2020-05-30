
import tkinter
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


from generic_screen import PersonalizedScreen


class Screen(PersonalizedScreen):
	def __init__(self, width, length, window_size=600):
		super().__init__(width, length)

	def create_main_frame(self, container, side=tkinter.TOP):
		super().create_main_frame(container, tkinter.LEFT)


		fig = Figure(figsize=(5, 4), dpi=100)
		t = np.arange(0, 3, .01)
		fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

		canvas = FigureCanvasTkAgg(fig, master=self.third_frame)  # A tk.DrawingArea.
		canvas.draw()
		canvas.get_tk_widget().pack(side=tkinter.TOP)



if __name__ == '__main__':
	width = 9
	length = width

	front = Screen(width, length)
