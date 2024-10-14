# Uma estratégia apropriada para encontrar um caminho de links entre duas páginas web seria a Busca em Largura (BFS). 
# Essa abordagem é eficaz em problemas onde é preciso explorar várias camadas de profundidade de um grafo, como ao procurar por links entre páginas. 
# A busca em largura explora todos os links de uma página antes de passar para as próximas, garantindo que você encontre o caminho mais curto.



import requests
from bs4 import BeautifulSoup
from collections import deque

# Função para pegar links de uma página
def pegar_links(url):
    try:
        resp = requests.get(url)
        html = BeautifulSoup(resp.text, 'html.parser')
        links = set()

        for a in html.find_all('a', href=True):
            link = a['href']
            if link.startswith('http'):
                links.add(link)
        
        return links
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return set()

# Função para encontrar o caminho entre duas URLs
def buscar_caminho(origem, destino):
    fila = deque([(origem, [origem])])
    visitados = set([origem])

    while fila:
        atual, caminho = fila.popleft()
        print(f"Visitando: {atual}")

        for link in pegar_links(atual):
            if link == destino:
                return caminho + [link]
            if link not in visitados:
                visitados.add(link)
                fila.append((link, caminho + [link]))

    return None

# Teste da função
def teste():
    origem = 'https://exemplo.com/inicio'  # Substituir por URL real
    destino = 'https://exemplo.com/fim'  # Substituir por URL real
    caminho = buscar_caminho(origem, destino)
    
    if caminho:
        print("Caminho encontrado:")
        for url in caminho:
            print(url)
    else:
        print("Caminho não encontrado.")

# Executar o teste
teste()
