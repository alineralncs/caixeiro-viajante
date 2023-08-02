import random
import time

grafo_k5 = [[0, 2, 7, 1, 5],
            [2, 0, 5, 3, 4],
            [7, 5, 0, 6, 8],
            [1, 3, 6, 0, 2],
            [5, 4, 8, 2, 0]]

grafo_k10 = [[0, 17, 23, 9, 14, 20, 12, 15, 8, 11],
             [17, 0, 6, 13, 10, 7, 19, 21, 16, 22],
             [23, 6, 0, 18, 10, 25, 11, 7, 13, 16],
             [9, 13, 18, 0, 22, 5, 17, 19, 12, 24],
             [14, 10, 10, 22, 0, 8, 14, 16, 9, 26],
             [20, 7, 25, 5, 8, 0, 15, 18, 10, 27],
             [12, 19, 11, 17, 14, 15, 0, 20, 12, 29],
             [15, 21, 7, 19, 16, 18, 20, 0, 7, 25],
             [8, 16, 13, 12, 9, 10, 12, 7, 0, 21],
             [11, 22, 16, 24, 26, 27, 29, 25, 21, 0]]

def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i+1]]
    cost += graph[path[-1]][path[0]]  
    return cost

def tsp_constructive_deterministic(graph):
    n = len(graph)
    path = [0] 
    remaining_vertices = set(range(1, n))  

    while remaining_vertices:
        next_vertex = min(remaining_vertices, key=lambda v: graph[path[-1]][v])
        path.append(next_vertex)
        remaining_vertices.remove(next_vertex)

    return path

def tsp_randomized_greedy(graph, K):
    n_deterministico = True

    valor = random.randint(1, 100)
    random.seed(valor)
   
    n = len(graph)
    path = [0]  
    remaining_vertices = set(range(1, n))  

    while remaining_vertices:
        candidates = random.choices(tuple(remaining_vertices), k=min(K, len(remaining_vertices)))
        next_vertex = min(candidates, key=lambda v: graph[path[-1]][v])
        path.append(next_vertex)
        remaining_vertices.remove(next_vertex)
    return path, valor


if __name__ == "__main__":
    n = 5 
    K = 2

    for _ in range(10):
        start_time = time.time()
        deterministic_path = tsp_constructive_deterministic(grafo_k10)
        deterministic_cost = calculate_cost(grafo_k10, deterministic_path)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'deterministico=true; instancia=inst_1; custo={deterministic_cost}; {execution_time} ms;')
    
    print('\n#############################################################\n')

    for i in range(100):
        start_time = time.time()
        randomized_path, seed = tsp_randomized_greedy(grafo_k10, K)
        randomized_cost = calculate_cost(grafo_k10, randomized_path)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'deterministico=true; instancia=inst_5; seed={seed}; alpha={K}; custo={randomized_cost}; {execution_time} ms;')