"""
Módulo Interpol (Interpolação)
Descrição: Realiza interpolação polinomial (Spline Cúbico) da curva de juros.
Autor: Felipe Dornelles
Data: 06/05/2026
Versão: 1.0.0
"""

import numpy as np
from scipy.interpolate import CubicSpline

def interpolar(x, y, n=500):
    # Ajuste do modelo Spline Cúbico
    modelo = CubicSpline(x, y)

    # Geração dos pontos interpolados
    x_novo = np.linspace(x.min(), x.max(), n)
    y_novo = modelo(x_novo)

    return x_novo, y_novo