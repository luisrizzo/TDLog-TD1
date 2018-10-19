 #Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 3
#Fait par Luis Augusto YOKOTA RIZZO
#      et Daniel Toshihiro OKANE

#1- Non-deterministique
#A chaque fois que la particule entre dans un transporteur on va faire deux choses :
#1- Elle va sortir dans le premier transporteur de la liste de possibilités
#2- Tous les autres possibilités de sortie seront enregistrés comme des nouvelles particules qui seront mises dans le système
#Donc la particule sur 1 continue son trajet jusqu'à la fin, quand une liste des sorties va recevoir ce valeur
#Quand 1 est sortie du système les particules de 2 seront mises dans le système
#
#Pour éviter des boucles infinis on va établir un système de parcours maximum d'une particule
#Ce limite serait égal à width * height 
# ABCDEF
#A o    A
#B  o  oB
#C  o  oC
#D      D
#E      E
#F      F
# ABCDEF
#Une particule qui a une entré >A peut entrer dans AB, sortir vers BC, entrer dans BF, sortir CC, entrer CF et recommencer le parcours à BC, etc,etc

#2a -Tests:
#On a mis quelques doctests dans des methodes simples pour faire les tests unitaires
#On a aussi des tests d'intégration faites dans la simulation et construction de la matrice
#2b - Tests aléatoires avec Hypothesis :
#Surtout pour des tests de validation


#!/usr/bin/env python

import random
import string
import unittest
import doctest

#from hypothesis import given
#from hypothesis.strategies import text

int_letter_couples = list(zip(range(0, len(string.ascii_uppercase)),
							  string.ascii_uppercase))
int_to_letter = { int:letter for (int, letter) in int_letter_couples }
letter_to_int = { letter:int for (int, letter) in int_letter_couples }
list_of_entries = []

class Particle:
	def __init__(self, x, y, dx, dy,p_counter):
		assert (dx in {-1, 0, 1}) and (dy in {-1, 0, 1}), "invalid dx/dy"
		assert (dx != 0) or (dy != 0), "invalid dx/dy"
		self._x = x
		self._y = y
		self._dx = dx
		self._dy = dy
		self._p = p_counter
	@property
	def x(self): return self._x
	@property
	def y(self): return self._y
	@property
	def dx(self): return self._dx
	@property
	def dy(self): return self._dy
	@property
	def p(self): return self._p
	def __str__(self):
		return "<{}, {}, {}, {}>".format(self._x, self._y, self._dx, self._dy)

class Aether:
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return ' '
	def step(self, particle):
		return Particle(particle.x + particle.dx,
				particle.y + particle.dy,
				particle.dx,
				particle.dy,
				particle.p+1)

class ForwardSlashMirror:
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '/'
	def step(self, particle):
		dx = -particle.dy
		dy = -particle.dx
		return Particle(particle.x + dx, particle.y + dy, dx, dy, particle.p+1)
		"""Test if step is working fine
		o = ForwardSlashMirror()
		p = Particle (2,2,0,1,0)
		print(o.step(p))
		>>> Particle(1, 2, -1, 0,1)
		"""

		"""Test if step is working fine
		o = ForwardSlashMirror()
		p = o.step(Particle(2,2,0,1,0))
		print(print(p.x,",",p.y))
		>>> (1, 2)
		"""
class BackSlashMirror:
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '\\'
	def step(self, particle):
		dx = particle.dy
		dy = particle.dx
		return Particle(particle.x + dx, particle.y + dy, dx, dy, particle.p+1)

class HorizontalMirror:
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '-'
	def step(self, particle):
		dx = particle.dx
		dy = -particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy, particle.p+1)
class VerticalMirror:
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '|'
	def step(self, particle):
		dx = -particle.dx
		dy = particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy, particle.p+1)

class SquareMirror:
	def __init__(self):
		pass
	@property
	def char_representation(self):
		return '#'
	def step(self, particle):
		dx = -particle.dx
		dy = -particle.dy
		return Particle(particle.x + dx, particle.y + dy, dx, dy, particle.p+1)

class Transporter:
	def __init__(self, o):
		self._outputs = o
	@property
	def char_representation(self):
		return 'o'
	def step(self, particle):
		if len(self._outputs) > 0:
			All_entries(particle,self._outputs)
			dx = particle.dx
			dy = particle.dy
			x, y = (self._outputs[0])
			if particle.x != x and particle.y != y:
				return Particle(x + dx, y + dy, dx, dy, particle.p+1)
			else:
				return None
		else:
			return None

class Box:
	def __init__(self, width, height, elements):
		assert (width >= 3) and (width <= 26), "invalid width"
		assert (height >= 3) and (height <= 26), "invalid height"
		self._width = width
		self._height = height
		self._grid = dict()
		for (x, y, element) in elements:
			self._grid[x, y] = element
		self._maxp = self._height * self._width
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
	def _particle_of_string(self, description,p_counter):
		assert (len(description) == 2)
		direction, letter = description
		assert (letter in string.ascii_uppercase)
		if direction == '>':
			return Particle(0, letter_to_int[letter], 1, 0, 0)
		elif direction == '<':
			return Particle(self._width - 1, letter_to_int[letter], -1, 0, 0)
		elif direction == 'v':
			return Particle(letter_to_int[letter], 0, 0, 1,0)
		elif direction == '^':  
			return Particle(letter_to_int[letter], self._height - 1, 0, -1,0)
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

	def simulate_with_trace(self, description,p_counter):
		particle = self._particle_of_string(description,p_counter)
		trace = set()
		list_of_exits = []
		exits, trace = self.simulate_nondeterministic(particle)
		list_of_exits.append(exits)
		for all_particles in list_of_entries:
			exits, trace = self.simulate_nondeterministic(all_particles)
			list_of_exits.append(exits)
		return list_of_exits, trace

	def simulate_nondeterministic(self,particle):
		trace = set()
		while self._is_particle_in_box(particle) and particle.p < self._maxp:
			trace.add((particle.x, particle.y))	
			particle = self[particle.x, particle.y].step(particle)
			if particle == None: return None, trace
		exit_symbols = (self._string_of_particle(particle))
		return exit_symbols , trace
	def simulate(self, description):
		exit_desc, trace = self.simulate_with_trace(description)
		return exit_desc

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

def All_entries(particle,transporters_list):
	global list_of_entries
	dx = particle.dx
	dy = particle.dy
	for i in range(len(transporters_list)):
		x, y = (transporters_list[i])
		if particle.x != x and particle.y != y and i != 0:
			list_of_entries.append(Particle(x+dx,y+dy,dx,dy,particle.p+1))
	return None


def All_exits ():
	box = build_interactively()
	print(box)
	list_of_exits, trace = box.simulate_with_trace(input("entry point?"),0)
	print(box.string_with_trace(trace))
	print("exit points:", list_of_exits)

