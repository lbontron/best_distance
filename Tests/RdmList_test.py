import unittest
from RdmList import RdmList

class TestClassRdmList(unittest.TestCase):
    def test_create(self):
        nb = 10
        l = RdmList.gen_rdm_list([x for x in range(1, nb - 1)], 0, nb-1)
        l.sort()
        for i in range(0, len(l)):
            self.assertEqual(i, l[i])
