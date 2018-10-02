import string

def PrintGrid(grid):
	#width=len(grid[0])
	#height=len(grid)
	for i in range(len(grid)):
		line=""
		for j in range(len(grid[0])):
			line+=grid[j][i]
		print(line)

width=int(input("What's the width of the grid?"))+2
height=int(input("What's the height of the grid?"))+2
#grid=[[" "]*width]*height
grid,row=[],[]
for i in range(height):
	for j in range(width):
		row.append(" ")
	grid.append(row)
letters=list(string.ascii_uppercase)
for i in range(height-2):
	grid[0][i+1]=letters[i]
	grid[height-1][i+1]=letters[i]
for j in range(width-2):
	grid[j+1][0]=letters[j]
	grid[j+1][width-1]=letters[j]
grid[3][3]="/"
print(grid[3][3])
print(grid[2][3])
PrintGrid(grid)
