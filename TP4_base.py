 #Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 4 - fichier complémentaire
#Fait par Luis Augusto YOKOTA RIZZO
#      et Daniel Toshihiro OKANE
#!/usr/bin/env python

import functools
import random
import string
from PyQt4.QtGui import *

int_letter_couples = list(zip(range(0, len(string.ascii_uppercase)),
							  string.ascii_uppercase))
int_to_letter = { int:letter for (int, letter) in int_letter_couples }
letter_to_int = { letter:int for (int, letter) in int_letter_couples }


class Particle:
	def __init__(self, x, y, dx, dy):
		assert (dx in {-1, 0, 1}) and (dy in {-1, 0, 1}), "invalid dx/dy"
		assert (dx != 0) or (dy != 0), "invalid dx/dy"
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
	def __eq__(self, other):
		return (self.__class__ == other.__class__) \
		   and (self._x == other._x) \
		   and (self._y == other._y) \
		   and (self._dx == other._dx) \
		   and (self._dy == other._dy)
	def __hash__(self):
		return self._x + self._y + self._dx + self._dy

class Deterministic:
	def __init__(self):
		pass
	def step_nondeterministic(self, particle):
		return { self.step(particle) }

class Aether(Deterministic):
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return ' '
	def step(self, particle):
		return Particle(particle.x + particle.dx,
						particle.y + particle.dy,
						particle.dx,
						particle.dy)
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/aether.png"))
		return label

class ForwardSlashMirror(Deterministic):
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '/'
	def step(self, particle):
		dx = -particle.dy
		dy = -particle.dx
		return Particle(particle.x + dx, particle.y + dy, dx, dy)
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/forward_slash_mirror.png"))
		return label

class BackSlashMirror(Deterministic):
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '\\'
	def step(self, particle):
		dx = particle.dy
		dy = particle.dx
		return Particle(particle.x + dx, particle.y + dy, dx, dy)
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/back_slash_mirror.png"))
		return label

class HorizontalMirror(Deterministic):
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '-'
	def step(self, particle):
		dx = particle.dx
		dy = -particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy)
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/horizontal_mirror.png"))
		return label

class VerticalMirror(Deterministic):
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '|'
	def step(self, particle):
		dx = -particle.dx
		dy = particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy)
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/vertical_mirror.png"))
		return label

class SquareMirror(Deterministic):
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '#'
	def step(self, particle):
		dx = -particle.dx
		dy = -particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy)
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/square_mirror.png"))
		return label

class Transporter:
	def __init__(self, o):
		self._outputs = o
	@property
	def char_representation(self):
		return 'o'
	def step(self, particle):
		if len(self._outputs) > 0:
			x, y = random.choice(self._outputs)
			dx = particle.dx
			dy = particle.dy
			return Particle(x + dx, y + dy, dx, dy)
		else:
			return None
	def step_nondeterministic(self, particle):
		dx = particle.dx
		dy = particle.dy
		return { Particle(x + dx, y + dy, dx, dy) for x, y in self._outputs }
	def img_repr(self):
		label = QLabel()
		label.setPixmap(QPixmap("images/transporter.png"))
		return label

def partition(predicate, iterable):
	true_set = set()
	false_set = set()
	for element in iterable:
		if predicate(element):
			true_set.add(element)
		else:
			false_set.add(element)
	return true_set, false_set

