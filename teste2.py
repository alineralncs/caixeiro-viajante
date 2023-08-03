import random
import time

grafo_k5_1 = [[0, 2, 7, 1, 5],
            [2, 0, 5, 3, 4],
            [7, 5, 0, 6, 8],
            [1, 3, 6, 0, 2],
            [5, 4, 8, 2, 0]]

grafo_k5_2 = [[0, 9, 4, 12, 8],
              [9, 0, 7, 6, 14],
              [4, 7, 0, 3, 5],
              [12, 6, 3, 0, 11],
              [8, 14, 5, 11, 0]]

grafo_k6 = [[0, 7, 2, 15, 9, 10],
            [7, 0, 5, 4, 10, 12],
            [2, 5, 0, 2, 3, 13],
            [15, 4, 2, 0, 8, 14],
            [9, 10, 3, 8, 0, 6],
            [10, 12, 13, 14, 6, 0]]


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
        cost += graph[path[i]][path[i + 1]]
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

def apply_local_search(graph, path):
    improved = True
    while improved:
        improved = False

        # 2-opt neighborhood
        for i in range(len(path) - 1):
            for j in range(i + 1, len(path)):
                new_path = path[:i] + path[i:j + 1][::-1] + path[j + 1:]
                new_cost = calculate_cost(graph, new_path)
                if new_cost < calculate_cost(graph, path):
                    path = new_path
                    improved = True

        # 3-opt neighborhood
        for i in range(len(path) - 2):
            for j in range(i + 1, len(path) - 1):
                for k in range(j + 1, len(path)):
                    opt3_cases = [
                        list(dict.fromkeys(path[:i+1] + path[j:i:-1] + path[k:j-1:-1] + path[k+1:])),
                        list(dict.fromkeys(path[:i+1] + path[j:k+1][::-1] + path[i+1:j] + path[k+1:])),
                        list(dict.fromkeys(path[:i+1] + path[j:k+1] + path[i+1:j][::-1] + path[k+1:]))
                    ]
                    new_path = min(opt3_cases, key=lambda p: calculate_cost(graph, p))
                    new_cost = calculate_cost(graph, new_path)
                    if new_cost < calculate_cost(graph, path):
                        path = new_path
                        improved = True

    return path

if __name__ == "__main__":
    K = 3
    total_pesos = 0

    for _ in range(10):
        start_time = time.time()
        deterministic_path = tsp_constructive_deterministic(grafo_k5_1)
        deterministic_path = apply_local_search(grafo_k5_1, deterministic_path)
        deterministic_cost = calculate_cost(grafo_k5_1, deterministic_path)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'deterministico=true; instancia=inst_1; custo={deterministic_cost}; {execution_time} ms;')
        print(f'{deterministic_path}')

    print('\n#############################################################\n')

    for i in range(100):
        start_time = time.time()
        randomized_path, seed = tsp_randomized_greedy(grafo_k5_1, K)
        randomized_path = apply_local_search(grafo_k5_1, randomized_path)
        randomized_cost = calculate_cost(grafo_k5_1, randomized_path)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'n-deterministico=true; instancia=inst_1; custo={randomized_cost}; seed={seed}; {execution_time} ms;')
        #print(f'{seed};{K};{randomized_cost};{execution_time};')
        print(f'{randomized_path}')
        total_pesos += randomized_cost

    media = total_pesos / 100
    print(f'---- media: {media}')
