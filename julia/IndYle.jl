module IndYle

export Ind, random_append_new_node!, convert_mtsp_to_tsp, find_path!, get_cost

# include("GraphYle.jl")
include("PathYle.jl")
using Main.PathYle: Path, add_node_path!, get_total_cost, graph, get_cost, return_random_next
# using Main.GraphYle: return_random_next, get_cost, graph


mutable struct Ind
    number_cars :: Int
    paths :: Vector{Path}
    all_nodes_visited_paths :: Vector{Int}
    all_cost_list :: Vector{Int}
    total_cost :: Int
    function Ind(number_cars :: Int = 3)
        paths = []
        i = 0
        while i < number_cars
            push!(paths, Path())
            i+=1
        end
        new(number_cars, paths, [1], [0], 0)
    end
end

function random_append_new_node!(ind :: Ind)
    for car in ind.paths
        next_node = return_random_next(ind.all_nodes_visited_paths)
        if next_node === nothing
            return false
        end
        cost_next = get_cost(last(car.route), next_node)
        ind.total_cost += cost_next
        add_node_path!(car, next_node)
        push!(ind.all_nodes_visited_paths, next_node)
        push!(ind.all_cost_list, cost_next)
    end
    return true
end

"""
Nessa função eu pego os caminhos dos carros e converto como se fosse somente um caixeiro viagante,
para fazer isso devo adicionar um novo node ficticion que sua distancia deve ser o mesmo com a origem
"""
function convert_mtsp_to_tsp(ind :: Ind)
    path_mixed = [1]
    cost_mixed = [0]
    total_cost = 0
    max = graph.number_of_nodes
    for car in ind.paths
        cost_mixed = vcat( cost_mixed, car.cost[2:end])
        path_mixed = vcat( path_mixed, car.route[2:end])

        total_cost += get_total_cost(car)

        cost_to_base = get_cost(last(car.route),1)
        max += 1

        push!(path_mixed, max)
        push!(cost_mixed, cost_to_base)
    end

    pop!(path_mixed)
    pop!(cost_mixed)

    return total_cost, path_mixed, cost_mixed 
end

function find_path!(number_cars :: Int)
    ind = Ind(number_cars)
    while random_append_new_node!(ind)
    end
    return convert_mtsp_to_tsp(ind)
end


end

