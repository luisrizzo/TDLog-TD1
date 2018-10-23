import TP4_base
import TP4_Interface
import sys
from PyQt5.QtGui import *

app = QApplication(sys.argv)
#new_grid, entry = TP4_base.box_and_entry_point()
new_grid = TP4_base.build_interactively()
print (new_grid)
TP4_Interface.window_app(new_grid)
#QGridLayout (new_grid)
#QLabel(QGridLayout,entry)
#
#traces = new_grid.simulate_nondeterministic_with_trace(entry)

sys.exit(app.exec_())