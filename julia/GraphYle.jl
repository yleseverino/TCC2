
module GraphYle

export get_cost, return_random_next, graph

using JLD
using StatsBase

"""Este objeto representa o grafo, com ele é possivel pegar os custo das cotas, a principio o grafo deve ser completo
    
    Attributes:
        number_of_nodes [int]: numero de node - 1 para assim ter um contagem de 0 ao total
        matrix Array{Int64, 2}: é a matriz de custos do meu grafo
    
"""
struct Graph
    matrix :: Array{Int64, 2}
    number_of_nodes :: Int
    function Graph()
        matrix = load("ch150.jld")["data"]
        number_of_nodes = size(matrix)[1]
        new(matrix,number_of_nodes)
    end
end

const graph = Graph()

function get_cost(current_node :: Int, next_node :: Int, graph :: Graph = graph)
    # @assert( current_node < graph.number_of_nodes || next_node < graph.number_of_nodes , "Node atual e node requerido inexistente")
    if current_node > graph.number_of_nodes
        return graph.matrix[1, next_node]
    elseif next_node > graph.number_of_nodes
        return graph.matrix[current_node, 1]
    else
        return graph.matrix[current_node, next_node]
    end   
end

function return_random_next(already_visited :: Array{Int64,1}, graph :: Graph = graph)
    possibles  = [2:1:graph.number_of_nodes;]
    return_possibles = []
    for node in possibles
        if node ∉ already_visited
            push!(return_possibles,node)
        end
    end
    if isempty(return_possibles)
        return nothing
    end
    return sample(return_possibles)
end

end


