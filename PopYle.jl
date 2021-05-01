module PopYle

export create_population, get_cost

using Main.IndYle: Ind, random_append_new_node!, convert_mtsp_to_tsp, find_path!

mutable struct Population
    number_cars :: Int
    total_cost :: Vector{Int}
    costs 
    path_mixeds 
    function Population(number_cars :: Int)
        new(number_cars,[],[],[])
    end
end

function create_population(number_cars :: Int, number_population :: Int)
    pop = Population(number_cars)
    for _ = 1:number_population
        total_cost, path_mixed, cost_mixed = find_path!(pop.number_cars)
        push!(pop.total_cost,total_cost)
        push!(pop.path_mixeds,path_mixed)
        push!(pop.costs,cost_mixed)
    end
    return return_population(pop)
end

function return_population(pop :: Population)
    dados = collect(zip(pop.total_cost, pop.path_mixeds, pop.costs))
    return dados
    return sort!(dados, by = x -> x[1][1], rev = true)
end

end