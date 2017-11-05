#!/usr/bin/env python
import random as rdm

class Individu:
    def __init__(self, listin, distance=None, proba=-1):
        self.listin = listin
        self.distance = distance
        self.proba = proba

    def selfmutate(self, ind):
        self = Individu.mutate(self, ind)

    def __str__(self):
        if len(self.listin) <= 16:
            return "ind : l = " + str(self.listin) + ", d = " + str(self.distance) + ", p = " + str(self.proba)
        else:
            return "ind : l = <listin:" + str(len(self.listin)) + ">, d = " + str(self.distance) + ", p = " + str(self.proba)

    @staticmethod
    def mutate(ind1, ind2):
        l = [i for i in range(0, len(ind1.listin))]
        res = []
        tmp = list(ind1.listin)
        for i in range(0, len(ind1.listin)):
            if rdm.randrange(0, 2) == 0:
                res.append(ind1.listin[i])
            else:
                res.append(ind2.listin[i])
            try:
                tmp.remove(res[i])
            except:
                res[i] = -1
            finally:
                pass
        for i in range(0, len(res)):
            if res[i] == -1:
                nb = rdm.randrange(0, len(tmp))
                res[i] = tmp[nb]
                del tmp[nb]
        ni = Individu(res)
        return ni