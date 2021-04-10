from graph import Graph
from path import Paths, Path
import random
from genetic import Genetic


genetic = Genetic(0,[1])
# print(genetic.find_path2(0,6))

genetic.populate(3000)
pop = genetic.return_paths()
print(pop.get_paths())

