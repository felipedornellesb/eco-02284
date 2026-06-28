"""
main.py

Descrição: Este programa define as variáveis para as atividades da lista e roda as funções sequencialmente
Autor: Felipe Dornelles e Affonso Pereira
Data: 17/03/2026
Versão: 1.0.0
"""

# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar módulos
from custo_de_capital import calcular_custo_capital
from modelo_de_markowitz import otimizar_carteira
from retorno_risco_desempenho_carteiras import calcular_drawdown
from teoria_da_utilidade_esperada import gerar_cenarios

# Alocação de Memória

## teoria_da_utilidade_esperada
riqueza_inicial = 100
n_cenarios = 10000
media = 0.05
volatilidade = 0.15
t_u_e_seed = 42

## retorno_risco_desempenho_carteiras
rrdc_seed = 42
n_periodos = 1000

## custo_de_capital
Ku = 0.12  # Custo de capital desalavancado
Kd = 0.07  # Custo da dívida
T = 0.34   # Imposto
de_ratio = pd.Series([round(x * 0.2, 2) for x in range(16)])

## modelo_de_markowitz
taxa_livre_risco = 0.05
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']
start_date = '2021-01-01'
end_date = '2022-01-01'

# Entrada de dados
# Dados são passados diretamente para as funções

# Processamento de dados

## Teoria da Utilidade Esperada
riquezas_finais, utilidade_esperada, equivalente_certo = gerar_cenarios(
    riqueza_inicial, n_cenarios, media, volatilidade, t_u_e_seed
)

## Retorno Risco Desempenho Carteiras
drawdown_max = calcular_drawdown(rrdc_seed, n_periodos)

## Custo de Capital
resultados_custo = calcular_custo_capital(Ku, Kd, T, de_ratio)

## Modelo de Markowitz
pesos_otimizados, indice_sharpe_max = otimizar_carteira(
    taxa_livre_risco, tickers, start_date, end_date
)

# Saída de dados

## Teoria da Utilidade Esperada
print("=" * 50)
print("TEORIA DA UTILIDADE ESPERADA")
print("=" * 50)
print(f"Utilidade Esperada: {utilidade_esperada:.4f}")
print(f"Equivalente Certo: {equivalente_certo:.2f}")
print()

# Plotar gráfico representativo
plt.figure(figsize=(10, 6))
plt.hist(riquezas_finais, bins=50, alpha=0.75, color='blue', edgecolor='black')
plt.axvline(equivalente_certo, color='red', linestyle='dashed', linewidth=2, label=f'Equivalente Certo: {equivalente_certo:.2f}')
plt.title('Distribuição das Riquezas Finais')
plt.xlabel('Riqueza Final')
plt.ylabel('Frequência')
plt.legend()
plt.grid(True)
plt.show()

## Retorno Risco Desempenho Carteiras
print("=" * 50)
print("RETORNO RISCO DESEMPENHO CARTEIRAS")
print("=" * 50)
print(f"Drawdown Máximo Histórico: {drawdown_max:.2%}")
print()

## Custo de Capital
print("=" * 50)
print("CUSTO DE CAPITAL")
print("=" * 50)
print(resultados_custo)
print()

## Modelo de Markowitz
print("=" * 50)
print("MODELO DE MARKOWITZ")
print("=" * 50)
print("Pesos Otimizados: ", pesos_otimizados)
print("Índice de Sharpe Máximo: ", indice_sharpe_max)
print()
