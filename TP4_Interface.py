import sys
from PyQt5.QtGui import *

class window_app():
	def __init__(self,grid):
		window = QWidget()
		window.resize(grid.height * 64 , grid.width * 64)
		for x in range(grid.width):
			for y in range(grid.height):
				layout.addwidget (grid[x,y].img_repr(),y,x)
		window.show()

class QLabel():
	def __init__(self,grid,description):
		pass

class QPushButton():
	def __init__(self):
		pass

class QTimer():
	def __init__(self):
		pass

class QMessageBox():
	def __init__(self,answer,list_exits):
		pass
