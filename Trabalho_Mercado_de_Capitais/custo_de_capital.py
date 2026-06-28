"""
custo_de_capital.py

Descrição: Este programa calcula o Ke e o WACC para diferentes níveis de alavancagem (D/E) usando a biblioteca pandas.
Autor: Felipe Dornelles e Affonso Pereira
Data: 17/03/2026
Versão: 1.0.0
"""

import pandas as pd

# Alocação de memória
# input inserido no main para eventual substituicao mais simples:
# Ku, Kd, T, de_ratio

# Entrada de dados
# input inserido no main para eventual substituicao mais simples

# Processamento de dados
def calcular_custo_capital(Ku, Kd, T, de_ratio):
    """
    Calcula Ke e WACC para diferentes níveis de alavancagem.
    
    Args:
        Ku: Custo de capital desalavancado
        Kd: Custo da dívida
        T: Imposto
        de_ratio: Série de D/E ratios
    
    Returns:
        DataFrame com D/E Ratio, Ke e WACC
    """
    ke_values = Ku + (Ku - Kd) * de_ratio * (1 - T)
    wacc_values = (ke_values / (1 + de_ratio)) + (
        Kd * (1 - T) * de_ratio / (1 + de_ratio)
    )
    
    resultados = pd.DataFrame({
        'D/E Ratio': de_ratio,
        'Ke': ke_values,
        'WACC': wacc_values
    })
    
    return resultados

# Saída de dados
# output inserido no main para eventual substituicao mais simples