class Box:
	def __init__(self, width, height, elements):
		assert (width >= 3) and (width <= 26), "invalid width"
		assert (height >= 3) and (height <= 26), "invalid height"
		self._width = width
		self._height = height
		self._grid = dict()
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
		assert (x >= 0) and (x < self._width)
		assert (y >= 0) and (y < self._height)
		if key in self._grid:
			return self._grid[key]
		else:
			return Aether()
	def string_with_trace(self, trace = None):
		def char_repr(x, y, t):
			if (t != None) and ((x, y) in t):
				return '.'
			else:
				return self[x, y].char_representation
		rule = " " + string.ascii_uppercase[0:self._width] + " "
		lines = []
		lines.append(rule)
		for y in range(0, self._height):
			letter = int_to_letter[y]
			elements = [char_repr(x, y, trace) for x in range(0, self._width)]
			lines.append("".join([letter] + elements + [letter]))
		lines.append(rule)
		return "\n".join(lines)
	def __str__(self):
		return self.string_with_trace()
	def _particle_of_string(self, description):
		#print(description)
		assert (len(description) == 2)
		direction, letter = description
		assert (letter in string.ascii_uppercase)
		if direction == '>':
			return Particle(0, letter_to_int[letter], 1, 0)
		elif direction == '<':
			return Particle(self._width - 1, letter_to_int[letter], -1, 0)
		elif direction == 'v':
			return Particle(letter_to_int[letter], 0, 0, 1)
		elif direction == '^':
			return Particle(letter_to_int[letter], self._height - 1, 0, -1)
		else:
			assert False, "invalid direction"
	def _string_of_particle(self, particle):
		if particle.x < 0:
			return "<" + int_to_letter[particle.y]
		elif particle.x >= self._width:
			return ">" + int_to_letter[particle.y]
		elif particle.y < 0:
			return "^" + int_to_letter[particle.x]
		elif particle.y >= self._height:
			return "v" + int_to_letter[particle.x]
		else:
			assert False, "particle is still in the box"
	def _is_particle_in_box(self, particle):
		return (particle.x >= 0) and (particle.x < self._width) \
		   and (particle.y >= 0) and (particle.y < self._height)
	def simulate_with_trace(self, description):
		particle = self._particle_of_string(description)
		trace = set()
		while self._is_particle_in_box(particle):
			trace.add((particle.x, particle.y))
			particle = self[particle.x, particle.y].step(particle)
			if particle == None: return None, trace
		return self._string_of_particle(particle), trace
	def simulate(self, description):
		exit_desc, trace = self.simulate_with_trace(description)
		return exit_desc
	def simulate_nondeterministic_with_trace(self, description):
		particle = self._particle_of_string(description)
		possible_positions = { particle }
		previous_positions = set()
		while previous_positions != possible_positions:
			previous_positions = possible_positions
			new_positions_list = [
				self[particle.x, particle.y].step_nondeterministic(particle)
				for particle in previous_positions
				if self._is_particle_in_box(particle)
			]
			new_positions = functools.reduce(set.union, new_positions_list)
			possible_positions = previous_positions.union(new_positions)
		inside_box, outside_box = partition(self._is_particle_in_box,
											possible_positions)
		return set(map(self._string_of_particle, outside_box)), \
			   { (particle.x, particle.y) for particle in inside_box }
	def get_exits(self, description):
		particle = self._particle_of_string(description)
		possible_positions = { particle }
		previous_positions = set()
		while previous_positions != possible_positions:
			previous_positions = possible_positions
			new_positions_list = [
				self[particle.x, particle.y].step_nondeterministic(particle)
				for particle in previous_positions
				if self._is_particle_in_box(particle)
			]
			new_positions = functools.reduce(set.union, new_positions_list)
			possible_positions = previous_positions.union(new_positions)
		inside_box, outside_box = partition(self._is_particle_in_box,
											possible_positions)
		return set(map(self._string_of_particle, outside_box))

def build_interactively():
	def input_dimension(text):
		res = input(text)
		assert res.isdigit(), "invalid dimension"
		return int(res)
	width = input_dimension("width? ")
	height = input_dimension("height? ")
	mirrors = []
	holes = []
	elem_desc = input("element? ")
	while elem_desc:
		assert len(elem_desc) == 3, "invalid element description"
		x, y, kind = elem_desc
		assert x in string.ascii_uppercase, "invalid coordinate"
		assert y in string.ascii_uppercase, "invalid coordinate"
		x = letter_to_int[x]
		y = letter_to_int[y]
		if kind == 'o':
			holes.append((x, y))
		else:
			if kind == '/': mirror_obj = ForwardSlashMirror()
			elif kind == '\\': mirror_obj = BackSlashMirror()
			elif kind == '-': mirror_obj = HorizontalMirror()
			elif kind == '|': mirror_obj = VerticalMirror()
			elif kind == '#': mirror_obj = SquareMirror()
			else: assert False, "invalid element kind"
			mirrors.append((x, y, mirror_obj))
		elem_desc = input("element? ")
	transporters = []
	for idx, (x, y) in enumerate(holes):
		other_holes = holes[:idx] + holes[idx+1:]
		transporters.append((x, y, Transporter(other_holes)))
	return Box(width, height, mirrors + transporters)
