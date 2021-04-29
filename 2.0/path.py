import numpy as np
from graph import Graph
import copy
from typing import Type

class Path():

    """Objeto referente ao caminho unitario percorrido
    
    Args:
        init_node [int]: node de origem
    
    Attributes:
        path [list]: lista do caminho
        cost [list]: lista de custo
    
    """

    def __init__(self, init_node: int = 0, graph : Type[Graph] = Graph()):
        self.path = [init_node]
        self.cost = [0]
        self.graph = graph
    
    def create_path(self, path_route):
        """Cria um caminho com o path route"""

        self.path = path_route
        self.cost = [0]
        for i in range(len(self.path) - 1):
            self.cost.append(self.graph.get_cost(self.path[i], self.path[i+1]))
    
    def get_total_cost(self) -> int:
        return sum(self.cost)
    
    def get_current_node(self):
        try:
            return self.path[-1]
        except:
            return self.path[0]

    def add(self, node: int, cost : int):
        """adicionar um node ao caminho
    
        Args:
            node [int]: node do grafo que se deseja adicionar
            cost [int]: O custo para chegar nesse node
        """

        self.path.append(node)
        self.cost.append(cost)
    
    def pop_node(self) -> int:
        """retira o ultimo nó da lista sem retornar ele"""

        self.path.pop()
        self.cost.pop()
    
    def add_random_next(self):
        """adiciona um node possivel para o caminha aleatoriamente
        
        return:
            [boolean]: True se foi possivel adicionar false se não
        """

        next_node = self.graph.return_random_next_not_zero()
        if next_node is not None:
            cost_next = self.graph.return_cost_next(self.path[-1],next_node)
            self.path.append(next_node)
            self.cost.append(cost_next)
            return True

        return False
    
    def return_all_possibles(self):
        """adiciona um node possivel para o caminha aleatoriamente
        
        return:
            [boolean]: True se foi possivel adicionar false se não
        """

        next_node = self.graph.return_random_next_not_zero()
        if next_node is not None:
            cost_next = self.graph.return_cost_next(self.path[-1],next_node)
            self.path.append(next_node)
            self.cost.append(cost_next)
            return True

        return False
    

        
