import TP4_base
import TP4_Interface
import sys
from PyQt4.QtGui import *
import random

#new_grid, entry = TP4_base.box_and_entry_point()

new_grid = TP4_base.build_automaticaly()
#print(new_grid)
print("Grid Generated")

entry_ray = TP4_base.random_entrance(new_grid)
print("Entry Ray Generated")

#app = QApplication(sys.argv)
print("Launching Interface")
#TP4_Interface.window_app(new_grid,entry_ray)
entry_ray = (TP4_base.convert_ray(entry_ray,new_grid))
exits = new_grid.get_exits(entry_ray)
print(exits)
#sys.exit(app.exec_())

#traces = new_grid.simulate_nondeterministic_with_trace(entry)




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