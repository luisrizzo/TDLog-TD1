import sys
from PyQt4.QtGui import *
import TP4_base

class window_app():
	def __init__(self,grid):
		app = QApplication(sys.argv)
		window = QWidget()
		window.setWindowTitle("Ray Game")
		window.show()
		window.resize((grid.height+4) * 64 , (grid.width+4) * 64)
		layout = QGridLayout(window)
		layout_elements = dict()
		button_elements = dict()
		for x in range(2,2+grid.width):
			layout_elements[x,0] = QLabel("?")
			layout_elements[x,4+grid.height] = QLabel("?")
			button_elements[x,1] = QPushButton("^")
			button_elements[x,3+grid.height] = QPushButton("v")
		for y in range(2,2+grid.height):
			layout_elements[0,y] = QLabel("?")
			layout_elements[4+grid.width,y] = QLabel("?")
			button_elements[1,y] = QPushButton("<")
			button_elements[3+grid.width,y] = QPushButton(">")
			
		for x in range(2,2+grid.width):
			layout.addWidget (layout_elements[x,0],0,x)
			layout.addWidget (layout_elements[x,4+grid.height],4+grid.height,x)
			layout.addWidget (button_elements[x,1],1,x)
			layout.addWidget (button_elements[x,3+grid.height],3+grid.height,x)
		for y in range(2,2+grid.height):
			layout.addWidget (layout_elements[0,y],y,0)
			layout.addWidget (layout_elements[4+grid.width,y],y,4+grid.width)
			layout.addWidget (button_elements[1,y],y,1)
			layout.addWidget (button_elements[3+grid.width,y],y,3+grid.width)
		for x in range(2,2+grid.width):
			for y in range(2,2+grid.height):
				layout.addWidget (grid[x-2,y-2].img_repr(),y,x)

		sys.exit(app.exec_())
class buttom_app():
	def __init__(self,x,y,desc):
		self._x=x
		self._y=y
		return QPushButton(desc)

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