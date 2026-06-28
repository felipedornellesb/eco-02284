"""
modelo_de_markowitz.py

Descrição: Este programa otimiza uma carteira de 4 ativos utilizando a biblioteca scipy.optimize e dados obtidos com a biblioteca yfinance.
Autores: Felipe Dornelles e Affonso Pereira
Data: 17/06/2026
Versão: 1.0.0
"""

import numpy as np
import scipy.optimize as opt
import yfinance as yf

# Alocação de memória
# input inserido no main para eventual substituicao mais simples:
# taxa_livre_risco, tickers, start_date, end_date

# Entrada de dados
# input inserido no main para eventual substituicao mais simples

# Processamento de dados
def indice_sharpe(weights, media_ativos, cov_matrix, taxa_livre_risco):
    """
    Calcula o Índice de Sharpe para uma carteira.
    
    Args:
        weights: Pesos dos ativos
        media_ativos: Média dos retornos dos ativos
        cov_matrix: Matriz de covariância
        taxa_livre_risco: Taxa livre de risco
    
    Returns:
        Índice de Sharpe
    """
    retorno_esperado = np.dot(weights, media_ativos)
    risco = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return (retorno_esperado - taxa_livre_risco) / risco

def restricao_pesos(weights):
    """
    Define a restrição de soma dos pesos igual a 1.
    
    Args:
        weights: Pesos dos ativos
    
    Returns:
        Soma dos pesos menos 1
    """
    return np.sum(weights) - 1

def obter_dados(tickers, start_date, end_date):
    """
    Obtém dados históricos e calcula média e covariância.
    
    Args:
        tickers: Lista de tickers
        start_date: Data inicial
        end_date: Data final
    
    Returns:
        media_ativos: Média dos retornos
        cov_matrix: Matriz de covariância
    """
    dados = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)['Close']
    retornos = np.log(dados / dados.shift(1)).dropna()
    media_ativos = retornos.mean().values
    cov_matrix = retornos.cov().values
    return media_ativos, cov_matrix

def otimizar_carteira(taxa_livre_risco, tickers, start_date, end_date):
    """
    Otimiza a carteira maximizando o Índice de Sharpe.
    
    Args:
        taxa_livre_risco: Taxa livre de risco
        tickers: Lista de tickers
        start_date: Data inicial
        end_date: Data final
    
    Returns:
        pesos_otimizados: Pesos ótimos da carteira
        indice_sharpe_max: Índice de Sharpe máximo
    """
    media_ativos, cov_matrix = obter_dados(tickers, start_date, end_date)
    n_ativos = len(media_ativos)
    pesos_iniciais = np.ones(n_ativos) / n_ativos
    limites = tuple((0, 1) for _ in range(n_ativos))
    restricoes = ({'type': 'eq', 'fun': restricao_pesos})
    
    resultado = opt.minimize(lambda w: -indice_sharpe(w, media_ativos, cov_matrix, taxa_livre_risco),
                             pesos_iniciais, method='SLSQP', bounds=limites, constraints=restricoes)
    
    pesos_otimizados = resultado.x
    indice_sharpe_max = -resultado.fun
    
    return pesos_otimizados, indice_sharpe_max

# Saída de dados
# output inserido no main para eventual substituicao mais simples
