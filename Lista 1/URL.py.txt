import requests  # Biblioteca para acessar páginas web
from bs4 import BeautifulSoup  # Biblioteca para analisar HTML
from collections import deque  # Fila para organizar as URLs

# Função simples para pegar os links de uma página
def obter_links(url):
    try:
        # Pega o conteúdo da página
        resposta = requests.get(url)
        sopa = BeautifulSoup(resposta.text, 'html.parser')  # Converte o conteúdo para HTML
        links = set()  # Um conjunto para armazenar links únicos
        
        # Procura todas as tags <a> com links
        for tag in sopa.find_all('a', href=True):
            link = tag['href']  # Pega o valor do link (href)
            if link.startswith('http'):  # Apenas links válidos (URLs completas)
                links.add(link)  # Adiciona ao conjunto de links
        
        return links
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")  # Mostra o erro se der problema
        return set()

# Função para encontrar o caminho de links entre duas páginas
def encontrar_caminho(start_url, objetivo_url):
    fila = deque([(start_url, [start_url])])  # Fila com a URL e o caminho percorrido
    visitados = set([start_url])  # Conjunto para evitar repetir visitas

    while fila:
        url_atual, caminho = fila.popleft()  # Pega a primeira URL da fila
        print(f"Visitando: {url_atual}")
        
        # Pega todos os links da página atual
        for link in obter_links(url_atual):
            if link == objetivo_url:  # Se achou a página desejada
                return caminho + [link]  # Retorna o caminho completo
            if link not in visitados:  # Se não visitou ainda
                visitados.add(link)  # Marca como visitado
                fila.append((link, caminho + [link]))  # Adiciona o novo caminho na fila
    
    return None  # Se não achar caminho, retorna nada

# Testando a função
def testar_caminho():
    inicio_url = 'https://exemplo.com/pagina_inicial'  # Trocar por URL real
    objetivo_url = 'https://exemplo.com/pagina_objetivo'  # Trocar por URL real
    caminho = encontrar_caminho(inicio_url, objetivo_url)
    
    if caminho:
        print("Caminho encontrado:")
        for url in caminho:
            print(url)
    else:
        print("Nenhum caminho encontrado.")

# Executar o teste
testar_caminho()
