import sys
from PyQt4.QtGui import *
import TP4_base
import TP4_Main
import time
import random
import string

int_letter_couples = list(zip(range(0, len(string.ascii_uppercase)),
							  string.ascii_uppercase))
int_to_letter = { int:letter for (int, letter) in int_letter_couples }
letter_to_int = { letter:int for (int, letter) in int_letter_couples }

class window_app():
	def __init__(self,grid,entryray):
		app = QApplication(sys.argv)
		window = QWidget()
		window.setWindowTitle("Ray Game")
		window.show()
		window.resize((grid.height+4) * 64 , (grid.width+4) * 64)
		layout = QGridLayout(window)
		layout_elements = dict()
		button_elements = dict()
		empty_elements = dict()
		for x in range(2,2+grid.width):
			layout_elements[x,0] = QLabel("?")
			layout_elements[x,4+grid.height] = QLabel("?")
			#button_elements[x,1] = buttom_app(x,1,"^")
			button_elements[x,1] = button(x, 1, "^",grid)
			button_elements[x,3+grid.height] = button(x, 3+grid.height, "v",grid)
		for y in range(2,2+grid.height):
			layout_elements[0,y] = QLabel("?")
			layout_elements[4+grid.width,y] = QLabel("?")
			button_elements[1,y] = button(1, y, "<",grid)
			button_elements[3+grid.width,y] = button(3+grid.width, y, ">",grid)
		for x in range(2,2+grid.width):
			layout.addWidget (layout_elements[x,0],0,x)
			layout.addWidget (layout_elements[x,4+grid.height],4+grid.height,x)
			layout.addWidget (button_elements[x,1].btn,1,x)
			layout.addWidget (button_elements[x,3+grid.height].btn,3+grid.height,x)
		for y in range(2,2+grid.height):
			layout.addWidget (layout_elements[0,y],y,0)
			layout.addWidget (layout_elements[4+grid.width,y],y,4+grid.width)
			layout.addWidget (button_elements[1,y].btn,y,1)
			layout.addWidget (button_elements[3+grid.width,y].btn,y,3+grid.width)
		for x in range(2,2+grid.width):
			for y in range(2,2+grid.height):
				layout.addWidget (grid[x-2,y-2].img_repr(),y,x)
				empty_elements[x,y] = QLabel()
				empty_elements[x,y].setPixmap(QPixmap("images/aether.png"))


		#input to give time to try to see matrix before reseting
		#x = input("Go on?")
		#Erase mirrors and add entryray position
		
		for x in range(2,2+grid.width):
			layout_elements[x,0].setText("")
			layout_elements[x,4+grid.height].setText("")
		for y in range(2,2+grid.height):
			layout_elements[0,y].setText("")
			layout_elements[4+grid.width,y].setText("")
		for x in range(2,2+grid.width):
			for y in range(2,2+grid.height):
				layout.addWidget (empty_elements[x,y],y,x)
		#print(entryray[0],entryray[1])
		layout_elements[entryray[0],entryray[1]].setText(entryray[2])
		#while answer == None:
		#	pass
		sys.exit(app.exec_())
	

class button(QWidget):
	def __init__(self,x,y,desc,grid):
		self._x=x
		self._y=y
		self._width = grid.width
		self._height= grid.height
		super(button,self).__init__()
		self._btn = QPushButton(desc, self)

		self.initUI()

	def initUI(self):
		self.btn.move(20, 20)
		self.btn.clicked.connect(self.coordinates)

	def string_of_exit(self):
		print(self._x, self._y)
		if self._x == 1:
			exit=str(int_to_letter[self.y]+">")
		elif self._x == self._width+3:
			exit=str(int_to_letter[self.y]+"<")
		elif self._y == 1:
			exit=str(int_to_letter[self.x]+"v")
		elif self._y == self._height+3:
			exit=str(int_to_letter[self.x]+"^")
		return exit

	def coordinates(self):
		#global answer
		answer_coord = (self._x, self._y)
		exits = TP4_Main.simulate_exits()
		answer = self.string_of_exit()
		#string_entry_ray = (TP4_base.convert_ray(window_app.entryray, window_app.grid))
		#exits = new_grid.get_exits(string_entry_ray)
		for exit in exits:
			if exit==answer:
				print("yes")
			else:
				print("no")
	@property
	def btn(self):
		return self._btn
	


"""def window_app(grid):
	app = QApplication(sys.argv)
	window = QWidget()
	window.setWindowTitle("Kamasutra")
	window.show()
	#window.resize(grid.height * 64 , grid.width * 64)
	layout = QGridLayout(window)
	for x in range(grid.width):
		for y in range(grid.height):
			layout.addWidget (grid[x,y].img_repr(),y,x)
	sys.exit(app.exec_())"""