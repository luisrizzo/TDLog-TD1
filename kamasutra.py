import TP4_base
import sys
from PyQt4.QtGui import *
import random
import string
import time
from PyQt4.QtCore import QTimer

def string_of_particle_interface(width,height,x,y):
    if x < 0:
        return "<" + int_to_letter[y]
    elif x >= width :
        return ">" + int_to_letter[y]
    elif y < 0:
        return "^" + int_to_letter[x]
    elif y >= height :
        return "v" + int_to_letter[x]

new_grid = TP4_base.build_automaticaly()
entry_ray = TP4_base.random_entrance(new_grid)
exit = []
exit.append(random.randint(0,new_grid.width-1))
exit.append(-1)
answer = string_of_particle_interface(new_grid.width, new_grid.height,exit[0],exit[1])
print(new_grid.width,new_grid.height)
print(exit)
print(answer)