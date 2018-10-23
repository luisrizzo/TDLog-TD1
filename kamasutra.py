import sys
from PyQt4.QtGui import *

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Kamasutra")
window.show()
window.resize(8 * 64 , 8 * 64)
grid = []
layout = QGridLayout(window)
label = QLabel()
label.setPixmap(QPixmap("images/transporter.png"))
label2 = QLabel()
label2.setPixmap(QPixmap("images/aether.png"))
layout.addWidget (label,0,0)
layout.addWidget (label2,7,7)
layout.addWidget (label2,5,5)
#for x in range(8):
#    for y in range(8):
#        layout.addWidget (label,y,x)

sys.exit(app.exec_())