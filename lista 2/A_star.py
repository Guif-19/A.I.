import heapq

# Coordenadas dos nós
coordinates = {
    'A': (0, 0),
    'B': (1, 0),
    'C': (0, 1),
    'D': (1, 1),
    'E': (0, 2),
    'F': (1, 2)
}

# Função para calcular a heurística de Manhattan
def manhattan_heuristic(node, goal):
    x1, y1 = coordinates[node]
    x2, y2 = coordinates[goal]
    return abs(x1 - x2) + abs(y1 - y2)

# Grafo ponderado (como lista de adjacência)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('F', 3)],
    'E': [('F', 2)],
    'F': []
}

# Função A* para encontrar o caminho mais curto
def a_star(graph, start, goal, heuristic):
    # Fila de prioridade para nós a serem explorados (f_score, nó)
    pq = []
    heapq.heappush(pq, (0, start))  # (f_score, node)
    
    # Dicionário para armazenar o menor custo g (custo real) até o nó
    g_score = {start: 0}
    
    # Dicionário para armazenar o caminho
    came_from = {start: None}
    
    while pq:
        # Pega o nó com o menor custo f da fila
        current_f, current_node = heapq.heappop(pq)
        
        # Se chegamos ao objetivo, reconstruímos o caminho
        if current_node == goal:
            path = []
            total_cost = g_score[goal]
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1], total_cost  # Retorna o caminho invertido e o custo total
        
        # Explorar vizinhos do nó atual
        for neighbor, cost in graph[current_node]:
            # Custo g (real) até o vizinho
            tentative_g_score = g_score[current_node] + cost
            
            # Se encontramos um caminho melhor para o vizinho
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Atualiza o caminho e o custo g
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(pq, (f_score, neighbor))
                came_from[neighbor] = current_node
    
    return None, None  # Retorna None se nenhum caminho foi encontrado

# Executando o algoritmo A* para encontrar o caminho de A até F
start_node = 'A'
goal_node = 'F'

# Usamos a heurística de Manhattan
path, cost = a_star(graph, start_node, goal_node, manhattan_heuristic)

print(f"Caminho mais curto de {start_node} até {goal_node}: {path}")
print(f"Custo total do caminho: {cost}")
