"""
Módulo ES (Entrada/Saída)
Descrição: Lê os dados da ETTJ prefixada do arquivo CSV da ANBIMA.
Autor: Felipe Dornelles
Data: 06/05/2026
Versão: 1.0.0
"""
import numpy as np

def ler_curva(arquivo='CurvaZero_.csv'):
    with open(arquivo, 'r', encoding='latin-1') as f:
        linhas = f.readlines()
    inicio = None
    for i, linha in enumerate(linhas):
        if 'PREFIXADOS' in linha.upper() and 'CIRCULAR' in linha.upper():
            inicio = i
            break
    vertices, taxas = [], []
    for j in range(inicio + 2, len(linhas)):
        linha = linhas[j].strip()
        if not linha or linha == ';' or 'ERRO' in linha.upper():
            if vertices:
                break
            continue
        partes = linha.split(';')
        if len(partes) >= 2:
            try:
                v = float(partes[0].replace('.', ''))
                t = float(partes[1].replace(',', '.'))
                vertices.append(v)
                taxas.append(t)
            except ValueError:
                continue
    return np.array(vertices), np.array(taxas)