from Population import Population
from MatrixDistance import MatrixDistance

nbRdmPath = 40
nbCity = 100
distMax = 5000
nbMutateMax = 20

p = Population(nbRdmPath, nbCity, distMax)
bestPath = p.get_best_ind()
print(bestPath)

for i in range(0, nbMutateMax):
    p.gen_new_population(nbRdmPath)
    if(p.np_is_better()):
        p.use_new_population()
        self.assertTrue((bestPath.distance) >= (p.get_best_ind().distance))
        bestPath = p.get_best_ind()
        print(bestPath)



