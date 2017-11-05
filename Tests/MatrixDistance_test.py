import unittest
from MatrixDistance import MatrixDistance


class TestClassMatrixDistance(unittest.TestCase):
    def test_create(self):
        qty = 4
        distMax = 100
        d = MatrixDistance(qty, distMax)
        for i in range(0, qty):
            self.assertEqual(d._matrixDist[i, i], 0)
            for j in range(0, qty):
                self.assertEqual(d._matrixDist[i, j], d._matrixDist[j, i])

    def test_calc_dist(self):
        qty = 5
        distMax = 100
        suite = [0, 1, 3, 4, 2]
        d = MatrixDistance(qty, distMax)

        d._matrixDist[0, 1] = 2
        d._matrixDist[1, 3] = 3
        d._matrixDist[3, 4] = 4
        d._matrixDist[4, 2] = 5
        self.assertEqual(d.calc_dist(suite), 14)

        suite = [0, 1, 4, 2, 3]
        d._matrixDist[1, 4] = 10
        d._matrixDist[4, 2] = 6
        d._matrixDist[2, 3] = 2
        self.assertEqual(d.calc_dist(suite), 20)
