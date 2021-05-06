include("GraphYle.jl")
include("PathYle.jl")
include("IndYle.jl")
include("PopYle.jl")
using Main.PopYle: create_population
using Main.GraphYle: get_cost, return_random_next, graph
using Main.PathYle: get_list_cost


mutable struct Genetic
    number_cars :: Int
    number_population :: Int
    number_selected :: Int
    number_cross_over :: Int
    selects :: Vector{Any}
    population :: Vector{Any}
    function Genetic(number_cars :: Int = 3)
        new(    number_cars, 
                50,
                50,
                50,
                []
            )   
    end
end


function seletion!(genetic :: Genetic)

    genetic.population = create_population(genetic.number_cars, genetic.number_population)

    for ind in genetic.population
        if !(ind in genetic.selects)
            push!(genetic.selects, deepcopy(ind))
        end
    end
    # union!(genetic.selects, genetic.population)

    sort!(genetic.selects, by = x -> x[1][1])
    genetic.selects = genetic.selects[1:genetic.number_selected]
end

function SCX_cross_over!(genetic :: Genetic)

    for ind1 = 1:genetic.number_selected

        if rand() > 0

            # Selecionar 2 individuos randomicamente
            # ind1 = rand(1:genetic.number_selected)
            ind2 = rand(1:genetic.number_selected)

            while ind1 == ind2
                ind2 = rand(1:genetic.number_selected)
            end

            route1 = genetic.selects[ind1][2]
            route2 = genetic.selects[ind2][2]

            cost1 = genetic.selects[ind1][3]
            cost2 = genetic.selects[ind2][3]

            offsprint_route = [1]
            offsprint_cost = [0]
            offsprint_total_cost = 0

            for i = 2:size(g.selects[1][2])[1]

                cost1 = get_cost(last(offsprint_route),route1[i])
                cost2 = get_cost(last(offsprint_route),route2[i])

                if cost1 <= cost2 && !(route1[i] in offsprint_route)
                    push!(offsprint_route, route1[i])
                    push!(offsprint_cost, cost1)
                    offsprint_total_cost += cost1

                elseif !(route2[i] in offsprint_route)
                    push!(offsprint_route, route2[i])
                    push!(offsprint_cost, cost2)
                    offsprint_total_cost += cost2

                elseif !(route1[i] in offsprint_route)
                    push!(offsprint_route, route1[i])
                    push!(offsprint_cost, cost1)
                    offsprint_total_cost += cost1
                
                else

                    next_node = return_random_next(offsprint_route)
                    if next_node === nothing
                        break
                    end

                    cost = get_cost(last(offsprint_route), next_node)
                    push!(offsprint_route, next_node)
                    push!(offsprint_cost, cost)
                    offsprint_total_cost += cost

                end
            end
            offsprint_ind = offsprint_total_cost, offsprint_route, offsprint_cost
            if !(offsprint_ind in genetic.selects)
                push!(genetic.selects, deepcopy(offsprint_ind))
            end
            # genetic.selects = vcat(genetic.selects, deepcopy())
        end
    end

    sort!(genetic.selects, by = x -> x[1][1])

end

"""
A mutação nada mais é do que o swap entre 2 elementos do caminho, para fazer esse swap
primeiramente é necessario calcular o tamanho da roda representada como caxeiro viagente unitario, que 
depende do numero de "carros/caixeiros" especificado antes de rodar o algoritmo 
"""
function mutation!(genetic :: Genetic)
    for ind in g.selects

        if rand() > 0.1

            # ind = g.selects[ rand(1:end) ] # seleciona um ind randomicamente

            node1 = rand(2:graph.number_of_nodes)
            node2 = rand(2:graph.number_of_nodes)

            while node1 == node2
                node2 = rand(2:graph.number_of_nodes)
            end

            new_path = copy(ind[2])
            index_1 = findfirst( new_path .== node1 )
            index_2 = findfirst( new_path .== node2 )

            new_path[index_1], new_path[index_2] = new_path[index_2], new_path[index_1]

            cost = get_list_cost(new_path)
            total_cost = sum(cost)

            new_ind = total_cost, new_path, cost
            if !(new_ind in genetic.selects)
                push!(genetic.selects, deepcopy(new_ind))
            end
        end
    end
    sort!(genetic.selects, by = x -> x[1][1])
end

function run!(genetic :: Genetic, number_generations :: Int = 2000)
    for i = 1:number_generations
        # println("Geração :", i)
        seletion!(g)
        SCX_cross_over!(g)
        mutation!(g)
    end
end

# g = Genetic(3)
# run!(g)
# g.selects

g = Genetic(10)
resultados = []
for i = 1:30
    println("Instância :", i)
    g = Genetic(10)
    run!(g)
    println(g.selects[1][1])
    push!(resultados,g.selects[1][1])
end