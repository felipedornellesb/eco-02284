"""
Programa interpol.py
Descrição:
Este módulo contém as funções usadas para realizar a interpolação
polinomial com numpy.
Autor: Felipe Dornelles Brasil
Versão: 1.0.0
"""

import numpy as np


def interpolar_curva(vertices, taxas, pontos=500):
    x = np.asarray(vertices, dtype=float)
    y = np.asarray(taxas, dtype=float)
    grau = len(x) - 1
    p = np.poly1d(np.polyfit(x, y, grau))
    xs = np.linspace(x.min(), x.max(), pontos)
    ys = p(xs)
    return xs, ys
