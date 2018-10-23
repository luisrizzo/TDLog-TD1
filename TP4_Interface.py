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
		for x in range(2,2+grid.width):
			layout_elements[x,0] = Qlabel("?")
			layout_elements[x,2+grid.height] = Qlabel("?")
		for y in range(2,2+grid.height):
			layout_elements[x,0] = Qlabel("?")
			layout_elements[x,2+grid.height] = Qlabel("?")
		for x in range(2,2+grid.width):
			for y in range(2,2+grid.height):
				layout.addWidget (grid[x-2,y-2].img_repr(),y,x)

		a=TP4_base.ForwardSlashMirror()	
		kamasutra = a.img_repr()
		layout.addWidget (kamasutra,0,0)

		sys.exit(app.exec_())

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