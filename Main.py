#Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 1 
#Fait par Luis Augusto YOKOTA RIZZO et Daniel Toshihiro OKANE

import string
import os

def PrintGrid(grid):
	for i in range(len(grid)):
		line=""
		for j in range(len(grid[0])):
			line+=grid[i][j]
		print(line)

#verify if the input of the mirror is correct
def checkmirror (mirror):
	while True :
		if mirror == "/": return mirror
		elif mirror == "\\": return mirror
		else :
			print("I've not recognised the mirror type.")
			mirror = input("To add mirror select / or \\:")

#verify if the mirror is inside the grid
def checkcoord(coord,max_x,max_y):
	coord_m = (coord.strip()).split(",")
	coord_m [0]= int(coord_m[0])
	coord_m [1]= int(coord_m[1])
	#print(coord_m)
	while True:
		if coord_m[0] > 0 and coord_m[0] < max_x - 1 and coord_m[1] > 0 and coord_m[1] < max_y - 1:
			return coord_m
		else:
			print("Mirror outside of range.")
			coord = input("Add new coordinates as i,j:")
			coord_m = (coord.strip()).split(",")
			coord_m [0]= int(coord_m[0])
			coord_m [1]= int(coord_m[1])

class ray():

	def __init__(self,x0,y0,direction0):
		self.x = x0
		self.y = y0
		self.direction = direction0

	#change the position of the ray
	def translate (self):
		self.printray()
		self.x += self.direction[0]
		self.y += self.direction[1]

	#define the symbol of the ray
	def printray(self):
		if self.direction == (0,-1) :
			return "<"
		elif self.direction == (0,1) :
			return ">"
		elif self.direction == (1,0) :
			return "v"
		elif self.direction == (-1,0) :
			return "^"
		else :
			return ""

	#change the direction of the ray when hiting a mirror
	def reflex (self, m):
		if m == "/" :
			if self.direction == (-1,0) :
				self.direction = (0,1)
			elif self.direction == (0,1) :
				self.direction = (-1,0)
			elif self.direction == (0,-1) :
				self.direction = (1,0)
			elif self.direction == (1,0) :
				self.direction = (0,-1)
		elif m == "\\" :
			if self.direction == (1,0) :
				self.direction = (0,1)
			elif self.direction == (0,1) :
				self.direction = (1,0)
			elif self.direction == (0,-1) :
				self.direction = (-1,0)
			elif self.direction == (-1,0) :
				self.direction = (0,-1)

def main():
	#create an empty grid
	width=int(input("What's the width of the grid? "))+2
	height=int(input("What's the height of the grid? "))+2
	while width < 4 or height < 4 or width >28 or height > 28:
		print("Problem with inputs given.")
		width=int(input("What's the width of the grid? "))+2
		height=int(input("What's the height of the grid? "))+2
	grid=[]
	for i in range(height):
		row=[]
		for j in range(width):
			row.append(" ")
		grid.append(row)

	#add letters to the first and last rows and columns
	letters=list(string.ascii_uppercase)
	for i in range(width-2):
		grid[0][i+1]=letters[i]
		grid[height-1][i+1]=letters[i]
	for j in range(height-2):
		grid[j+1][0]=letters[j]
		grid[j+1][width-1]=letters[j]

	#add mirrors to the grid
	add_mirrors = True
	keep_adding = input("Do you want to add a mirror? (y/n) ")
	while add_mirrors :
		if keep_adding == "y":
			coord = input("Add coordinates i,j: ")
			m = input("Add mirror type (/ or \\): ")

			m = checkmirror (m)
			mirror_position = checkcoord(coord, height, width)

			grid[mirror_position[0]][mirror_position[1]]=m

			PrintGrid(grid)
			keep_adding = input("Do you want to add another mirror? (y/n) ")
		elif keep_adding == "n":
			add_mirrors = False
		else :
			print("I did not understand your answer.")
			keep_adding = input("Do you want to add another mirror? (y/n) ")
	print("Final grid is :")
	PrintGrid(grid)

	#Initial position of the ray
	question_ray_letter = input("Entry point: type the uppercase letter of the ray: ")
	question_ray_direction = input("Entry point: type the direction of the ray: ")
	match = 26
	while match == 26:
		for i in range(25):
			if question_ray_letter==letters[i]:
				match=i
				break
		if match == 26:
			print("I did not understand your ray entrypoint.")
			question_ray_letter = input("Entry point: type the uppercase letter of the ray: ")
	while question_ray_direction != "<" and question_ray_direction != ">" and question_ray_direction != "v" and question_ray_direction != "^":
		print("I did not understand your ray direction.")
		question_ray_direction = input("Entry point: type the direction of the ray: ")

	if question_ray_direction=="<":
		direction = (0,-1)
		x=width-2
		y=match+1
	elif  question_ray_direction==">":
		direction = (0,1)
		x=1
		y=match+1
	elif  question_ray_direction=="^":
		direction = (-1,0)
		x=match+1
		y=height-2
	elif  question_ray_direction=="v":
		direction = (1,0)
		x=match+1
		y=1
	else:
		print ("Ray direction problem.")
	r=ray(y,x,direction)

	#Ray's movement
	inside = True
	while inside :
		if grid[r.x][r.y] == "/" or grid[r.x][r.y] == "\\" :
			r.reflex(grid[r.x][r.y])
			r.translate()
		else :
			grid[r.x][r.y] = r.printray()
			r.translate()
		os.system('cls' if os.name == 'nt' else "printf '\033c'")
		PrintGrid(grid)
		if r.x > height-2 or r.x < 1 or r.y > width-2 or r.y < 1 :
			inside = False
	print ("Game over, ray left out the system! Point of exit is ",grid[r.x][r.y]," with a direction ",r.printray())

main()
