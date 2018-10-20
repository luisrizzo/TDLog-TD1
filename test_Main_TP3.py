import unittest
import Main_TP3

class TestMirrors(unittest.TestCase):

    def test_step_ForwardSlashMirror(self):
        o = ForwardSlashMirror()
        p_v = o.step(Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(1, 2, -1, 0,1))
        p_h = o.step(Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(2, 1, 0, -1,1))
        
    def test_step_BackSlashMirror(self):
        o = BackSlashMirror()
        p_v = o.step(Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(3, 2, 1, 0,1))
        p_h = o.step(Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(2, 3, 0, 1,1))
       
    def test_step_HorizontalhMirror(self):
        o = HorizontalMirror()
        p_v = o.step(Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(2, 1, 0, -1,1))
        p_h = o.step(Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(3, 2, 1, 0,1))
        
    def test_step_VerticalMirror(self):
        o = VerticalMirror()
        p_v = o.step(Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(2, 3, 0, 1,1))
        p_h = o.step(Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(1, 2, -1, 0,1))
        
    def test_step_SquareMirror(self):
        o = SquareMirror()
        p_v = o.step(Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(2, 1, 0, -1,1))
        p_h = o.step(Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(1, 2, -1, 0,1))

        
class TestBuilder(unittest.TestCase):        
    
    def test_build_interactively(self):
        user_input = ['26','26','BBo','BDo','CC/','CDo','ED#',]
        expected_box = []
        expected_transporters = []
        expected_holes = []
        
        Main_TP3.build_interactively()
        
        self.assertEqual(mirrors, expected_mirrors)
        self.assertEqual(transporters, expected_transporters)
        self.assertEqual(holes, expected_holes)
        
if __name__ == '__main__' :
    unittest.main()