#new function added after the TP3
#Similar logic from the test functions but that returns the new grid so that the rest
#of the program can run normally	
def build_automaticaly():
	width = random.randint(3,26)
	height = random.randint(3,26)
	mirror_kinds=[
		ForwardSlashMirror(),
		BackSlashMirror(),
		HorizontalMirror(),
		VerticalMirror(),
		SquareMirror()
		]
	mirrors = []
	holes = []
	transporters = []
	nb_elements = random.randint(1,(width * height)//4)
	nb_mirror = random.randint(1,nb_elements)
	#6 was a parameter test to reduce what was sometimes a really large quantity of transporters
	#can be elimitated without any impact on other functions
	nb_transp = min((nb_elements - nb_mirror),6)
	while len(mirrors)!=nb_mirror:
		x = random.randint(0,width)
		y = random.randint(0,height)
		mirror_obj = random.choice(mirror_kinds)
		repetition = False
		for i in range(len(mirrors)):
			if mirrors[i][0] == x and mirrors[i][1]==y : repetition = True
		if not(repetition): mirrors.append((x,y,mirror_obj))
	if nb_transp>=2:
		while len(holes) != nb_transp :
			x = random.randint(0,width)
			y = random.randint(0,height)
			repetition = False
			for (oldx,oldy) in holes:
				if x == oldx and y == oldy:
					repetition = True
			if not(repetition):holes.append((x,y))
		for idx, (x, y) in enumerate(holes):
			other_holes = holes[:idx] + holes[idx+1:]
			transporters.append((x, y, Transporter(other_holes)))
	return Box(width, height, mirrors + transporters)

#création d'un rayon d'entrée qui doit etre dans les dimensions qui respectent la grid crée avant
def random_entrance(new_grid):
	if bool(random.getrandbits(1)):
		#code pour entré de ray vertical
		xray = random.randint(0,new_grid.width-1)
		if bool(random.getrandbits(1)):
			yray = -1
			symbol = "v"
		else:
			yray = new_grid.height
			symbol = "^"
	else:
		#code pour entré de ray horizontal
		yray = random.randint(0,new_grid.height-1)
		if bool(random.getrandbits(1)):
			xray = -1
			symbol = ">"
		else:
			xray = new_grid.width
			symbol = "<"
	return (xray,yray,symbol)

def convert_ray(entry_ray,grid):
	if entry_ray[2] == ">" or entry_ray[2] == "<":
		return str(entry_ray[2]) + int_to_letter[entry_ray[1]]
	elif entry_ray[2] == "^" or entry_ray[2] == "v":
		return str(entry_ray[2]) + int_to_letter[entry_ray[0]]
		

import unittest
from hypothesis import given
import hypothesis.strategies as strats

DIRECTIONS = [
	(-1, 0),
	(0, -1),
	(0, 1),
	(1, 0)
]

DETERMINISTIC_CLASSES = [
	Aether,
	ForwardSlashMirror,
	BackSlashMirror,
	HorizontalMirror,
	VerticalMirror,
	SquareMirror
]

class TestParticle(unittest.TestCase):
	def _particle_or_none(self, x, y, dx, dy):
		try:
			return Particle(x, y, dx, dy)
		except AssertionError:
			return None
	@given(x=strats.integers(),
		   y=strats.integers())
	def test_constructor_error(self, x, y):
		self.assertEqual(self._particle_or_none(x, y, 3, 0), None)
		self.assertEqual(self._particle_or_none(x, y, 0, 0), None)
		self.assertEqual(self._particle_or_none(x, y, 0, -3), None)
	@given(x=strats.integers(),
		   y=strats.integers(),
		   dx_dy=strats.sampled_from(DIRECTIONS))
	def test_constructor_and_properties(self, x, y, dx_dy):
		dx, dy = dx_dy
		particle = Particle(x, y, dx, dy)
		self.assertEqual(particle.x, x)
		self.assertEqual(particle.y, y)
		self.assertEqual(particle.dx, dx)
		self.assertEqual(particle.dy, dy)
	def test_string(self):
		particle = Particle(3, 2, 1, 0)
		self.assertEqual(str(particle), "<3, 2, 1, 0>")
	def test_equal(self):
		particle1 = Particle(3, 2, 1, 0)
		particle2 = Particle(3, 2, 1, 0)
		particle3 = Particle(-3, -2, -1, 0)
		self.assertEqual(particle1, particle2)
		self.assertNotEqual(particle1, particle3)
		self.assertNotEqual(particle2, particle3)
	@given(x1=strats.integers(min_value = 0, max_value = 4),
		   y1=strats.integers(min_value = 0, max_value = 4),
		   dx_dy1=strats.sampled_from(DIRECTIONS),
		   x2=strats.integers(min_value = 0, max_value = 4),
		   y2=strats.integers(min_value = 0, max_value = 4),
		   dx_dy2=strats.sampled_from(DIRECTIONS),
		   x3=strats.integers(min_value = 0, max_value = 4),
		   y3=strats.integers(min_value = 0, max_value = 4),
		   dx_dy3=strats.sampled_from(DIRECTIONS))
	def test_eq_contract(self, x1, y1, dx_dy1, x2, y2, dx_dy2, x3, y3, dx_dy3):
		dx1, dy1 = dx_dy1
		dx2, dy2 = dx_dy2
		dx3, dy3 = dx_dy3
		particle1 = Particle(x1, y1, dx1, dy1)
		particle2 = Particle(x2, y2, dx2, dy2)
		particle3 = Particle(x3, y3, dx3, dy3)
		self.assertEqual(particle1, particle1)
		self.assertEqual(particle1 == particle2, particle2 == particle1)
		if particle1 == particle2:
			self.assertEqual(particle1 == particle3, particle2 == particle3)
			if particle1 == particle3:
				self.assertEqual(particle2, particle3)
	@given(x1=strats.integers(min_value = 0, max_value = 4),
		   y1=strats.integers(min_value = 0, max_value = 4),
		   dx_dy1=strats.sampled_from(DIRECTIONS),
		   x2=strats.integers(min_value = 0, max_value = 4),
		   y2=strats.integers(min_value = 0, max_value = 4),
		   dx_dy2=strats.sampled_from(DIRECTIONS))
	def test_hash_contract(self, x1, y1, dx_dy1, x2, y2, dx_dy2):
		dx1, dy1 = dx_dy1
		dx2, dy2 = dx_dy2
		particle1 = Particle(x1, y1, dx1, dy1)
		particle2 = Particle(x2, y2, dx2, dy2)
		if particle1 == particle2:
			self.assertEqual(hash(particle1), hash(particle2))

class TestDeterministicElements(unittest.TestCase):
	@given(x=strats.integers(),
		   y=strats.integers(),
		   dx_dy=strats.sampled_from(DIRECTIONS))
	def test_twice(self, x, y, dx_dy):
		dx, dy = dx_dy
		particle_in = Particle(x, y, dx, dy)
		for clss in DETERMINISTIC_CLASSES:
			instance = clss()
			particle_out = instance.step(instance.step(particle_in))
			self.assertEqual(particle_in.dx, particle_out.dx)
			self.assertEqual(particle_in.dy, particle_out.dy)

@strats.composite
def box_and_entry_point(draw):
	mirror_kinds=[
		ForwardSlashMirror(),
		BackSlashMirror(),
		HorizontalMirror(),
		VerticalMirror(),
		SquareMirror()
	]
	width = draw(strats.integers(min_value=3, max_value=26))
	height = draw(strats.integers(min_value=3, max_value=26))
	max_mirrors = max(1, (width * height) // 10)
	gen_x = strats.integers(min_value=0, max_value=width - 1)
	gen_y = strats.integers(min_value=0, max_value=height - 1)
	mirrors = draw(strats.lists(strats.tuples(gen_x, \
											  gen_y, \
											  strats.sampled_from(mirror_kinds)), \
								min_size=1, \
								max_size=max_mirrors))
	transporters = []
	if draw(strats.booleans()):
		holes = []
		x = draw(gen_x)
		y = draw(gen_y)
		holes.append((x,y))
		number = draw(strats.integers(min_value = 2, max_value = max_mirrors - len(mirrors)))
		#print(numbers)
		while len(holes) != number :
			newx = draw(gen_x)
			newy = draw(gen_y)
			repetition = False
			for (x,y) in holes:
				if x == newx and y == newy:
					repetition = True
			if not(repetition):holes.append((x,y))
		for idx, (x, y) in enumerate(holes):
			other_holes = holes[:idx] + holes[idx+1:]
			transporters.append((x, y, Transporter(other_holes)))
	else: 
		#la tirage au sort a dit de ne pas avoir des transporters
		pass 

	horizontal = draw(strats.booleans())
	if horizontal:
		entry_point=(">" if draw(strats.booleans()) else "<") + \
					int_to_letter[draw(gen_y)]
	else:
		entry_point=("^" if draw(strats.booleans()) else "v") + \
					int_to_letter[draw(gen_x)]
	return Box(width, height, mirrors + transporters), entry_point

def opposite_direction(direction_and_letter):
	direction, letter = direction_and_letter
	if direction == ">": return "<" + letter
	elif direction == "<": return ">" + letter
	elif direction == "^": return "v" + letter
	elif direction == "v": return "^" + letter
	else: assert False

class TestBox(unittest.TestCase):
	def test_empty(self):
		self.assertEqual(Box(3, 3, []).simulate(">C"), ">C")
	def test_mirrors(self):
		self.assertEqual(Box(3, 3, [(1, 2, ForwardSlashMirror())]).simulate(">C"), "^B")
		self.assertEqual(Box(3, 3, [(1, 2, BackSlashMirror())]).simulate(">C"), "vB")
		self.assertEqual(Box(3, 3, [(1, 2, HorizontalMirror())]).simulate(">C"), ">C")
		self.assertEqual(Box(3, 3, [(1, 2, VerticalMirror())]).simulate(">C"), "<C")
		self.assertEqual(Box(3, 3, [(1, 2, SquareMirror())]).simulate(">C"), "<C")
	def test_transporter(self):
		self.assertEqual(Box(3, 3, [(1, 2, Transporter([]))]).simulate(">C"), None)
	def test_transporters(self):
		box = Box(3, 3, [
			(1, 2, Transporter([(2, 1)])),
			(2, 1, Transporter([(1, 2)])),
		])
		self.assertEqual(box.simulate(">C"), ">B")
	@given(box_entry=box_and_entry_point())
	def test_det_and_nondet_agree(self, box_entry):
		box, entry_point = box_entry
		exit_point = box.simulate(entry_point)
		exit_points, trace = box.simulate_nondeterministic_with_trace(entry_point)
		self.assertTrue(exit_point in exit_points)
	@given(box_entry=box_and_entry_point())
	def test_return_to_entry_point(self, box_entry):
		box, first_entry_point = box_entry
		first_exit_point = box.simulate(first_entry_point)
		second_entry_point = opposite_direction(first_exit_point)
		second_exit_point = box.simulate(second_entry_point)
		self.assertEqual(opposite_direction(second_exit_point), first_entry_point)

if __name__ == '__main__':
	unittest.main()
