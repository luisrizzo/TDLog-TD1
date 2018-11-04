 #Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 4 - fichier de base
#Fait par Luis Augusto YOKOTA RIZZO
#      et Daniel Toshihiro OKANE
#!/usr/bin/env python

import TP4_base
import sys
from PyQt4.QtGui import *
import random
import string
import time
from PyQt4.QtCore import QTimer

#Global variables used in most of the functions
int_letter_couples = list(zip(range(0, len(string.ascii_uppercase)),
							  string.ascii_uppercase))
int_to_letter = { int:letter for (int, letter) in int_letter_couples }
letter_to_int = { letter:int for (int, letter) in int_letter_couples }
ticking = 0
trying = True
new_grid = TP4_base.build_automaticaly()
entry_ray = TP4_base.random_entrance(new_grid)
layout_elements = dict()
button_elements = dict()
empty_elements = dict()

#class to make similar work as of string_of_particle from the Box class in TP4_Base
def string_of_particle_interface(width,height,x,y):
	if x < 0:
		return "<" + int_to_letter[y]
	elif x >= width :
		return ">" + int_to_letter[y]
	elif y < 0:
		return "^" + int_to_letter[x]
	elif y >= height :
		return "v" + int_to_letter[x]

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
		self.btn.clicked.connect(self.showdialog)

	def showdialog(self):
		global new_grid
		global trying
		trying = False
		answer_coord = (self._x, self._y)
		exits = simulate_exits()
		answer = string_of_particle_interface(new_grid.width,new_grid.height,self._x,self._y)
		rightwrong = False
		for i in exits:
			if answer == i: rightwrong = True
		msg = QMessageBox()
		msg.setIcon(QMessageBox.Information)
		msg.setText("So you answered the game")
		if not(rightwrong): msg.setInformativeText("And your answer was wrong :" + answer)
		else : msg.setInformativeText("And your answer was right! Congratulations")
		msg.setWindowTitle("Game Over")
		msg.setDetailedText("All the correct answers are: " + str(exits))
		retval = msg.exec_()

	@property
	def btn(self):
		return self._btn

#action every 1 second for the timer
#used for explaining rules and starting the game
def tick():
	global trying
	global ticking
	global layout_elements
	global entry_ray
	global new_grid
	global empty_elements
	if trying: ticking +=1
	if ticking == 5:
		newmsg = QMessageBox()
		newmsg.setText("Remember mirror positions")
		retval = newmsg.exec_()
	elif ticking == 15:
		newmsg = QMessageBox()
		newmsg.setText("Game starts. Watch the entry point of the ray")
		retval = newmsg.exec_()
		for x in range(2,2+new_grid.width):
			layout_elements[x,0].setText("")
			layout_elements[x,4+new_grid.height].setText("")
		for y in range(2,2+new_grid.height):
			layout_elements[0,y].setText("")
			layout_elements[4+new_grid.width,y].setText("")
		if entry_ray[0]== -1:
			layout_elements[entry_ray[0]+1,entry_ray[1]+2].setText(entry_ray[2])
		elif entry_ray[0] == new_grid.width:
			layout_elements[entry_ray[0]+4,entry_ray[1]+2].setText(entry_ray[2])
		elif entry_ray[1] == new_grid.height:
			layout_elements[entry_ray[0]+2,entry_ray[1]+4].setText(entry_ray[2])
		elif entry_ray[1]== -1:
			layout_elements[entry_ray[0]+2,entry_ray[1]+1].setText(entry_ray[2])
		for x in range(2,2+new_grid.width):
			for y in range (2,2+new_grid.height):
				empty_elements[x,y].setPixmap(QPixmap("images/aether.png"))
	elif ticking == 25 :
		print("answer")
		newmsg = QMessageBox()
		newmsg.setText("You are taking too long to answer")
		retval = newmsg.exec_()
		ticking = 16

#fonction principal de l'interface graphique
class window_app():
	def __init__(self,grid,entry_ray):
		app = QApplication(sys.argv)
		window = QWidget()
		window.setWindowTitle("Ray Game")
		window.show()
		window.resize((grid.height+4) * 64 , (grid.width+4) * 64)
		timer = QTimer()
		timer.timeout.connect(tick)
		timer.start(1000)
		layout = QGridLayout(window)
		global layout_elements
		global empty_elements
		global button_elements
		for x in range(2,2+grid.width):
			layout_elements[x,0] = QLabel("?")
			layout_elements[x,4+grid.height] = QLabel("?")
			#button_elements[x,1] = buttom_app(x,1,"^")
			button_elements[x,1] = button(x-2, -1, "^",grid)
			button_elements[x,3+grid.height] = button(x-2, grid.height, "v",grid)
		for y in range(2,2+grid.height):
			layout_elements[0,y] = QLabel("?")
			layout_elements[4+grid.width,y] = QLabel("?")
			button_elements[1,y] = button(-1, y-2, "<",grid)
			button_elements[3+grid.width,y] = button(grid.width, y-2, ">",grid)
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
				empty_elements[x,y] = grid[x-2,y-2].img_repr()
		for x in range(2,2+grid.width):
			for y in range(2,2+grid.height):
				layout.addWidget (empty_elements[x,y],y,x)
		sys.exit(app.exec_())

#new_grid, entry = TP4_base.box_and_entry_point()
def simulate_exits():
	global entry_ray
	global new_grid
	string_entry_ray = TP4_base.convert_ray(entry_ray,new_grid)
	exits = new_grid.get_exits(string_entry_ray)
	return exits

def main():
	global entry_ray
	global new_grid
	user_answer = window_app(new_grid,entry_ray)
	
if __name__ == '__main__':
	main()

#sys.exit(app.exec_())

"""
a=TP4_base.ForwardSlashMirror()
b=TP4_base.SquareMirror()

window = QWidget()
window.setWindowTitle("Kamasutra")
window.show()
window.resize(8 * 64 , 8 * 64)

layout = QGridLayout(window)
label = a.img_repr()
#label.setPixmap(QPixmap("images/transporter.png"))
label2 = b.img_repr()
#label2.setPixmap(QPixmap("images/aether.png"))
layout.addWidget (label,0,0)
layout.addWidget (label2,7,7)

sys.exit(app.exec_())"""