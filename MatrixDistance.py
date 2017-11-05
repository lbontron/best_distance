#!/usr/bin/env python
import random as rdm


class MatrixDistance:
    def __init__(self, nb=20, dist_max=500):
        self._matrixDist = {}
        self._distmax = dist_max
        self._nbdist = nb
        for i in range(0, nb):
            self._matrixDist[i, i] = 0
            for j in range(i + 1, nb):
                self._matrixDist[i, j] = rdm.randrange(dist_max)
                self._matrixDist[j, i] = self._matrixDist[i, j]

    def calc_dist(self, listin):
        dist = 0
        for i in range(1, len(listin)):
            dist = dist + self._matrixDist[listin[i-1], listin[i]]
        return dist

    def getMax(self):
        return self._distmax

    def getNbDist(self):
        return self._nbdist
