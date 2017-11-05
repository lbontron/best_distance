import unittest
from Proba import Proba
import numpy as np


class TestClassProba(unittest.TestCase):
    def test_create(self):
        p = Proba(0.15, 0.85, 126, 500)
        self.assertEqual(np.round(p.a + 7/3740, 10), 0)
        self.assertEqual(np.round(p.b - 4061/3740, 10), 0)
        self.assertEqual(np.round(p.calcule(126), 10), 0.85)
        self.assertEqual(np.round(p.calcule(500), 10), 0.15)

        p1 = Proba(0.15, 0.85)
        p1.vmin(126)
        p1.vmax(500)
        self.assertEqual(np.round(p1.a + 7/3740, 10), 0)
        self.assertEqual(np.round(p1.b - 4061/3740, 10), 0)
        self.assertEqual(np.round(p1.calcule(126), 10), 0.85)
        self.assertEqual(np.round(p1.calcule(500), 10), 0.15)

        p2 = Proba(0.15, 0.85)
        p2.vmax(500)
        p2.vmin(126)
        self.assertEqual(np.round(p2.a + 7/3740, 10), 0)
        self.assertEqual(np.round(p2.b - 4061/3740, 10), 0)
        self.assertEqual(np.round(p2.calcule(126), 10), 0.85)
        self.assertEqual(np.round(p2.calcule(500), 10), 0.15)
