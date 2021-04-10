import numpy as np
from graph import Graph
from path import Path
from copy import copy

class Cars():
    def __init__(self, numbers_cars, nodes_dest, graph = Graph(), init_node = 0):
        self.numbers_cars = numbers_cars
        self.init_node = init_node

        self.paths = [Path(init_node) for i in range(numbers_cars)]
        self.paths_cost = []
        self.paths_real = []

        self.total_cost = 0
        self.all_paths = {0}
        self.graph = graph

        self.nodes_dest = nodes_dest # lista dos lugares objetivos

    def return_paths(self):
        return self.paths

    def random_append_new_node(self):
        for car in self.paths:
            next_node = self.graph.return_random_next(car.get_path())
            if next_node == None:
                return False
            cost_next = self.graph.return_cost_next(car.get_current_node(),next_node)
            car.add(next_node,cost_next)
            self.all_paths.add(next_node)
        return True

    def find_path(self):
        self.paths = [Path(self.init_node) for i in range(self.numbers_cars)]
        self.all_paths = {0}
        self.paths_real = []
        while True:
            find = self.random_append_new_node()
            if all(elem in self.all_paths for elem in self.nodes_dest) or not find:
                if not find:
                    return False
                break
        self.remove_excess_of_path()
        self.calc_total_cost()
        self.adjust_real_path()
        return True

    def remove_excess_of_path(self):
        for car in self.paths:
            while True:
                if car.get_current_node() in self.nodes_dest or car.get_current_node() == None:
                    break
                car.pop_node()
    
    def adjust_real_path(self):
        for car in self.paths:
            self.paths_real.append(car.get_path())
    
    def calc_total_cost(self):
        self.total_cost = 0
        self.paths_cost = []
        for car in self.paths:
            self.paths_cost.append(car.get_total_cost())
            self.total_cost += int(car.get_total_cost())
    
    def return_str(self):
        str_path = ''
        for path in self.paths_real:
            for node in path:
                str_path += str(node) + '->'
            str_path += 'E'
            str_path += '__'
        return self.total_cost, str_path


    def return_cars(self):
        return self.total_cost, self.paths_real
    
    def return_list_of_nodes_visites_per_car(self):
        nodes_visites_per_car = []
        for car in self.paths:
            visited = []
            for node in car.get_path():
                if node in self.nodes_dest:
                    visited.append(node)
            nodes_visites_per_car.append(copy(visited))
        
        return nodes_visites_per_car

    # WIP
    def remove_path(self):
        self.paths.pop()
        self.paths_cost.pop()
        self.total_cost = sum(self.paths_cost)

    # WIP
    def append_path(self, path, cost):
        self.paths.append(path)
        self.paths_cost.append(cost)
        self.total_cost = sum(self.paths_cost)

    # WIP
    def validate_path(self):
        self.all_paths = {0}
        for path in self.paths:
            for node in path.get_path():
                self.all_paths.add(node)
        
        if all(elem in self.all_paths for elem in self.nodes_dest):
            return True
        else:
            return False
            
    # WIP
    def return_last_path(self):
        return self.paths[-1],self.paths_cost[-1]





# graph = Graph()
# cars = Cars(2,[8,1,6])
# if cars.find_path():
#     print(cars.return_list_of_nodes_visites_per_car())
# # # for path in cars.return_paths():
# # #     print(path.get_path())
