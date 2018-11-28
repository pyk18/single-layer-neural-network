# Arora, Priyank
# 1001-55-3349
# 2018-09-08
# Assignment-03-01

import sys
import scipy.misc
import random
import os
from sklearn.metrics import mean_squared_error,mean_absolute_error
from sklearn.metrics import confusion_matrix
if sys.version_info[0] < 3:
	import Tkinter as tk
else:
	import tkinter as tk
from tkinter import simpledialog
from tkinter import filedialog
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.backends.tkagg as tkagg


class MainWindow(tk.Tk):
	"""
	This class creates and controls the main window frames and widgets
	Farhad Kamangar 2018_06_03
	"""

	def __init__(self, debug_print_flag=False):
		tk.Tk.__init__(self)
		self.debug_print_flag = debug_print_flag
		self.master_frame = tk.Frame(self)
		self.master_frame.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		self.rowconfigure(0, weight=1, minsize=500)
		self.columnconfigure(0, weight=1, minsize=500)
		# set the properties of the row and columns in the master frame
		# self.master_frame.rowconfigure(0, weight=1,uniform='xx')
		# self.master_frame.rowconfigure(1, weight=1, uniform='xx')
		self.master_frame.rowconfigure(2, weight=10, minsize=400, uniform='xx')
		self.master_frame.rowconfigure(3, weight=1, minsize=10, uniform='xx')
		self.master_frame.columnconfigure(0, weight=1, minsize=200, uniform='xx')
		#self.master_frame.columnconfigure(1, weight=1, minsize=200, uniform='xx')
		# create all the widgets
		self.menu_bar = MenuBar(self, self.master_frame, background='orange')
		self.tool_bar = ToolBar(self, self.master_frame)
		self.left_frame = tk.Frame(self.master_frame)
		#self.right_frame = tk.Frame(self.master_frame)
		self.status_bar = StatusBar(self, self.master_frame, bd=1, relief=tk.SUNKEN)
		# Arrange the widgets
		self.menu_bar.grid(row=0, columnspan=2, sticky=tk.N + tk.E + tk.S + tk.W)
		self.tool_bar.grid(row=1, columnspan=2, sticky=tk.N + tk.E + tk.S + tk.W)
		self.left_frame.grid(row=2, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		#self.right_frame.grid(row=2, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
		self.status_bar.grid(row=3, columnspan=2, sticky=tk.N + tk.E + tk.S + tk.W)
		# Create an object for plotting graphs in the left frame
		self.display_activation_functions = LeftFrame(self, self.left_frame, debug_print_flag=self.debug_print_flag)
		# Create an object for displaying graphics in the right frame
		#self.display_graphics = RightFrame(self, self.right_frame, debug_print_flag=self.debug_print_flag)


class MenuBar(tk.Frame):
	def __init__(self, root, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self.root = root
		self.menu = tk.Menu(self.root)
		root.config(menu=self.menu)
		self.file_menu = tk.Menu(self.menu)
		self.menu.add_cascade(label="File", menu=self.file_menu)
		self.file_menu.add_command(label="New", command=self.menu_callback)
		self.file_menu.add_command(label="Open...", command=self.menu_callback)
		self.file_menu.add_separator()
		self.file_menu.add_command(label="Exit", command=self.menu_callback)
		self.dummy_menu = tk.Menu(self.menu)
		self.menu.add_cascade(label="Dummy", menu=self.dummy_menu)
		self.dummy_menu.add_command(label="Item1", command=self.menu_item1_callback)
		self.dummy_menu.add_command(label="Item2", command=self.menu_item2_callback)
		self.help_menu = tk.Menu(self.menu)
		self.menu.add_cascade(label="Help", menu=self.help_menu)
		self.help_menu.add_command(label="About...", command=self.menu_help_callback)

	def menu_callback(self):
		self.root.status_bar.set('%s', "called the menu callback!")

	def menu_help_callback(self):
		self.root.status_bar.set('%s', "called the help menu callback!")

	def menu_item1_callback(self):
		self.root.status_bar.set('%s', "called item1 callback!")

	def menu_item2_callback(self):
		self.root.status_bar.set('%s', "called item2 callback!")


class ToolBar(tk.Frame):
	def __init__(self, root, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self.root = root
		self.master = master
		self.var_filename = tk.StringVar()
		self.var_filename.set('')
		self.ask_for_string = tk.Button(self, text="Ask for a string", command=self.ask_for_string)
		self.ask_for_string.grid(row=0, column=1)
		self.file_dialog_button = tk.Button(self, text="Open File Dialog", fg="blue", command=self.browse_file)
		self.file_dialog_button.grid(row=0, column=2)
		self.open_dialog_button = tk.Button(self, text="Open Dialog", fg="blue", command=self.open_dialog_callback)
		self.open_dialog_button.grid(row=0, column=3)

	def say_hi(self):
		self.root.status_bar.set('%s', "hi there, everyone!")

	def ask_for_string(self):
		s = simpledialog.askstring('My Dialog', 'Please enter a string')
		self.root.status_bar.set('%s', s)

	def ask_for_float(self):
		f = float(simpledialog.askfloat('My Dialog', 'Please enter a float'))
		self.root.status_bar.set('%s', str(f))

	def browse_file(self):
		self.var_filename.set(tk.filedialog.askopenfilename(filetypes=[("allfiles", "*"), ("pythonfiles", "*.txt")]))
		filename = self.var_filename.get()
		self.root.status_bar.set('%s', filename)

	def open_dialog_callback(self):
		d = MyDialog(self.root)
		self.root.status_bar.set('%s', "mydialog_callback pressed. Returned results: " + str(d.result))

	def button2_callback(self):
		self.root.status_bar.set('%s', 'button2 pressed.')

	def toolbar_draw_callback(self):
		self.root.display_graphics.create_graphic_objects()
		self.root.status_bar.set('%s', "called the draw callback!")

	def toolbar_callback(self):
		self.root.status_bar.set('%s', "called the toolbar callback!")


class MyDialog(tk.simpledialog.Dialog):
	def body(self, parent):
		tk.Label(parent, text="Integer:").grid(row=0, sticky=tk.W)
		tk.Label(parent, text="Float:").grid(row=1, column=0, sticky=tk.W)
		tk.Label(parent, text="String:").grid(row=1, column=2, sticky=tk.W)
		self.e1 = tk.Entry(parent)
		self.e1.insert(0, 0)
		self.e2 = tk.Entry(parent)
		self.e2.insert(0, 4.2)
		self.e3 = tk.Entry(parent)
		self.e3.insert(0, 'Default text')
		self.e1.grid(row=0, column=1)
		self.e2.grid(row=1, column=1)
		self.e3.grid(row=1, column=3)
		self.cb = tk.Checkbutton(parent, text="Hardcopy")
		self.cb.grid(row=3, columnspan=2, sticky=tk.W)

	def apply(self):
		try:
			first = int(self.e1.get())
			second = float(self.e2.get())
			third = self.e3.get()
			self.result = first, second, third
		except ValueError:
			tk.tkMessageBox.showwarning("Bad input", "Illegal values, please try again")


class StatusBar(tk.Frame):
	def __init__(self, root, master, *args, **kwargs):
		tk.Frame.__init__(self, master, *args, **kwargs)
		self.label = tk.Label(self)
		self.label.grid(row=0, sticky=tk.N + tk.E + tk.S + tk.W)

	def set(self, format, *args):
		self.label.config(text=format % args)
		self.label.update_idletasks()

	def clear(self):
		self.label.config(text="")
		self.label.update_idletasks()


class LeftFrame:
	"""
	This class creates and controls the widgets and figures in the left frame which
	are used to display the activation functions.
	Farhad Kamangar 2018_06_03
	"""

	def __init__(self, root, master, debug_print_flag=False):
		self.master = master
		self.root = root
		#########################################################################
		#  Set up the constants and default values
		#########################################################################

		self.xmin = 0
		self.xmax = 10
		self.ymin = 0
		self.ymax = 2
		self.alpha_rate = 0.1
		self.delay_element = 11
		self.train_size = 0.8
		self.stride = 2
		self.iterations = 10
		self.weights = np.zeros((1,(2*(self.delay_element))+1))
		self.test_data = []
		self.train_data = []
		self.data = []
		self.mae = []
		self.mse = []
		self.current_epoch = 0
		#########################################################################
		#  Set up the plotting frame and controls frame
		#########################################################################
		master.rowconfigure(0, weight=10, minsize=200)
		master.columnconfigure(0, weight=1)
		self.plot_frame = tk.Frame(self.master, borderwidth=10, relief=tk.SUNKEN)
		self.plot_frame.grid(row=0, column=0, columnspan=1, sticky=tk.N + tk.E + tk.S + tk.W)
		self.figure = plt.figure("")
		self.axes = self.figure.add_axes([0.15, 0.15, 0.6, 0.8])
		# self.axes = self.figure.add_axes()
		self.axes = self.figure.gca()
		self.axes.set_xlabel('Iteration')
		self.axes.set_ylabel('Error')
		# self.axes.margins(0.5)
		self.axes.set_title("")
		plt.xlim(self.xmin, self.xmax)
		plt.ylim(self.ymin, self.ymax)
		self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
		self.plot_widget = self.canvas.get_tk_widget()
		self.plot_widget.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		self.plot_widget.pack(side="top", fill='both', expand=True)
		# Create a frame to contain all the controls such as sliders, buttons, ...
		self.controls_frame = tk.Frame(self.master)
		self.controls_frame.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		#########################################################################
		#  Set up the control widgets such as sliders and selection boxes
		#########################################################################
		self.data = self.read_csv_as_matrix("data1.csv") # read data
		self.train_test_split() # split data
		self.number_of_delay_slider = tk.Scale(self.controls_frame, variable=tk.DoubleVar(), orient=tk.HORIZONTAL,
												   from_= 0, to_=100, resolution=10, bg="#DDDDDD",
												   activebackground="#FF0000", highlightcolor="#00FFFF", label="Delay Element",
												   command=lambda event: self.slider_callback())
		self.number_of_delay_slider.set(self.delay_element-1)
		self.number_of_delay_slider.bind("<ButtonRelease-1>", lambda event: self.slider_callback())
		self.number_of_delay_slider.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		#########################################################################
		#  Set up the control widgets such as sliders and selection boxes
		#########################################################################

		self.alpha_rate_slider = tk.Scale(self.controls_frame, variable=tk.DoubleVar(), orient=tk.HORIZONTAL,
												   from_= 0.001 , to_= 1, resolution=0.001, bg="#DDDDDD",
												   activebackground="#FF0000", highlightcolor="#00FFFF", label="Alpha Rate",
												   command=lambda event: self.slider_callback())
		self.alpha_rate_slider.set(self.alpha_rate)
		self.alpha_rate_slider.bind("<ButtonRelease-1>", lambda event: self.slider_callback())
		self.alpha_rate_slider.grid(row=0, column=1, sticky=tk.N + tk.E + tk.S + tk.W)
		#########################################################################
		#  Set up the control widgets such as sliders and selection boxes
		#########################################################################
		self.training_sample_slider = tk.Scale(self.controls_frame, variable=tk.DoubleVar(), orient=tk.HORIZONTAL,
												   from_= 0, to_=100, resolution=10, bg="#DDDDDD",
												   activebackground="#FF0000", highlightcolor="#00FFFF", label="Train Size",
												   command=lambda event: self.slider_callback())
		self.training_sample_slider.set(int(self.train_size*100))
		self.training_sample_slider.bind("<ButtonRelease-1>", lambda event: self.slider_callback())
		self.training_sample_slider.grid(row=0, column=2, sticky=tk.N + tk.E + tk.S + tk.W)

		#########################################################################
		#  Set up the control widgets such as sliders and selection boxes
		#########################################################################

		self.stride_slider = tk.Scale(self.controls_frame, variable=tk.DoubleVar(), orient=tk.HORIZONTAL,
												   from_= 0, to_=100, resolution=1, bg="#DDDDDD",
												   activebackground="#FF0000", highlightcolor="#00FFFF", label="Stride",
												   command=lambda event: self.slider_callback())
		self.stride_slider.set(self.stride//2)
		self.stride_slider.bind("<ButtonRelease-1>", lambda event: self.slider_callback())
		self.stride_slider.grid(row=0, column=3, sticky=tk.N + tk.E + tk.S + tk.W)

		#########################################################################
		#  Set up the control widgets such as sliders and selection boxes
		#########################################################################


		self.number_of_iteration_slider = tk.Scale(self.controls_frame, variable=tk.DoubleVar(), orient=tk.HORIZONTAL,
												   from_= 0, to_=100, resolution=10, bg="#DDDDDD",
												   activebackground="#FF0000", highlightcolor="#00FFFF", label="Iterations",
												   command=lambda event: self.slider_callback())
		self.number_of_iteration_slider.set(self.iterations)
		self.number_of_iteration_slider.bind("<ButtonRelease-1>", lambda event: self.slider_callback())
		self.number_of_iteration_slider.grid(row=0, column=4, sticky=tk.N + tk.E + tk.S + tk.W)

		#########################################################################
		#  Set up the frame for drop down selection
		#########################################################################

		self.reset_weights_button = tk.Button(self.controls_frame, text="Reset Weights", fg="blue", command=self.reset_weights_function)
		self.reset_weights_button.grid(row=0, column=5)
		self.adjust_weights_LMS_button = tk.Button(self.controls_frame, text="LMS", fg="blue", command=self.do_lms_algo_training)
		self.adjust_weights_LMS_button.grid(row=0, column=6)
		self.adjust_weights_direct_button = tk.Button(self.controls_frame, text="Direct", fg="blue", command=self.do_direct_algorithm)
		self.adjust_weights_direct_button.grid(row=0, column=7)

		self.canvas.get_tk_widget().bind("<ButtonPress-1>", self.left_mouse_click_callback)
		self.canvas.get_tk_widget().bind("<ButtonPress-1>", self.left_mouse_click_callback)
		self.canvas.get_tk_widget().bind("<ButtonRelease-1>", self.left_mouse_release_callback)
		self.canvas.get_tk_widget().bind("<B1-Motion>", self.left_mouse_down_motion_callback)
		self.canvas.get_tk_widget().bind("<ButtonPress-3>", self.right_mouse_click_callback)
		self.canvas.get_tk_widget().bind("<ButtonRelease-3>", self.right_mouse_release_callback)
		self.canvas.get_tk_widget().bind("<B3-Motion>", self.right_mouse_down_motion_callback)
		self.canvas.get_tk_widget().bind("<Key>", self.key_pressed_callback)
		self.canvas.get_tk_widget().bind("<Up>", self.up_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Down>", self.down_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Right>", self.right_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Left>", self.left_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Shift-Up>", self.shift_up_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Shift-Down>", self.shift_down_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Shift-Right>", self.shift_right_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("<Shift-Left>", self.shift_left_arrow_pressed_callback)
		self.canvas.get_tk_widget().bind("f", self.f_key_pressed_callback)
		self.canvas.get_tk_widget().bind("b", self.b_key_pressed_callback)

	def key_pressed_callback(self, event):
		self.root.status_bar.set('%s', 'Key pressed')

	def up_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Up arrow was pressed")

	def down_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Down arrow was pressed")

	def right_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Right arrow was pressed")

	def left_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Left arrow was pressed")

	def shift_up_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift up arrow was pressed")

	def shift_down_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift down arrow was pressed")

	def shift_right_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift right arrow was pressed")

	def shift_left_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift left arrow was pressed")

	def f_key_pressed_callback(self, event):
		self.root.status_bar.set('%s', "f key was pressed")

	def b_key_pressed_callback(self, event):
		self.root.status_bar.set('%s', "b key was pressed")

	def left_mouse_click_callback(self, event):
		self.root.status_bar.set('%s', 'Left mouse button was clicked. ' + 'x=' + str(event.x) + '   y=' + str(
			event.y))
		self.x = event.x
		self.y = event.y
		self.canvas.focus_set()

	def left_mouse_release_callback(self, event):
		self.root.status_bar.set('%s',
		                         'Left mouse button was released. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = None
		self.y = None

	def left_mouse_down_motion_callback(self, event):
		self.root.status_bar.set('%s', 'Left mouse down motion. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = event.x
		self.y = event.y

	def right_mouse_click_callback(self, event):
		self.root.status_bar.set('%s', 'Right mouse down motion. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = event.x
		self.y = event.y

	def right_mouse_release_callback(self, event):
		self.root.status_bar.set('%s',
		                         'Right mouse button was released. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = None
		self.y = None

	def right_mouse_down_motion_callback(self, event):
		self.root.status_bar.set('%s', 'Right mouse down motion. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = event.x
		self.y = event.y

	def left_mouse_click_callback(self, event):
		self.root.status_bar.set('%s', 'Left mouse button was clicked. ' + 'x=' + str(event.x) + '   y=' + str(
			event.y))
		self.x = event.x
		self.y = event.y

	def slider_callback(self):
		self.iterations = int(self.number_of_iteration_slider.get())
		self.stride = int(self.stride_slider.get())*2
		self.train_size = np.float(self.training_sample_slider.get())/100
		self.alpha_rate = np.float(self.alpha_rate_slider.get())
		if self.delay_element != int(self.number_of_delay_slider.get()) + 1:
			self.delay_element = int(self.number_of_delay_slider.get()) + 1
			self.reset_weights_function()

	def read_csv_as_matrix(self,file_name):
		# Each row of data in the file becomes a row in the matrix
		# So the resulting matrix has dimension [num_samples x sample_dimension]
		data = np.loadtxt(file_name, skiprows=1, delimiter=',', dtype=np.float32)
		std = lambda x: 2 * ((x - np.amin(x)) / (np.amax(x) - np.amin(x))) - 1
		return np.apply_along_axis(std, 0, data)

	# self.focus_set()
	def display_activation_function(self,x_val,y_val,y_val_2,sttring):
		self.axes.relim()
		self.axes.autoscale_view()
		self.axes.cla()
		self.axes.set_xlabel('Iterations')
		self.axes.set_ylabel('Errors')
		self.axes.plot(x_val, y_val, "k--", color="blue", label = "Mean Square Error")
		self.axes.plot(x_val, y_val_2,"k:", color="green", label = "Maximum Absolute Error")
		self.axes.set_ylim([self.ymin, self.ymax])
		self.axes.xaxis.set_visible(True)
		self.axes.legend(loc='upper right', shadow=True)
		plt.title(sttring)
		self.canvas.draw()

	def input_weight_slider_callback(self):
		self.alpha_rate = np.float(self.alpha_learning_rate_slider.get())

	def train_test_split(self):
		split_row = int(self.train_size * len(self.data))
		self.train_data = self.data[:split_row]
		self.test_data = self.data[split_row:]

	def do_lms_algo_training(self):
		for k in range(self.current_epoch, self.current_epoch + self.iterations):
			#Training Part
			len_1 = len(self.train_data)
			for i in range(0, len_1 - self.delay_element, self.stride):
				delay = min(self.delay_element, len_1 - i - 1)
				if delay != self.delay_element:
					diff = (self.delay_element) - delay
					dd = np.hstack(
						(np.flipud(self.train_data[i:i + delay, 1]), [0] * diff, np.flipud(self.train_data[i:i + delay, 0]), [0] * diff, [1]))
				else:
					dd = np.hstack((np.flipud(self.train_data[i:i + delay, 1]), np.flipud(self.train_data[i:i + delay, 0]), [1]))
				error = self.train_data[i + delay, 0] - np.dot(self.weights, dd)
				self.weights += np.multiply(2 * self.alpha_rate * error, dd)
			#Testing Part
			len_1 = len(self.test_data)
			predic = []
			true = []
			for i in range(0, len_1 - self.delay_element, self.stride):
				delay = min(self.delay_element, len_1 - i - 1)
				if delay != self.delay_element:
					diff = (self.delay_element) - delay
					dd = np.hstack(
						(np.flipud(self.test_data[i:i + delay, 1]), [0] * diff, np.flipud(self.test_data[i:i + delay, 0]), [0] * diff, [1]))
				else:
					dd = np.hstack((np.flipud(self.data[i:i + delay, 1]), np.flipud(self.test_data[i:i + delay, 0]), [1]))
				predic.append(np.dot(self.weights, dd)[0])
				true.append(self.test_data[i + delay, 0])
				#plot them on the graph
			self.mse.append(mean_squared_error(true, predic))
			self.mae.append(max(np.absolute(np.subtract(true, predic))))
			self.display_activation_function(range(len(self.mse)),self.mse,self.mae,"LMS")

	def do_direct_algorithm(self):
		for k in range(self.current_epoch,self.current_epoch+self.iterations):
			len_1 = len(self.train_data)
			h = np.zeros((1, (2 * (self.delay_element)) + 1))
			R = np.zeros((((2 * (self.delay_element)) + 1), (2 * (self.delay_element)) + 1))
			total = 0
			for i in range(0, len_1 - self.delay_element, self.stride):
				total += 1
				delay = min(self.delay_element, len_1 - i - 1)
				if delay != self.delay_element:
					diff = (self.delay_element) - delay
					dd = np.hstack(
						(np.flipud(self.train_data[i:i + delay, 1]), [0] * diff, np.flipud(self.train_data[i:i + delay, 0]), [0] * diff, [1]))
				else:
					dd = np.hstack((np.flipud(self.train_data[i:i + delay, 1]), np.flipud(self.train_data[i:i + delay, 0]), [1]))
				target = self.train_data[i + delay, 0]
				h += np.multiply(target, dd)
				R += np.outer(dd, dd)
			R /= total
			h /= total
			self.weights = np.dot(h, np.linalg.inv(R))
			len_1 = len(self.test_data)
			predic = []
			true = []
			for i in range(0, len_1 - self.delay_element, self.stride):
				delay = min(self.delay_element, len_1 - i - 1)
				if delay != self.delay_element:
					diff = (self.delay_element) - delay
					dd = np.hstack(
						(np.flipud(self.test_data[i:i + delay, 1]), [0] * diff, np.flipud(self.test_data[i:i + delay, 0]), [0] * diff, [1]))
				else:
					dd = np.hstack((np.flipud(self.data[i:i + delay, 1]), np.flipud(self.test_data[i:i + delay, 0]), [1]))
				predic.append(np.dot(self.weights, dd)[0])
				true.append(self.test_data[i + delay, 0])
				#plot them on the graph
			self.mse.append(mean_squared_error(true, predic))
			self.mae.append(max(np.absolute(np.subtract(true, predic))))
			self.display_activation_function(range(len(self.mse)), self.mse, self.mae, "LMS Direct")

	def reset_weights_function(self):
		self.weights = np.zeros((1,(2*(self.delay_element))+1))

class RightFrame:
	"""
	This class is for creating right frame widgets which are used to draw graphics
	on canvas as well as embedding matplotlib figures in the tkinter.
	Farhad Kamangar 2018_06_03
	"""

	def __init__(self, root, master, debug_print_flag=False):
		self.root = root
		self.master = master
		self.debug_print_flag = debug_print_flag
		width_px = root.winfo_screenwidth()
		height_px = root.winfo_screenheight()
		width_mm = root.winfo_screenmmwidth()
		height_mm = root.winfo_screenmmheight()
		# 2.54 cm = in
		width_in = width_mm / 25.4
		height_in = height_mm / 25.4
		width_dpi = width_px / width_in
		height_dpi = height_px / height_in
		if self.debug_print_flag:
			print('Width: %i px, Height: %i px' % (width_px, height_px))
			print('Width: %i mm, Height: %i mm' % (width_mm, height_mm))
			print('Width: %f in, Height: %f in' % (width_in, height_in))
			print('Width: %f dpi, Height: %f dpi' % (width_dpi, height_dpi))
		# self.canvas = self.master.canvas
		#########################################################################
		#  Set up the plotting frame and controls frame
		#########################################################################
		master.rowconfigure(0, weight=10, minsize=200)
		master.columnconfigure(0, weight=1)
		master.rowconfigure(1, weight=1, minsize=20)
		self.right_frame = tk.Frame(self.master, borderwidth=10, relief='sunken')
		self.right_frame.grid(row=0, column=0, columnspan=1, sticky=tk.N + tk.E + tk.S + tk.W)
		self.matplotlib_width_pixel = self.right_frame.winfo_width()
		self.matplotlib_height_pixel = self.right_frame.winfo_height()
		# set up the frame which contains controls such as sliders and buttons
		self.controls_frame = tk.Frame(self.master)
		self.controls_frame.grid(row=1, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		self.controls_frame.rowconfigure(1, weight=1, minsize=20)
		self.draw_button = tk.Button(self.controls_frame, text="Draw", fg="red", width=16,
		                             command=self.graphics_draw_callback)
		self.plot_2d_button = tk.Button(self.controls_frame, text="Plot 2D", fg="red", width=16,
		                                command=self.matplotlib_plot_2d_callback)
		self.plot_3d_button = tk.Button(self.controls_frame, text="Plot 3D", fg="red", width=16,
		                                command=self.matplotlib_plot_3d_callback)
		self.draw_button.grid(row=0, column=0)
		self.plot_2d_button.grid(row=0, column=1)
		self.plot_3d_button.grid(row=0, column=2)
		self.right_frame.update()
		self.canvas = tk.Canvas(self.right_frame, relief='ridge', width=self.right_frame.winfo_width() - 110,
		                        height=self.right_frame.winfo_height())
		if self.debug_print_flag:
			print("Right frame width, right frame height : ", self.right_frame.winfo_width(),
			      self.right_frame.winfo_height())
		self.canvas.rowconfigure(0, weight=1)
		self.canvas.columnconfigure(0, weight=1)
		self.canvas.grid(row=0, column=0, sticky=tk.N + tk.E + tk.S + tk.W)
		self.canvas.bind("<ButtonPress-1>", self.left_mouse_click_callback)
		self.canvas.bind("<ButtonRelease-1>", self.left_mouse_release_callback)
		self.canvas.bind("<B1-Motion>", self.left_mouse_down_motion_callback)
		self.canvas.bind("<ButtonPress-3>", self.right_mouse_click_callback)
		self.canvas.bind("<ButtonRelease-3>", self.right_mouse_release_callback)
		self.canvas.bind("<B3-Motion>", self.right_mouse_down_motion_callback)
		self.canvas.bind("<Key>", self.key_pressed_callback)
		self.canvas.bind("<Up>", self.up_arrow_pressed_callback)
		self.canvas.bind("<Down>", self.down_arrow_pressed_callback)
		self.canvas.bind("<Right>", self.right_arrow_pressed_callback)
		self.canvas.bind("<Left>", self.left_arrow_pressed_callback)
		self.canvas.bind("<Shift-Up>", self.shift_up_arrow_pressed_callback)
		self.canvas.bind("<Shift-Down>", self.shift_down_arrow_pressed_callback)
		self.canvas.bind("<Shift-Right>", self.shift_right_arrow_pressed_callback)
		self.canvas.bind("<Shift-Left>", self.shift_left_arrow_pressed_callback)
		self.canvas.bind("f", self.f_key_pressed_callback)
		self.canvas.bind("b", self.b_key_pressed_callback)
		# Create a figure for 2d plotting
		self.matplotlib_2d_fig = mpl.figure.Figure()
		# self.matplotlib_2d_fig.set_size_inches(4,2)
		self.matplotlib_2d_fig.set_size_inches((self.right_frame.winfo_width() / width_dpi) - 0.5,
		                                       self.right_frame.winfo_height() / height_dpi)
		self.matplotlib_2d_ax = self.matplotlib_2d_fig.add_axes([.1, .1, .7, .7])
		if self.debug_print_flag:
			print("Matplotlib figsize in inches: ", (self.right_frame.winfo_width() / width_dpi) - 0.5,
			      self.right_frame.winfo_height() / height_dpi)
		self.matplotlib_2d_fig_x, self.matplotlib_2d_fig_y = 0, 0
		self.matplotlib_2d_fig_loc = (self.matplotlib_2d_fig_x, self.matplotlib_2d_fig_y)
		# fig = plt.figure()
		# ax = fig.gca(projection='3d')
		# Create a figure for 3d plotting
		self.matplotlib_3d_fig = mpl.figure.Figure()
		self.matplotlib_3d_figure_canvas_agg = FigureCanvasAgg(self.matplotlib_3d_fig)
		# self.matplotlib_2d_fig.set_size_inches(4,2)
		self.matplotlib_3d_fig.set_size_inches((self.right_frame.winfo_width() / width_dpi) - 0.5,
		                                       self.right_frame.winfo_height() / height_dpi)
		self.matplotlib_3d_ax = self.matplotlib_3d_fig.add_axes([.1, .1, .6, .6], projection='3d')
		self.matplotlib_3d_fig_x, self.matplotlib_3d_fig_y = 0, 0
		self.matplotlib_3d_fig_loc = (self.matplotlib_3d_fig_x, self.matplotlib_3d_fig_y)

	def display_matplotlib_figure_on_tk_canvas(self):
		# Draw a matplotlib figure in a Tk canvas
		self.matplotlib_2d_ax.clear()
		X = np.linspace(0, 2 * np.pi, 100)
		# Y = np.sin(X)
		Y = np.sin(X * np.int((np.random.rand() + .1) * 10))
		self.matplotlib_2d_ax.plot(X, Y)
		self.matplotlib_2d_ax.set_xlim([0, 2 * np.pi])
		self.matplotlib_2d_ax.set_ylim([-1, 1])
		self.matplotlib_2d_ax.grid(True, which='both')
		self.matplotlib_2d_ax.axhline(y=0, color='k')
		self.matplotlib_2d_ax.axvline(x=0, color='k')
		# plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
		# Place the matplotlib figure on canvas and display it
		self.matplotlib_2d_figure_canvas_agg = FigureCanvasAgg(self.matplotlib_2d_fig)
		self.matplotlib_2d_figure_canvas_agg.draw()
		self.matplotlib_2d_figure_x, self.matplotlib_2d_figure_y, self.matplotlib_2d_figure_w, \
		self.matplotlib_2d_figure_h = self.matplotlib_2d_fig.bbox.bounds
		self.matplotlib_2d_figure_w, self.matplotlib_2d_figure_h = int(self.matplotlib_2d_figure_w), int(
			self.matplotlib_2d_figure_h)
		self.photo = tk.PhotoImage(master=self.canvas, width=self.matplotlib_2d_figure_w,
		                           height=self.matplotlib_2d_figure_h)
		# Position: convert from top-left anchor to center anchor
		self.canvas.create_image(self.matplotlib_2d_fig_loc[0] + self.matplotlib_2d_figure_w / 2,
		                         self.matplotlib_2d_fig_loc[1] + self.matplotlib_2d_figure_h / 2, image=self.photo)
		tkagg.blit(self.photo, self.matplotlib_2d_figure_canvas_agg.get_renderer()._renderer, colormode=2)
		self.matplotlib_2d_fig_w, self.matplotlib_2d_fig_h = self.photo.width(), self.photo.height()
		self.canvas.create_text(0, 0, text="Sin Wave", anchor="nw")

	def display_matplotlib_3d_figure_on_tk_canvas(self):
		self.matplotlib_3d_ax.clear()
		r = np.linspace(0, 6, 100)
		temp=np.random.rand()
		theta = np.linspace(-temp * np.pi, temp * np.pi, 40)
		r, theta = np.meshgrid(r, theta)
		X = r * np.sin(theta)
		Y = r * np.cos(theta)
		Z = np.sin(np.sqrt(X ** 2 + Y ** 2))
		surf = self.matplotlib_3d_ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap="coolwarm", linewidth=0, antialiased=False);
		# surf = self.matplotlib_3d_ax.plot_surface(X, Y, Z, rcount=1, ccount=1, cmap='bwr', edgecolor='none');
		self.matplotlib_3d_ax.set_xlim(-6, 6)
		self.matplotlib_3d_ax.set_ylim(-6, 6)
		self.matplotlib_3d_ax.set_zlim(-1.01, 1.01)
		self.matplotlib_3d_ax.zaxis.set_major_locator(LinearLocator(10))
		self.matplotlib_3d_ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
		# Place the matplotlib figure on canvas and display it
		self.matplotlib_3d_figure_canvas_agg.draw()
		self.matplotlib_3d_figure_x, self.matplotlib_3d_figure_y, self.matplotlib_3d_figure_w, \
		self.matplotlib_3d_figure_h = self.matplotlib_2d_fig.bbox.bounds
		self.matplotlib_3d_figure_w, self.matplotlib_3d_figure_h = int(self.matplotlib_3d_figure_w), int(
			self.matplotlib_3d_figure_h)
		if self.debug_print_flag:
			print("Matplotlib 3d figure x, y, w, h: ", self.matplotlib_3d_figure_x, self.matplotlib_3d_figure_y,
			      self.matplotlib_3d_figure_w, self.matplotlib_3d_figure_h)
		self.photo = tk.PhotoImage(master=self.canvas, width=self.matplotlib_3d_figure_w,
		                           height=self.matplotlib_3d_figure_h)
		# Position: convert from top-left anchor to center anchor
		self.canvas.create_image(self.matplotlib_3d_fig_loc[0] + self.matplotlib_3d_figure_w / 2,
		                         self.matplotlib_3d_fig_loc[1] + self.matplotlib_3d_figure_h / 2, image=self.photo)
		tkagg.blit(self.photo, self.matplotlib_3d_figure_canvas_agg.get_renderer()._renderer, colormode=2)
		self.matplotlib_3d_fig_w, self.matplotlib_3d_fig_h = self.photo.width(), self.photo.height()

	def key_pressed_callback(self, event):
		self.root.status_bar.set('%s', 'Key pressed')

	def up_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Up arrow was pressed")

	def down_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Down arrow was pressed")

	def right_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Right arrow was pressed")

	def left_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Left arrow was pressed")

	def shift_up_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift up arrow was pressed")

	def shift_down_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift down arrow was pressed")

	def shift_right_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift right arrow was pressed")

	def shift_left_arrow_pressed_callback(self, event):
		self.root.status_bar.set('%s', "Shift left arrow was pressed")

	def f_key_pressed_callback(self, event):
		self.root.status_bar.set('%s', "f key was pressed")

	def b_key_pressed_callback(self, event):
		self.root.status_bar.set('%s', "b key was pressed")

	def left_mouse_click_callback(self, event):
		self.root.status_bar.set('%s', 'Left mouse button was clicked. ' + 'x=' + str(event.x) + '   y=' + str(
			event.y))
		self.x = event.x
		self.y = event.y
		self.canvas.focus_set()

	def left_mouse_release_callback(self, event):
		self.root.status_bar.set('%s',
		                         'Left mouse button was released. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = None
		self.y = None

	def left_mouse_down_motion_callback(self, event):
		self.root.status_bar.set('%s', 'Left mouse down motion. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = event.x
		self.y = event.y

	def right_mouse_click_callback(self, event):
		self.root.status_bar.set('%s', 'Right mouse down motion. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = event.x
		self.y = event.y

	def right_mouse_release_callback(self, event):
		self.root.status_bar.set('%s',
		                         'Right mouse button was released. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = None
		self.y = None

	def right_mouse_down_motion_callback(self, event):
		self.root.status_bar.set('%s', 'Right mouse down motion. ' + 'x=' + str(event.x) + '   y=' + str(event.y))
		self.x = event.x
		self.y = event.y

	def left_mouse_click_callback(self, event):
		self.root.status_bar.set('%s', 'Left mouse button was clicked. ' + 'x=' + str(event.x) + '   y=' + str(
			event.y))
		self.x = event.x
		self.y = event.y

	# self.focus_set()
	def frame_resized_callback(self, event):
		print("frame resize callback")

	def create_graphic_objects(self):
		self.canvas.delete("all")
		r = np.random.rand()
		self.drawing_objects = []
		for scale in np.linspace(.1, 0.8, 20):
			self.drawing_objects.append(self.canvas.create_oval(int(scale * int(self.canvas.cget("width"))),
			                                                    int(r * int(self.canvas.cget("height"))),
			                                                    int((1 - scale) * int(self.canvas.cget("width"))),
			                                                    int((1 - scale) * int(self.canvas.cget("height")))))

	def redisplay(self, event):
		self.create_graphic_objects()

	def matplotlib_plot_2d_callback(self):
		self.display_matplotlib_figure_on_tk_canvas()
		self.root.status_bar.set('%s', "called matplotlib_plot_2d_callback callback!")

	def matplotlib_plot_3d_callback(self):
		self.display_matplotlib_3d_figure_on_tk_canvas()
		self.root.status_bar.set('%s', "called matplotlib_plot_3d_callback callback!")

	def graphics_draw_callback(self):
		self.create_graphic_objects()
		self.root.status_bar.set('%s', "called the draw callback!")


def close_window_callback(root):
	if tk.messagebox.askokcancel("Quit", "Do you really wish to quit?"):
		root.destroy()


main_window = MainWindow(debug_print_flag=False)
# main_window.geometry("500x500")
main_window.wm_state('normal')
main_window.title('Assignment_01 --  Kamangar')
main_window.minsize(800, 600)
main_window.protocol("WM_DELETE_WINDOW", lambda root_window=main_window: close_window_callback(root_window))
main_window.mainloop()

