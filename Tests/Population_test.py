import unittest
from Population import Population
from MatrixDistance import MatrixDistance


class TestClassPopulation(unittest.TestCase):
    def test_gen_individu(self):
        nb = 40
        dist = 100
        distmax = 5000

        p = Population(nb, dist, distmax)
        self.assertEqual(len(p._individus), nb)
        for individu in p._individus:
            self.assertEqual(len(individu.listin), dist)
            individu.listin.sort()
            self.assertTrue(individu.distance <= distmax*dist)
            for i in range(0, len(individu.listin)):
                self.assertEqual(i, individu.listin[i])

    def test_gen_npopulation(self):
        nbctrl = 5
        nb = 40
        dist = 100
        distmax = 5000
        nbMutate = 20

        for i in range(0, nbctrl):
            p = Population(nb, dist, distmax)
            bis = p.get_best_ind()

            for i in range(0, nbMutate):
                p.gen_new_population(nb)
                if(p.np_is_better()):
                    p.use_new_population()
                    self.assertTrue((bis.distance) >= (p.get_best_ind().distance))
                    bis = p.get_best_ind()
