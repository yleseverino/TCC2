import numpy as np
import random

class Graph:
    
    """Este objeto representa o grafo, com ele é possivel pegar os custo das cotas, a principio o grafo deve ser completo
    
    Args:
        number_of_nodes [int]: é o numeros de nós que tera o grafo,
        filename [str]: é o nome do arquivo .npy (binarios de numpy) para carregar no objeto
    
    Attributes:
        number_of_nodes [int]: numero de node - 1 para assim ter um contagem de 0 ao total
        edges [numpy.ndarray]: é a matriz de custos do meu grafo
    
    """

    def __init__(self, number_of_nodes: int = 0, filename: str = 'eil51.tsp'):

        if filename:
            self.load(filename)

        # TODO Criação de grafo manual
        elif number_of_nodes:
            self.number_of_nodes = number_of_nodes
            self.edges = np.full((number_of_nodes, number_of_nodes), 999)
        else:
            Exception('Sem numero de nós definido e sem nome de arquivo definido tb')
    
    def add_cost(self, node_from: int, node_to: int, cost: int):

        """metodo para alterar ou adicionar o custo de uma rota no grafo
    
        Args:
            node_from [int]: node origem no grafo,
            node_to node [int]: de destino,
            cost [int]: custo a ser adicionado
    
        """
        if node_from == node_to:
            Exception('Não se pode conectar o mesmo ponto')
        if (node_from > (self.number_of_nodes - 1)) or (node_to > (self.number_of_nodes - 1)) or (node_from < 0) or (node_to < 0):
            Exception('ponto inexistente')

        self.edges[node_from,node_to] = cost
    
    def get_cost(self, node_from, node_to) -> int:
        """Pega o custo de um node para o outro
        *se o node de origen ou destino não existir então sera considerado o node de origem,
        isso é util para o algoritmo de cross over SCX
    
        Args:
            node_from [int]: node origem no grafo
            node_to node [int]: de destino

        return:
            [int]: custo para chegar nesse node
    
        """
        try:
            return self.edges[node_from, node_to]
        except IndexError:
            if node_from > self.number_of_nodes:
                return self.edges[0,node_to]
            else:
                return self.edges[node_from,0]
    
    def save(self, filename):
        '''Salva o grafo na pasta graphs'''

        with open(f'graphs/{filename}.npy', 'wb') as f:
            np.save(f,self.edges)
    
    def load(self, filename):
        with open(f'graphs/{filename}.npy', 'rb') as f:
            self.edges = np.load(f)
            self.number_of_nodes = len(self.edges) - 1
    
    
    
    def return_random_next_not_zero(self, already_visited) -> int:
        """Retorna um possivel proximo node não randomico
        
        return:
            [int]: valor do nó
            [None]: Se não encontrar um node possivel (visitou todos os nodes)
        """

        possibles = [i for i in range(1,self.number_of_nodes + 1)]
        return_possibles = []
        for node in possibles:
            if node not in already_visited:
                return_possibles.append(node)
        if not return_possibles:
            return None
        return random.choice(return_possibles)
    
    def return_all_possibles_nodes(self, already_visited: list) -> list:
        """retorna todos os nodes possivel para ser adicionado ao caminho

        Args:
            
        
        return:
            [list]: lista com os nodes
        """
        possibles = [i for i in range(1,self.number_of_nodes)]
        print(possibles)
        return_possibles = []
        for node in possibles:
            if node not in already_visited:
                return_possibles.append(node)
        return return_possibles

    # def return_cost_next(self, current_node, next_node) -> int:
    #     return self.edges[current_node][next_node]
    
    # def return_random_next(self, already_visited):
    #     try:
    #         possibles = np.where(self.edges[already_visited[-1]] != 999 )[0]

    #     except IndexError:
    #         for i in range(len(already_visited)):
    #             if already_visited[i]  >= self.number_of_nodes:
    #                 already_visited[i] = 0

    #         possibles = np.where(self.edges[already_visited[-1]] != 999 )[0]
    #     return_possibles = []
    #     for node in possibles:
    #         if node not in already_visited:
    #             return_possibles.append(node)
    #     if not return_possibles:
    #         return None
    #     return random.choice(return_possibles)
