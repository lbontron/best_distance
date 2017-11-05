import random as rdm
import copy as cp

class RdmList:
    @staticmethod
    def gen_rdm_list(listin, starter=None, endler=None):
        list_res = cp.deepcopy(listin)
        rdm.shuffle(list_res)
        if starter is not None:
            list_res.insert(0, starter)
        if endler is not None:
            list_res.append(endler)
        return list_res

    @staticmethod
    def gen_list_rdm_list(qty, listin, starter=None, endler=None):
        list_res = []
        for i in range(0, qty):
            list_res.append(RdmList.gen_rdm_list(listin, starter, endler))
        return list_res