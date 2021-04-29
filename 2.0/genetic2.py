from copy import copy
from population import Population
from graph import Graph
from random import randint, random, choice
from path import Path

class Genetic:

    def __init__(self, number_cars = 3, Graph = Graph()):
        self.population = Population(number_cars)
        self.number_selected = 50
        self.number_population = 200
        self.number_of_nodes = Graph.number_of_nodes

        self.number_cars = number_cars

        self.graph = Graph

        self.selects_routes = []
        self.selects = []
        self.crossed = []

    def create_generation(self):
        self.selection()
        self.SCX_cross_over()
        self.mutation()
        # self.selects = self.selects[0:self.number_selected] # Filtro os melhores
    
    def run(self, number_of_generations = 2000):
        for i in range(number_of_generations):
            print(f'gerando a geração {i}')
            self.create_generation()

    # Sequential Constructive Crossover Operator
    def SCX_cross_over(self, number_cross_over = 50):
        for i in range(number_cross_over):

            # Selecionar 2 individuos randomicamente
            ind1 = 0
            ind2 = 0
            while ind1 == ind2:
                ind1 = randint(0, self.number_selected - 1)
                ind2 = randint(0, self.number_selected - 1)

            # Fazer o SCX crossover
            route1 = self.selects[ind1][1]
            route2 = self.selects[ind2][1]

            cost1 = self.selects[ind1][2]
            cost2 = self.selects[ind2][2]

            offsprint_route = [0]
            offsprint_cost = [0]
            offsprint_total_cost = 0

            for i in range( 1, len(route1)):
                if ( cost1[i] <= cost2[i] ) and route1[i] not in offsprint_route:
                    cost_next = self.graph.get_cost(offsprint_route[-1], route1[i])
                    offsprint_route.append(copy(route1[i]))
                    offsprint_cost.append(cost_next)
                    offsprint_total_cost += int(cost_next)
                
                elif route2[i] not in offsprint_route:
                    cost_next = self.graph.get_cost(offsprint_route[-1], route2[i])
                    offsprint_route.append(copy(route2[i]))
                    offsprint_cost.append(cost_next)
                    offsprint_total_cost += int(cost_next)
                
                else:
                    next_node = self.graph.return_random_next_not_zero(already_visited = offsprint_route)
                    if next_node == None:
                        break

                    if offsprint_route[-1] == None:
                        cost_next = self.graph.get_cost(offsprint_route[0], next_node)
                    else:
                        cost_next = self.graph.get_cost(offsprint_route[-1], next_node)

                    offsprint_route.append(next_node)
                    offsprint_cost.append(cost_next)
                    offsprint_total_cost += cost_next

            if offsprint_route not in self.selects_routes:
                self.selects_routes.append(copy(offsprint_route))
                self.selects.append( copy((offsprint_total_cost, offsprint_route, offsprint_cost)) )
                self.selects = sorted( self.selects, key = lambda t : t[0] )
    
    def selection(self):
        self.population.create_generation(self.number_population) # Crio a população
        temp_pop = self.population.return_data()

        for select in temp_pop: # copio os inds
            if select[1] not in self.selects_routes:
                self.selects_routes.append(select[1])
                self.selects.append(select)
        try:
            self.selects = sorted( self.selects, key = lambda t : t[0] ) # Ordeno de acordo com a pontuação
            self.selects = self.selects[0:self.number_selected] # Filtro os melhores
        except:
            print(self.selects)
            raise
    
    def mutation(self):
        '''A mutação nada mais é do que o swap entre 2 elementos do caminho, para fazer esse swap
        primeiramente é necessario calcular o tamanho da roda representada como caxeiro viagente unitario, que 
        depende do numero de "carros/caixeiros" especificado antes de rodar o algoritmo '''

        if random() > 0.9:

            ind = choice(self.selects)

            node1 = randint(1, self.number_of_nodes )
            node2 = randint(1, self.number_of_nodes )
            while node1 == node2:
                node2 = randint(1, self.number_of_nodes )

            new_path = copy(ind[1])

            index1 = new_path.index(node1)
            index2 = new_path.index(node2)
            
            new_path[index1], new_path[index2] = new_path[index2], new_path[index1]

            new_path_obj = Path()
            new_path_obj.create_path(new_path)

            self.selects_routes.append(copy(new_path))
            self.selects.append( copy((new_path_obj.get_total_cost(), new_path, new_path_obj.cost)) )
            self.selects = sorted( self.selects, key = lambda t : t[0] )

                

    
    def return_best_ind(self):
        route_mixed = self.selects[0][1][1:]
        routes = []
        route = []
        for node in route_mixed:
            route.append(node)
            if node > self.number_of_nodes:
                routes.append(copy(route[:-1]))
                route = []
        routes.append(route)
        return self.selects[0][0], routes