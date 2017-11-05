import random as rdm
from MatrixDistance import MatrixDistance
from Individu import Individu
from Proba import Proba
from RdmList import RdmList

class Population:
    def __init__(self, nbInd, nbDist, distmax = 500, pmin=0.15, pmax=0.85):
        self._proba = Proba(pmin, pmax)
        self._mdist = MatrixDistance(nbDist, distmax)
        self._individus = []
        distmin = self._mdist.getMax()*self._mdist.getNbDist()
        distmax = 0
        for i in range(0, nbInd):
            ind = Individu(RdmList.gen_rdm_list([x for x in range(1, nbDist-1)], 0, nbDist-1))
            ind.distance = self._mdist.calc_dist(ind.listin)
            distmax = max(ind.distance, distmax)
            distmin = min(ind.distance, distmin)
            self._individus.append(ind)
        self._proba.vmin(distmin)
        self._proba.vmax(distmax)
        self._best_ind = self._individus[0]
        self._badest_ind = self._individus[0]
        for i in range(0, nbInd):
            self._individus[i].proba = self._proba.calcule(self._individus[i].distance)
            if self._best_ind.distance > self._individus[i].distance:
                self._best_ind = self._individus[i]
            if self._badest_ind.distance < self._individus[i].distance:
                self._badest_ind = self._individus[i]

    def gen_new_population(self, nbInd):
        self._nindividus = []
        distmin = self._mdist.getMax()*self._mdist.getNbDist()
        distmax = 0
        while(len(self._nindividus) < nbInd):
            i1 = self._individus[rdm.randrange(0, len(self._individus))]
            i2 = self._individus[rdm.randrange(0, len(self._individus))]
            if((rdm.random() <= i1.proba) & (rdm.random() <= i2.proba) & (i1 != i2)):
                ind = Individu.mutate(i1, i2)
                ind.distance = self._mdist.calc_dist(ind.listin)
                distmax = max(ind.distance, distmax)
                distmin = min(ind.distance, distmin)
                self._nindividus.append(ind)
        self._proba.vmin(distmin)
        self._proba.vmax(distmax)
        self._nbest_ind = self._nindividus[0]
        self._nbadest_ind = self._nindividus[0]
        for i in range(0, nbInd):
            self._nindividus[i].proba = self._proba.calcule(self._nindividus[i].distance)
            if self._nbest_ind.distance > self._nindividus[i].distance:
                self._nbest_ind = self._nindividus[i]
            if self._nbadest_ind.distance < self._nindividus[i].distance:
                self._nbadest_ind = self._nindividus[i]

    def use_new_population(self):
        self._individus = self._nindividus
        self._best_ind = self._nbest_ind
        self._badest_ind = self._nbadest_ind
        self._nindividus = []
        self._nbest_ind = None
        self._nbadest_ind = None

    def np_is_better(self):
        return (self._nbest_ind.distance <= self._best_ind.distance)

    def get_best_ind(self):
        return self._best_ind

    def get_badest_ind(self):
        return self._badest_ind

    def __str__(self):
        s = ""
        for i in range(0, len(self._individus)):
            s += str(self._individus[i]) + '\n'
        return s
