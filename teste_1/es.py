"""
Programa es.py
Descrição:
Este módulo contém os dados da ETTJ Pré da ANBIMA.
Autor: Felipe Dornelles Brasil
Versão: 1.0.0
"""

def ler_curva_pre():
    vertices = [126, 252, 378, 504, 630, 756, 882, 1008, 1134, 1260, 1386, 1512,
                1638, 1764, 1890, 2016, 2142, 2268, 2394, 2520, 2646]
    taxas = [13.9754, 13.7070, 13.5843, 13.5489, 13.5633, 13.6036, 13.6553,
             13.7095, 13.7610, 13.8072, 13.8469, 13.8797, 13.9060, 13.9262,
             13.9410, 13.9511, 13.9571, 13.9597, 13.9593, 13.9566, 13.9520]
    return vertices, taxas
