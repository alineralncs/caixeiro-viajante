import random
import time

grafo_k5 = [[0, 2, 7, 1, 5], [2, 0, 5, 3, 4], [7, 5, 0, 6, 8], [1, 3, 6, 0, 2], [5, 4, 8, 2, 0]]

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
        candidates = random.sample(remaining_vertices, min(K, len(remaining_vertices)))
        next_vertex = min(candidates, key=lambda v: graph[path[-1]][v])
        path.append(next_vertex)
        remaining_vertices.remove(next_vertex)
    print(f'n-deterministico={n_deterministico};instancia={graph};seed={valor};')
    return path


if __name__ == "__main__":
    n = 5 
    K = 2  #

    start_time = time.time()
    deterministic_path = tsp_constructive_deterministic(grafo_k5)
    deterministic_cost = calculate_cost(grafo_k5, deterministic_path)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução (segundos) - algoritmo construtivo determinístico:", execution_time)

    print("Caminho pelo algoritmo construtivo determinístico:", deterministic_path)
    print("Custo do caminho pelo algoritmo construtivo determinístico:", deterministic_cost)
    
    start_time = time.time()
    randomized_path = tsp_randomized_greedy(grafo_k5, K)
    randomized_cost = calculate_cost(grafo_k5, randomized_path)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Tempo de execução (segundos) - algoritmo guloso randomizado:", execution_time)
    print("Caminho pelo algoritmo guloso randomizado:", randomized_path)
    print("Custo do caminho pelo algoritmo guloso randomizado:", randomized_cost)
