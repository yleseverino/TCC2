import numpy as np
from graph import Graph
from path import Path
from copy import copy

class Ind():

    """Esse objeto representa os indivíduo do problema, ou seja nele é possivel definir o numero de carros e o nó de inicio do problema
    além de ser responsável para encontrar de forma aléatoria um solução para o problema
    
    Args:
        numbers_cars [int]: Numero de carros para o problema
        graph [Graph]: é o objeto do grafo do problema
    
    Attributes:
        number_of_nodes [int]: numero de node - 1 para assim ter um contagem de 0 ao total
        edges [numpy.ndarray]: é a matriz de custos do meu grafo
    
    """

    def __init__(self, numbers_cars: int, graph: type(Graph) = Graph(), init_node: int = 0):
        self.numbers_cars = numbers_cars
        self.init_node = init_node

        self.paths = [Path(init_node) for i in range(numbers_cars)]
        self.paths_cost = []
        self.paths_real = []

        self.total_cost = 0
        self.all_nodes_visited_paths = [0]
        self.graph = graph

    def random_append_new_node(self):
        """Adiciona um node para cada caminho
        
        Returns:
            [boolean]: True para foi possivel adicionar e False quando terminou de prencher os caminhos
        """
        for car in self.paths:
                next_node = self.graph.return_random_next_not_zero(already_visited = self.all_nodes_visited_paths)
                if next_node == None:
                    return False
                cost_next = self.graph.get_cost(car.get_current_node(),next_node)
                car.add(next_node,cost_next)
                self.all_nodes_visited_paths.append(next_node)
        return True
    
    def find_path(self):
        self.paths = [Path(self.init_node) for i in range(self.numbers_cars)]
        self.all_nodes_visited_paths = [0]
        finding = True
        while finding:
            finding = self.random_append_new_node()

        return self.convert_mtsp_to_tsp()
    
    def convert_mtsp_to_tsp(self):
        '''Nessa funcção eu pego os caminhos dos carros e converto como se fosse somente um caixeiro viagante,
        para fazer isso devo adicionar um novo node ficticion que sua distancia deve ser o mesmo com a origem'''

        path_mixed = [0]
        cost_mixed = [0]
        for car in self.paths:
            path_mixed.extend(car.path[1::])
            cost_mixed.extend(car.cost[1::])

            current_node = car.path[-1]
            next_node = max(self.all_nodes_visited_paths) + 1
            self.all_nodes_visited_paths.append(next_node)
            cost_node = self.graph.get_cost(current_node, next_node)

            path_mixed.append(next_node)
            cost_mixed.append(cost_node)

        return path_mixed[:-1], cost_mixed[:-1], sum(cost_mixed[:-1])
    
    def calc_total_cost(self):
        self.total_cost = 0
        self.paths_cost = []
        for car in self.paths:
            self.paths_cost.append(car.get_total_cost())
            self.total_cost += int(car.get_total_cost())