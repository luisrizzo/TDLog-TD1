import string

def PrintGrid(grid):
	for i in range(len(grid)):
		line=""
		for j in range(len(grid[0])):
			line+=grid[j][i]
		print(line)

def checkmirror (mirror):
	while True :
		if mirror == "/": return
		elif mirror == "\\": return
		else :
			print("I've not recognised the mirror type")
			mirror = input("To add mirror type select / or \\")

def checkcoord(coord,max_x,max_y):
	coord_m = (coord.strip()).split(",")
	while True:
		if coord_m(0) > 1 and coord_m(0) < max_x and coord_m(1) > 1 and coord_m(1) < max_y
			return coord_m
		else:
			coord = input("Add coordinates: x,y")

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

#create an empty grid
width=int(input("What's the width of the grid?"))+2
height=int(input("What's the height of the grid?"))+2
grid=[]
for i in range(height):
	row=[]
	for j in range(width):
		row.append(" ")
	grid.append(row)

#add letters to the first and last rows and columns
letters=list(string.ascii_uppercase)
for i in range(height-2):
	grid[0][i+1]=letters[i]
	grid[height-1][i+1]=letters[i]
for j in range(width-2):
	grid[j+1][0]=letters[j]
	grid[j+1][width-1]=letters[j]

add_mirrors = True
keep_adding = input("Do you want to add a mirror? (y/n)")
while add_mirrors :
	if keep_adding == "y":
		coord = input("Add coordinates: x,y")
		m = input("Add mirror type: / or \\")

		checkmirror (m)
		mirror_position = checkcoord (coord, width, height)

		grid(mirror_position(0),mirror_position(1))

		PrintGrid(grid)
		keep_adding = input("Do you want to add another mirror? (y/n)")
	elif keep_adding == "n":
		add_mirrors = False
	else :
		print("I did not understand your answer.")
		keep_adding = input("Do you want to add another mirror? (y/n)")
Prind ("Final grid is :")
PrintGrid(grid)

#Initial position of the ray
question_ray_letter = input("Entry point: type the uppercase letter of the ray:")
question_ray_dir = input("Entry point: type the direction of the ray:")
for i in range(30):
	if question_ray_letter==letters[i]:
		match=i
		break
#Write check routine to see if letter is a valid entry or not

if question_ray_dir=="^":
	dir = (0,-1)
	x=match
	y=height-2
elif  question_ray_dir=="V":
	dir = (0,1)
	x=match
	y=1
elif  question_ray_dir==">":
	dir = (1,0)
	x=1
	y=match
elif  question_ray_dir=="<":
	dir = (-1,0)
	x=width-2
	y=match
else:
	print ("Ray direction problem")

r=ray(x,y,dir)

#Ray's movement
inside = True
while inside :
	if grid[r.x][r.y] == "/" or grid[r.x][r.y] == "\\" :
		r.reflex(grid[r.x][r.y],dir)
		r.translate()
	else :
		grid[r.x][r.y] = r.printray()
		r.translate()
	PrintGrid()
	if r.x > width-2 or r.x < 1 or r.y > height-2 or r.y < 1 :
		inside = False
Print ("Game over, ray left out the system! Coordinates of exit are" & r(x,y))