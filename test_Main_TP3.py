import unittest
import Main_TP3

class TestCalc(unittest.TestCase):

	def test_step(self):
		o = ForwardSlashMirror()
		p = o.step(Particle(2,2,0,1,0))
		self.assertEqual(print(p.x,",",p.y),print(1,2))
		#o1 = ForwardSlashMirror()
		#p1 = o1.step(Particle(2,2,0,1,0))
		#self.assertEqual(p , Particle(1, 2, -1, 0,1))

if __name__ == '__main__' :
	unittest.main()