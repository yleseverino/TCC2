from graph import Graph
from path import Paths, Path
import random

class Genetic():

    def __init__(self,node_init,nodes_dest):
        self.graph = Graph()
        self.paths = Paths()
        self.node_init = node_init
        self.nodes_dest = nodes_dest
    
    def find_path(self):
        path = Path()
        path.add(self.node_init, 0)
        already_visited = [self.node_init]
        while True:
            next_node = self.graph.return_random_next(already_visited)
            if not next_node:
                break
            cost_next = self.graph.return_cost_next(already_visited[-1], next_node)
            path.add(next_node,cost_next)
            already_visited.append(next_node)    
            if all(elem in already_visited for elem in self.nodes_dest):
                self.paths.add(path)
                break

    def populate(self, ind_number):
        self.paths = Paths()
        for i in range(ind_number):
            self.find_path()
    
    def return_paths(self):
        return self.paths