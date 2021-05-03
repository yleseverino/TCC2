struct Graph
    matrix :: Array{Int64, 2}
    number_of_nodes :: Int
    function Graph()
        matrix = load("graph_m51.jld")["data"]
        number_of_nodes = size(matrix)[1]
        new(matrix,number_of_nodes)
    end
end

using JLD
using PyCall
py"""
import numpy as np

with open(f'ch150.tsp.npy', 'rb') as f:
    matrix = np.load(f)
    number_of_nodes = len(matrix) - 1
"""

matrix = py"matrix"
number_of_nodes = py"number_of_nodes"

save("ch150.jld", "data", matrix)