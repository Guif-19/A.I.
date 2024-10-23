from collections import deque

# Representa o estado do problema como missionários à esquerda, canibais à esquerda, posição do barco
class State:
    def __init__(self, M1, C1, B):
        self.M1 = M1
        self.C1 = C1
        self.B = B
        self.parent = None  # Rastrear o caminho de volta

    # Verifica se o estado é válido (nenhum missionário é comido pelos canibais)
    def is_valid(self):
        if self.M1 < 0 or self.C1 < 0 or self.M1 > 3 or self.C1 > 3:
            return False
        if self.M1 > 0 and self.M1 < self.C1:  # Mais canibais que missionários
            return False
        if (3 - self.M1) > 0 and (3 - self.M1) < (3 - self.C1):  # Lado direito
            return False
        return True

    # Verifica se o estado atual é o estado objetivo
    def is_goal(self):
        return self.M1 == 0 and self.C1 == 0 and self.B == 0

    # Gera todos os possíveis estados a partir do estado atual
    def get_successors(self):
        successors = []
        if self.B == 1:  # Barco está à esquerda
            # Tentamos levar diferentes combinações de missionários e canibais
            successors.append(State(self.M1 - 2, self.C1, 0))  # 2 missionários
            successors.append(State(self.M1, self.C1 - 2, 0))  # 2 canibais
            successors.append(State(self.M1 - 1, self.C1 - 1, 0))  # 1 missionário, 1 canibal
            successors.append(State(self.M1 - 1, self.C1, 0))  # 1 missionário
            successors.append(State(self.M1, self.C1 - 1, 0))  # 1 canibal
        else:  # Barco está à direita
            successors.append(State(self.M1 + 2, self.C1, 1))  # 2 missionários
            successors.append(State(self.M1, self.C1 + 2, 1))  # 2 canibais
            successors.append(State(self.M1 + 1, self.C1 + 1, 1))  # 1 missionário, 1 canibal
            successors.append(State(self.M1 + 1, self.C1, 1))  # 1 missionário
            successors.append(State(self.M1, self.C1 + 1, 1))  # 1 canibal

        # Retorna somente os sucessores válidos
        return [s for s in successors if s.is_valid()]

    # Para comparação de estados
    def __eq__(self, other):
        return (self.M1 == other.M1 and
                self.C1 == other.C1 and
                self.B == other.B)

    # Para usar o estado como chave em um set ou dict
    def __hash__(self):
        return hash((self.M1, self.C1, self.B))

# Realiza a busca em largura para encontrar a solução
def bfs(initial_state):
    frontier = deque([initial_state])
    explored = set()

    while frontier:
        state = frontier.popleft()
        if state.is_goal():
            return state  # Encontrou o estado objetivo

        explored.add(state)

        for successor in state.get_successors():
            if successor not in explored and successor not in frontier:
                successor.parent = state  # Para rastrear o caminho de volta
                frontier.append(successor)
    return None

# Imprime a solução rastreando o caminho de volta
def print_solution(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()

    for step in path:
        print(f"Missionários à esquerda: {step.M1}, Canibais à esquerda: {step.C1}, Barco: {'Esquerda' if step.B == 1 else 'Direita'}")

# Estado inicial: 3 missionários, 3 canibais, barco à esquerda
initial_state = State(3, 3, 1)
solution = bfs(initial_state)

if solution:
    print("Solução encontrada:")
    print_solution(solution)
else:
    print("Nenhuma solução encontrada.")
