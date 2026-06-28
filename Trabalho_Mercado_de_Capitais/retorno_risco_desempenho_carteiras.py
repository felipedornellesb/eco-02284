"""
retorno_risco_desempenho_carteiras.py

Descrição: Este programa calcula o Drawdown Máximo Histórico de uma série temporal de retornos acumulados.
Autor: Felipe Dornelles e Affonso Pereira
Data: 17/03/2026
Versão: 1.0.0
"""

import numpy as np
import pandas as pd

# Alocação de memória
# input inserido no main para eventual substituicao mais simples:
# rrdc_seed, n_periodos

# Entrada de dados
def gerar_retornos(rrdc_seed, n_periodos):
    """
    Gera série temporal de retornos acumulados.
    
    Args:
        rrdc_seed: Seed para reprodutibilidade
        n_periodos: Número de períodos
    
    Returns:
        serie_temporal: Série de retornos acumulados
    """
    np.random.seed(rrdc_seed)
    retornos = np.random.normal(loc=0.001, scale=0.02, size=n_periodos)
    serie_temporal = pd.Series((1 + retornos).cumprod(), name='Retorno Acumulado')
    return serie_temporal

# Processamento de dados
def drawdown_maximo(serie):
    """
    Calcula o Drawdown Máximo de uma série temporal.
    
    Args:
        serie: Série temporal de retornos acumulados
    
    Returns:
        Drawdown máximo
    """
    cum_max = serie.cummax()
    drawdown = (serie - cum_max) / cum_max
    return drawdown.min()

def calcular_drawdown(rrdc_seed, n_periodos):
    """
    Função wrapper que gera retornos e calcula drawdown máximo.
    
    Args:
        rrdc_seed: Seed para reprodutibilidade
        n_periodos: Número de períodos
    
    Returns:
        drawdown_max: Drawdown máximo histórico
    """
    serie_temporal = gerar_retornos(rrdc_seed, n_periodos)
    drawdown_max = drawdown_maximo(serie_temporal)
    return drawdown_max

# Saída de dados
# output inserido no main para eventual substituicao mais simples
