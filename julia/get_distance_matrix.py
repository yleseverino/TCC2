import numpy as np
import tsplib95

problem = tsplib95.load('ch150.tsp')

distance = np.full((problem.dimension, problem.dimension),0)

for node1, weigth1 in problem.as_dict()['node_coords'].items():
    a = np.array(weigth1)
    for node2, weigth2 in problem.as_dict()['node_coords'].items():
        if node1 != node2:
            b = np.array(weigth2)
            dist = np.linalg.norm(a-b)
        else:
            dist = 999
        distance[node1 - 1, node2 - 1] = int(dist)

with open(f'ch150.tsp.npy', 'wb') as f:
    np.save(f,distance)

print(distance)