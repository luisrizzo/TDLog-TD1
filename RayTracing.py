from numpy import *

class ray():

	def __init__(x0,y0,dir0)
		self._x = x0
		self._y = y0
		self._dir = dir0

	def translate (self,dir)
		printray(dir)
		self.x += dir[0]
		self.y += dir[1]

	def printray(dir)
		if dir == (0,1) :
			return "^"
		elif dir == (0,-1) :
			return "V"
		elif dir == (1,0) :
			return ">"
		elif dir == (-1,0) :
			return "<"
		else
			return ""

def reflex (m, dir)
	if m = "/" :
		if dir == (1,0) :
			dir = (0,-1)
		elif dir == (0,1) :
			dir = (-1,0)
		elif dir == (0,-1) :
			dir = (1,0)
		elif dir == (-1,0) :
			dir = (0,1)
		else
			print ("Ray direction problem")
	elif m = "\\" :
		if dir == (1,0) :
			dir = (0,1)
		elif dir == (0,1) :
			dir = (1,0)
		elif dir == (0,-1) :
			dir = (-1,0)
		elif dir == (-1,0) :
			dir = (0,-1)
		else
			print ("Ray direction problem")

g=grid(x,y)
question_ray_x = input("X coordinate of ray")
question_ray_y = input("Y coordinate of ray")
if question_ray_1 == "Horizontal":

r=ray(x,y,dir)
inside = True
while inside :
	if grid[ray.x][ray.y] == "/" or grid[ray.x][ray.y] == "\\" :
		ray.reflex(grid[ray.x][ray.y],dir)
		translate(dir)
	else
		grid[ray.x][ray.y].value = ray.printray(dir)
		translate(dir)
		grid.print_grid
	if ray.x > grid.x or ray.x < 1 or ray.y > grid.y or ray.y < 1 :
		inside = False
Print ("Game over, ray left out the system! Coordinates of exit are" & r(x,y))

