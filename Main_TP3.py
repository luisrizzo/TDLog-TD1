#Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 3
#Fait par Luis Augusto YOKOTA RIZZO
#      et Daniel Toshihiro OKANE

#!/usr/bin/env python

import random
import string
import unitest
import doctest

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
                        particle.dy)

class ForwardSlashMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '/'
    def step(self, particle):
        dx = -particle.dy
        dy = -particle.dx
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class BackSlashMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '\\'
    def step(self, particle):
        dx = particle.dy
        dy = particle.dx
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class HorizontalMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '-'
    def step(self, particle):
        dx = particle.dx
        dy = -particle.dy
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class VerticalMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '|'
    def step(self, particle):
        dx = -particle.dx
        dy = particle.dy
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

class SquareMirror:
    def __init__(self):
        pass
    @property
    def char_representation(self):
        return '#'
    def step(self, particle):
        dx = -particle.dx
        dy = -particle.dy
        return Particle(particle.x + dx, particle.y + dy, dx, dy)

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

box = build_interactively()
print(box)
exit_point, trace = box.simulate_with_trace(input("entry point? "))
print("exit point:", exit_point)
print(box.string_with_trace(trace))
