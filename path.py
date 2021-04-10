import numpy as np
from graph import Graph
import copy

class Path():

    """Objeto referente ao caminho unitario percorrido
    
    Args:
        init_node [int]: node de origem
    
    Attributes:
        path [list]: lista do caminho
        cost [list]: lista de custo
    
    """

    def __init__(self, init_node: int = 0):
        self.path = [init_node]
        self.cost = [0]

    def add(self, node: int, cost : int):

        """adicionar um node ao caminho
    
        Args:
            node [int]: node do grafo que se deseja adicionar
            cost [int]: O custo para chegar nesse node
        
        """

        self.path.append(node)
        self.cost.append(cost)
    
    def pop_node(self) -> int:
        """retira o ultimo nó da lista sem retornalo"""

        self.path.pop()
        self.cost.pop()
    
    def get_total_cost(self) -> int:
        return sum(self.cost)
    
    def get_current_node(self):
        try:
            return self.path[-1]
        except:
            return None
        
