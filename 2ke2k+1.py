from collections import deque

def busca_em_largura(estado_inicial, objetivo):
    fila = deque([estado_inicial])
    visitados = set()

    while fila:
        # Remove o primeiro estado da fila
        estado_atual = fila.popleft()

        # Se o estado atual é o objetivo, acaba
        if estado_atual == objetivo:
            return estado_atual

        # Marca o estado atual como visitado
        visitados.add(estado_atual)

        # Calcula os próximos estados (sucessores)
        proximo_esquerda = 2 * estado_atual      # Ir para 2k
        proximo_direita = 2 * estado_atual + 1   # Ir para 2k + 1

        # Adiciona os sucessores na fila se ainda não foram visitados
        if proximo_esquerda not in visitados:
            fila.append(proximo_esquerda)
        if proximo_direita not in visitados:
            fila.append(proximo_direita)

    return None  # Caso não ache o objetivo

# Função principal que executa a busca e imprime o caminho
def simulacao_busca(objetivo):
    estado_inicial = 1  # O estado inicial é sempre 1
    resultado = busca_em_largura(estado_inicial, objetivo)

    # Verifica se o objetivo foi alcançado
    if resultado:
        print(f"Objetivo {objetivo} alcançado a partir do estado inicial {estado_inicial}.")
    else:
        print(f"Objetivo {objetivo} não foi alcançado.")

# Definindo o objetivo como 11 (pode mudar para qualquer número)
objetivo = 11

# Executa a simulação
simulacao_busca(objetivo)
