import string

def PrintGrid(grid):
	for i in range(len(grid)):
		line=""
		for j in range(len(grid[0])):
			line+=grid[j][i]
		print(line)

width=int(input("What's the width of the grid?"))+2
height=int(input("What's the height of the grid?"))+2
#empty grid
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
