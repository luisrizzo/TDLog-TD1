class ray():

	def __init__(x0,y0,dir0):
		self.x = x0
		self.y = y0
		self.dir = dir0

	def translate (self):
		printray(self.dir)
		self.x += self.dir[0]
		self.y += self.dir[1]

	def printray(self):
		if self.dir == (0,-1) :
			return "^"
		elif self.dir == (0,1) :
			return "V"
		elif self.dir == (1,0) :
			return ">"
		elif self.dir == (-1,0) :
			return "<"
		else :
			return ""

	def reflex (self, m):
		if m == "/" :
			if self.dir == (1,0) :
				self.dir = (0,-1)
			elif self.dir == (0,1) :
				self.dir = (-1,0)
			elif self.dir == (0,-1) :
				self.dir = (1,0)
			elif self.dir == (-1,0) :
				self.dir = (0,1)
			else :
				print ("Ray direction problem")
		elif m == "\\" :
			if self.dir == (1,0) :
				self.dir = (0,1)
			elif self.dir == (0,1) :
				self.dir = (1,0)
			elif self.dir == (0,-1) :
				self.dir = (-1,0)
			elif self.dir == (-1,0) :
				self.dir = (0,-1)
			else :
				print ("Ray direction problem")

#Initial position of the ray
question_ray_letter = input("Entry point: type the uppercase letter of the ray:")
question_ray_dir = input("Entry point: type the direction of the ray:")
if question_ray_dir=="^":
	dir = (0,-1)
	#x=
	y=height-2
elif  question_ray_dir=="V":
	dir = (0,1)
	#x=
	y=1
elif  question_ray_dir==">":
	dir = (1,0)
	x=1
	#y=
elif  question_ray_dir=="<":
	dir = (-1,0)
	x=width-2
	#y=
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

