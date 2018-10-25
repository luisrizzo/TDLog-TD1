import TP4_base
import TP4_Interface
import sys
from PyQt4.QtGui import *
import random

new_grid = TP4_base.build_automaticaly()
entry_ray = TP4_base.random_entrance(new_grid)

#new_grid, entry = TP4_base.box_and_entry_point()
def simulate_exits():
	global entry_ray
	global new_grid
	print(entry_ray)
	string_entry_ray = TP4_base.convert_ray(entry_ray,new_grid)
	print(string_entry_ray)
	exits = new_grid.get_exits(string_entry_ray)
	return exits

def main():
	global entry_ray
	global new_grid
	#print(new_grid)
	print("Grid Generated")
	print("Entry Ray Generated")

	print("Launching Interface")
	user_answer = TP4_Interface.window_app(new_grid,entry_ray)
	print("User answer is ", user_answer)

	print("Simulating grid")
	string_entry_ray = (TP4_base.convert_ray(entry_ray,new_grid))
	exits = new_grid.get_exits(string_entry_ray)

	print("Comparing results")
	print(exits)

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