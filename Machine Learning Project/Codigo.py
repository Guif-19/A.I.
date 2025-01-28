import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv("mortalidadenormalizada.csv", delimiter=";", encoding="utf-8")
df

df.plot(kind="scatter", x="Ano do obito", y="Regiao Sudeste");

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Carregar os dados do arquivo CSV
df = pd.read_csv('mortalidadetotal.csv', delimiter=';')

# Verificar valores ausentes
print("Valores ausentes por coluna:")
print(df.isnull().sum())

# Preencher valores ausentes com 0
df.fillna(0, inplace=True)

# Transformar o ano em uma variável temporal
df['Ano desde 1996'] = df['Ano do obito'] - 1996

# Selecionar variáveis independentes e dependentes
X = df[['Ano desde 1996']]  # Variável independente
y = df['Regiao Sudeste']  # Variável dependente

# Dividir os dados em treinamento e teste (divisão temporal)
X_train = X[df['Ano do obito'] <= 2020]
y_train = y[df['Ano do obito'] <= 2020]
X_test = X[df['Ano do obito'] > 2020]
y_test = y[df['Ano do obito'] > 2020]

# Criar e treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = modelo.predict(X_test)

# Avaliar o modelo
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Quadrático Médio (MSE) no conjunto de teste: {mse:.2f}")

# Exibir previsões no conjunto de teste
print("\nPrevisões no conjunto de teste:")
for ano, pred in zip(df.loc[df['Ano do obito'] > 2020, 'Ano do obito'], y_pred):
    print(f"Ano {ano}: {int(pred)} óbitos")

# Previsões para anos futuros
anos_futuros = np.array([[2024 - 1996], [2025 - 1996], [2026 - 1996], [2027 - 1996], [2028 - 1996], [2029 - 1996], [2030 - 1996], [2031 - 1996], [2032 - 1996], [2033 - 1996], [2034 - 1996], [2035 - 1996]])
pred_futuro = modelo.predict(anos_futuros)
print("\nPrevisões para anos futuros:")
for ano, pred in zip(range(2024, 2035), pred_futuro):
    print(f"Ano {ano}: {int(pred)} óbitos")

# Comparação com o ano anterior
print("\nComparação de previsões entre anos consecutivos:")
for i in range(1, len(pred_futuro)):
    if pred_futuro[i] > pred_futuro[i - 1]:
        print(f"De {2024 + i - 1} para {2024 + i}: Aumentou ({int(pred_futuro[i - 1])} -> {int(pred_futuro[i])})")
    elif pred_futuro[i] < pred_futuro[i - 1]:
        print(f"De {2024 + i - 1} para {2024 + i}: Diminuiu ({int(pred_futuro[i - 1])} -> {int(pred_futuro[i])})")
    else:
        print(f"De {2024 + i - 1} para {2024 + i}: Permaneceu igual ({int(pred_futuro[i - 1])})")


df = pd.read_csv("10anos.csv", delimiter=";", encoding="utf-8")
df.plot(kind="scatter", x="Ano obito", y="Regiao Sudeste(BR)");

