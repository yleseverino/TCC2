module PathYle

export Path, add_node_path!, get_total_cost, graph, get_cost, return_random_next, get_list_cost

include("GraphYle.jl")
using Main.GraphYle: get_cost, return_random_next, graph

mutable struct Path
    route :: Vector{Int}
    cost :: Vector{Int}
    function Path(route :: Vector{Int} = [1])
        if route == [1]
            new(route,[0])
        else
            cost = []
            for (index, value) in enumerate(route)
                if index == size(route)[1]
                    break
                end
                push!(cost, get_cost(value, route[index + 1]))
            end
            new(route,cost)
        end
    end
end

function get_list_cost(route :: Vector{Int})
    cost :: Vector{Int} = []
    for (index, value) in enumerate(route)
        if index == size(route)[1]
            break
        end
        push!(cost, get_cost(value, route[index + 1]))
    end
    return cost
end

function get_total_cost(path :: Path)
    sum(path.cost)
end

function add_node_path!(path :: Path, node :: Int ,graph = graph)
    
    cost = get_cost(last(path.route), node)

    push!(path.cost, cost)
    push!(path.route, node)

end


end