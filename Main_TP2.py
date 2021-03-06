#Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 2
#Fait par Luis Augusto YOKOTA RIZZO et Daniel Toshihiro OKANE


#Nous avons choisi de prendre le code corrigé du TP1 de Xavier, selon les possibilités données par M Thierry Martinez.

#1.Mirroirs additionelles: Nous avons créé une nouvelle classe pour chaque nouveau type de mirroir, avec une structure similaire des mirroir du TP1.

#2.Trace: Pour la trajectoire du rayon, nous avons décidé que si le rayon passe par un object, sa répresentation ne changera pas pour mieux comprendre la raison
#du changement de la direction ou de la position du rayon. Neanmoins, nous avons écrit des lignes de code en commentaire qui pourraient changer la 
#representation de l'object par la representation de la trajectoire.
#La trajectoire est donnée a partir du changement de la répresentation du charactère de la classe que le rayon a passée. Ce changement est fait en utilisant
#un nouveau attribute de la classe qui s'appele 'trace'.

#3.Transporters: Pour les transporters nous avons ajouté une nouvelle classe, comme pour les mirroirs. Dans ce cas, il a aussi une liste comme input de la création
#de la classe, avec tous la positions de tous les transporters. Cette liste est utilisée quand le rayon entre dans un transporter et ira apparaitre dans un transporter
#différent.


import string
import random
import sys

int_letter_couples = list(zip(range(0, len(string.ascii_uppercase)),
							  string.ascii_uppercase))
int_to_letter = { int:letter for (int, letter) in int_letter_couples }
letter_to_int = { letter:int for (int, letter) in int_letter_couples }

possible_rays = dict()
possible_rays['<'], possible_rays['>'], possible_rays['v'], possible_rays['^'] = "Exists for key","Exists for key","Exists for key","Exists for key"

possible_objects = dict()
possible_objects['/'], possible_objects['\\'], possible_objects['#'], possible_objects['|'], possible_objects['-'], possible_objects['o'] = "Exists for key","Exists for key","Exists for key","Exists for key","Exists for key","Exists for key"


class Particle:
	def __init__(self, x, y, dx, dy):
		self._x = x
		self._y = y
		self._dx = dx
		self._dy = dy
	@property
	def x(self): return self._x
	@property
	def y(self): return self._y
	@property
	def dx(self): return self._dx
	@property
	def dy(self): return self._dy
	def __str__(self):
		return "<{}, {}, {}, {}>".format(self._x, self._y, self._dx, self._dy)

class Aether:
	def __init__(self):
		self.trace=0
	@property
	def char_representation(self):
		if self.trace>0: return "."
		else: return " "

	def step(self, particle):
		self.trace +=1
		#print(self.trace)
		return Particle(particle.x + particle.dx, particle.y + particle.dy, particle.dx, particle.dy)

class ForwardSlashMirror:
	def __init__(self):
		#self.trace=False
		pass
	@property
	def char_representation(self):
		#if self.trace: return'.'
		#else: return '/'
		return '/'
	def step(self, particle):
		#self.trace=True
		dx = -particle.dy
		dy = -particle.dx
		return Particle(particle.x + dx, particle.y + dy, dx, dy)

class BackSlashMirror:
	def __init__(self):
		#self.trace=False
		pass
	@property
	def char_representation(self):
		#if self.trace: return'.'
		#else: return '\\'
		return '\\'
	def step(self, particle):
		#self.trace=True
		dx = particle.dy
		dy = particle.dx
		return Particle(particle.x + dx, particle.y + dy, dx, dy)

class VerticalMirror :
	def __init__(self):
		#self.trace=False
		pass
	@property
	def char_representation(self):
		#if self.trace: return'.'
		#else: return "|"
		return "|"
	def step(self, particle):
		#self.trace=True
		dx = -particle.dx
		dy = particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy)

class HorizontalMirror :
	def __init__(self):
		#self.trace=False
		pass
	@property
	def char_representation(self):
		#if self.trace: return'.'
		#else: return "-"
		return "-"
	def step(self, particle):
		#self.trace=True
		dx = particle.dx
		dy = -particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy)

class SquareMirror :
	def __init__(self):
		#self.trace=False
		pass
	@property
	def char_representation(self):
		#if self.trace: return'.'
		#else: return "#"
		return "#"
	def step(self, particle):
		#self.trace=True
		dx = -particle.dx
		dy = -particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy)

class Transporter :
	def __init__(self, transporters):
		self.transporters_list = transporters
		#self.trace=False
	@property
	def char_representation(self):
		#if self.trace: return'.'
		#else: return 'o'
		return 'o'
	def actionteleport(self,oldx, oldy):
		if len(self.transporters_list) > 1:
			i=random.randint(0,len(self.transporters_list)-1)
			while oldx == self.transporters_list[i][0] and oldy == self.transporters_list[i][1]:
				i=random.randint(0,len(self.transporters_list)-1)
			newx = self.transporters_list[i][0]
			newy = self.transporters_list[i][1]
			return (newx , newy)
		else:
			print(box)
			sys.exit(0)
	def step(self,particle):
		#self.trace = True
		dx = particle.dx
		dy = particle.dy
		newx, newy = self.actionteleport(particle.x,particle.y)
		return Particle (newx + dx, newy + dy, dx, dy)

