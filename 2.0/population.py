from ind import Ind
from copy import copy


class Population():

    """Objeto referente a população de carros
    
    Args:
        number_cars [int]: numero de carros que cada indivíduo da população deve ter.
    
    Attributes:
        cost [list]: lista com o custo de node a node de um indivíduo
        total_cost [list]: lista com o custo total de cada indivíduo
        route [list]: lista com a rota de cada indivíduo
        ind [Ind]: objeto indivíduo com numero de carros definidos para gerar as rotas
    
    """    

    def __init__(self, number_cars: int):

        self.cost = []
        self.total_cost = []
        self.routes = []

        self.ind =  Ind(numbers_cars = number_cars)
    
    def create_generation(self, number_of_ind):
        for _ in range(number_of_ind):
            if self.ind.find_path():
                route, cost, total_cost = self.ind.find_path()
                if route not in self.routes:
                    self.routes.append(copy(route))
                    self.cost.append(copy(cost))
                    self.total_cost.append(copy(int(total_cost)))
        
    def return_data(self):
        dados = list(zip(self.total_cost, self.routes, self.cost))
        return( sorted( dados, key = lambda t : t[0]) )