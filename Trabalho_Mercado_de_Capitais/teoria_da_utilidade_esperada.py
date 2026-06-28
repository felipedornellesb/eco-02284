"""
teoria_da_utilidade_esperada.py

Descrição: Este programa simula e plota a função de utilidade U(W) = ln(W) e seu Equivalente Certo.
Autores: Affonso Pereira e Felipe Dornelles
Data: 17/03/2026
Versão: 1.0.0
"""

import numpy as np

# Alocação de memória
# input inserido no main para eventual substituicao mais simples:
# riqueza_inicial, n_cenarios, media, volatilidade, t_u_e_seed

# Entrada de dados
def gerar_cenarios(riqueza_inicial, n_cenarios, media, volatilidade, t_u_e_seed):
    """
    Gera cenários de retornos e calcula utilidade esperada e equivalente certo.
    
    Args:
        riqueza_inicial: Riqueza inicial
        n_cenarios: Número de cenários
        media: Média dos retornos
        volatilidade: Volatilidade dos retornos
        t_u_e_seed: Seed para reprodutibilidade
    
    Returns:
        riquezas_finais: Array de riquezas finais
        utilidade_esperada: Utilidade esperada
        equivalente_certo: Equivalente certo
    """
    np.random.seed(t_u_e_seed)
    retornos = np.random.normal(loc=media, scale=volatilidade, size=n_cenarios)
    
    # Processamento de dados
    riquezas_finais = riqueza_inicial * (1 + retornos)
    utilidades = np.log(riquezas_finais)
    utilidade_esperada = np.mean(utilidades)
    equivalente_certo = np.exp(utilidade_esperada)
    
    return riquezas_finais, utilidade_esperada, equivalente_certo

# Processamento de dados
# Processamento realizado dentro da função gerar_cenarios

# Saída de dados
# output inserido no main para eventual substituicao mais simples
