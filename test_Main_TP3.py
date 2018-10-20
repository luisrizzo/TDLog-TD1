 #Ecole Nationale des Ponts et Chaussées
#Techniques de Développement Logiciel
#TP 3
#Fait par Luis Augusto YOKOTA RIZZO
#      et Daniel Toshihiro OKANE
#
#Les tests que nous avons mis comme commentaires nous n'avons pas réussi à les mettre en place. Dans les
#deux cas, il a eu un problème de: 'tuple' object has no attribute 'x'.
#
#Pour les tests de aléatoires, nous avons eu des problèmes pour l'installation de la bibliothèque de hypothesis.

from unittest.mock import patch
import unittest
import Main_TP3

class TestObjects(unittest.TestCase):

    def test_step_ForwardSlashMirror(self):
        o = Main_TP3.ForwardSlashMirror()
        p_v = o.step(Main_TP3.Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(1, 2, -1, 0,1))
        p_h = o.step(Main_TP3.Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(2, 1, 0, -1,1))
        
    def test_step_BackSlashMirror(self):
        o = Main_TP3.BackSlashMirror()
        p_v = o.step(Main_TP3.Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(3, 2, 1, 0,1))
        p_h = o.step(Main_TP3.Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(2, 3, 0, 1,1))
       
    def test_step_HorizontalhMirror(self):
        o = Main_TP3.HorizontalMirror()
        p_v = o.step(Main_TP3.Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(2, 1, 0, -1,1))
        p_h = o.step(Main_TP3.Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(3, 2, 1, 0,1))
        
    def test_step_VerticalMirror(self):
        o = Main_TP3.VerticalMirror()
        p_v = o.step(Main_TP3.Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(2, 3, 0, 1,1))
        p_h = o.step(Main_TP3.Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(1, 2, -1, 0,1))
        
    def test_step_SquareMirror(self):
        o = Main_TP3.SquareMirror()
        p_v = o.step(Main_TP3.Particle(2,2,0,1,0))
        self.assertEqual((p_v.x,p_v.y,p_v.dx,p_v.dy,p_v.p),(2, 1, 0, -1,1))
        p_h = o.step(Main_TP3.Particle(2,2,1,0,0))
        self.assertEqual((p_h.x,p_h.y,p_h.dx,p_h.dy,p_h.p),(1, 2, -1, 0,1))
        
    '''def test_step_Transporter(self):
        o = Main_TP3.Transporter([[1,2],[3,3],[4,3]])
        global list_of_entries
        print(list_of_entries)
        #list_of_entries = [Main_TP3.Particle(1,3,0,1,1),Main_TP3.Particle(3,4,0,1,1),Main_TP3.Particle(4,4,0,1,1)]
        p = o.step(Main_TP3.Particle(2,2,0,1,0))
        self.assertEqual((p.x,p.y,p.dx,p.dy,p.p),(1, 3, 0, 1,1))'''


class TestEntries(unittest.TestCase):     
    def test_AllEntries(self):
        p = Main_TP3.Particle(2,2,0,1,0)
        transporters_list=[[1,2],[3,3],[4,3]]
        e_list = Main_TP3.All_entries(p,transporters_list)
        for i in range(len(e_list)):
            e_list[i]=e_list[i].identity
        expected_e_list = [Main_TP3.Particle(1,3,0,1,1).identity,Main_TP3.Particle(3,4,0,1,1).identity,Main_TP3.Particle(4,4,0,1,1).identity]
        self.assertEqual(e_list,expected_e_list)
    
    '''def test_AllExits(self):
        user_input = ['26','26','BBo','CCo','','>B']
        expected_exits={'>C':1}
        with patch('builtins.input', side_effect=user_input):
            exits = Main_TP3.All_exits()
        self.assertEqual(exits, expected_exits)'''
        
if __name__ == '__main__' :
    unittest.main()