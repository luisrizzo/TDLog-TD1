import string

def PrintGrid(grid):
	for i in range(len(grid)):
		line=""
		for j in range(len(grid[0])):
			line+=grid[j][i]
		print(line)

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

PrintGrid(grid)

#Initial position of the ray
question_ray_letter = input("Entry point: type the uppercase letter of the ray:")
question_ray_dir = input("Entry point: type the direction of the ray:")
for i in range(30):
	if question_ray_letter==letters[i]:
		match=i
		break
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