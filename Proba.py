
class Proba:
    def __init__(self, pmin, pmax, vmin=0, vmax=0):
        self._pmin = pmin
        self._pmax = pmax
        self._vmin = vmin
        self._vmax = vmax
        self.updateab()

    def calcule(self, val):
        return val*self.a + self.b


    def vmin(self, value):
        self._vmin = value
        self.updateab()


    def vmax(self, value):
        self._vmax = value
        self.updateab()

    def updateab(self):
        if (self._vmin - self._vmax) != 0:
            self.a = (self._pmax - self._pmin)/(self._vmin - self._vmax)
            self.b = self._pmax - ((self._pmax - self._pmin)/(self._vmin - self._vmax))*self._vmin
        else:
            self.a = 0
            self.b = 0