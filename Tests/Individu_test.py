import unittest
from Individu import Individu
import random as rdm


class TestClassIndividu(unittest.TestCase):
    def test_gen_individu(self):
        nb = 10
        listin = [x for x in range(0, nb)]
        rdm.shuffle(listin)
        i = Individu(listin)
        i.listin.sort()
        for j in range(0, nb):
            self.assertEqual(j, i.listin[j])

    def test_mutate(self):
        nb = 10
        listin = [x for x in range(0, nb)]
        rdm.shuffle(listin)
        i0 = Individu(listin)
        listin = [x for x in range(0, nb)]
        rdm.shuffle(listin)
        i1 = Individu(listin)
        i2 = Individu.mutate(i0, i1)
        i2.listin.sort()
        for j in range(0, nb):
            self.assertEqual(j, i2.listin[j])
