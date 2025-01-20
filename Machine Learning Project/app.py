import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report

df = pd.read_csv("mortalidade97.csv", delimiter=";", encoding="utf-8")

# Selecionar variáveis independentes e dependentes
X = df[['Ano do obito']]  # Ano do óbito como variável independente
y_class = df['aumento_diminui']  # Aumento ou diminuição de óbitos (classificação)
y_reg = df['Regiao Sudeste']  # Número de óbitos (regressão)

# Dividir os dados em treinamento e teste
X_train, X_test, y_class_train, y_class_test, y_reg_train, y_reg_test = train_test_split(X, y_class, y_reg, test_size=0.3, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Treinar o modelo de regressão logística para previsão de aumento ou diminuição
modelo_classificacao = LogisticRegression()
modelo_classificacao.fit(X_train_scaled, y_class_train)

# Treinar o modelo de regressão linear para prever o número de óbitos
modelo_regressao = LinearRegression()
modelo_regressao.fit(X_train_scaled, y_reg_train)

# Fazer previsões de aumento ou diminuição
y_pred_class = modelo_classificacao.predict(X_test_scaled)

# Fazer previsões do número de óbitos
y_pred_reg = modelo_regressao.predict(X_test_scaled)

st.title("prevendo o numero de obitos:")