class Box:
	def __init__(self, width, height, elements):
		self._width = width
		self._height = height
		self._grid = dict()
		for x in range (width):
			for y in range (height):
				self._grid[x,y] = Aether()
		for (x, y, element) in elements:
			self._grid[x, y] = element
	@property
	def width(self):
		return self._width
	@property
	def height(self):
		return self._height
	def __getitem__(self, key):
		x, y = key
		return self._grid[key]
	def __str__(self):
		rule = " " + string.ascii_uppercase[0:self._width] + " "
		lines = []
		lines.append(rule)
		for y in range(0, self._height):
			letter = int_to_letter[y]
			elements = [self[x, y].char_representation
						for x in range(0, self._width)]
			lines.append("".join([letter] + elements + [letter]))
		lines.append(rule)
		return "\n".join(lines)
	def _particle_of_string(self, description):
		direction, letter = description
		if direction == '>':
			return Particle(0, letter_to_int[letter], 1, 0)
		elif direction == '<':
			return Particle(self._width - 1, letter_to_int[letter], -1, 0)
		elif direction == 'v':
			return Particle(letter_to_int[letter], 0, 0, 1)
		elif direction == '^':
			return Particle(letter_to_int[letter], self._height - 1, 0, -1)
	def _string_of_particle(self, particle):
		if particle.x < 0:
			return "<" + int_to_letter[particle.y]
		elif particle.x >= self._width:
			return ">" + int_to_letter[particle.y]
		elif particle.y < 0:
			return "^" + int_to_letter[particle.x]
		elif particle.y >= self._height:
			return "v" + int_to_letter[particle.x]
	def _is_particle_in_box(self, particle):
		return (particle.x >= 0) and (particle.x < self._width) \
		   and (particle.y >= 0) and (particle.y < self._height)
	def simulate(self):
		def input_ray(list_of_rays):
			control_input=True
			while control_input :
				try:
					ray = input("Entry point ? ")
					ray_kind, ray_position = ray
					list_of_rays[ray_kind]
					letter_to_int[ray_position]
					if ray_kind=="^" or ray_kind=="v":
						if letter_to_int[ray_position] < self._width: control_input=False
						else: print("Entry point outside of the grid.")
					else: 
						if letter_to_int[ray_position] < self._height: control_input=False
						else: print("Entry point outside of the grid.")
				except ValueError:
					print("Invalid input. Not the right amount of inputs.")
				except KeyError :
					print("One of the inputs was invalid. Try again.")
			return ray
		particle = self._particle_of_string(input_ray(possible_rays))
		while self._is_particle_in_box(particle):
			particle = self[particle.x, particle.y].step(particle)
		return self._string_of_particle(particle)

def build_interactively():
	def input_dimension():
		control_input = True
		while control_input :
			try :
				width = int(input("Width? "))
				height = int(input("Height? "))
				if (width < 3) or (width > 26):
					print("Invalid width.")
				if (height < 3) or (height > 26):
					print("Invalid height.")
				if (width >= 3) and (width <= 26) and (height >= 3) and (height <= 26):
					control_input = False
			except ValueError:
				print ("Oops. One of the inputs was not a number.")
		return (width,height)

	def input_object(list_of_objects):
		control_input=True
		while control_input :
			try:
				obj_obj = input("Add new object? ")
				if obj_obj=="":
					break
				x_obj, y_obj, kind_obj = obj_obj
				letter_to_int[x_obj]
				letter_to_int[y_obj]
				list_of_objects[kind_obj]
				if letter_to_int[x_obj] < width and letter_to_int[y_obj] < height: control_input=False
				else: print("Position outside of the grid.")
			except ValueError:
				print("Invalid input. Not the right amount of inputs.")
			except KeyError :
				print("One of the inputs was invalid. Try again.")
		return obj_obj

	width, height = input_dimension()
	objects_list = []
	transporters = []
	object_desc = input_object(possible_objects)
	while object_desc:
		x, y, kind = object_desc
		if kind == '/': object_obj = ForwardSlashMirror()
		elif kind == '\\': object_obj = BackSlashMirror()
		elif kind == "|": object_obj = VerticalMirror()
		elif kind == "-": object_obj = HorizontalMirror()
		elif kind == "#": object_obj = SquareMirror()
		elif kind == "o":
			transporters.append((letter_to_int[x], letter_to_int[y]))
			object_obj = Transporter(transporters)
		objects_list.append((letter_to_int[x], letter_to_int[y], object_obj))
		object_desc = input_object(possible_objects)
	return Box(width, height, objects_list)

box = build_interactively()
print(box)
print(box.simulate())
print(box)