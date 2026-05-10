"""
Programa main.py
Descrição:
Este programa lê os dados da ETTJ Pré da ANBIMA e traça o gráfico da
curva de juros usando interpolação polinomial.
Autor: Felipe Dornelles Brasil
Versão: 1.0.1
"""

import matplotlib.pyplot as plt
import numpy as np
import es
import interpol


def main():
    vertices, taxas = es.ler_curva_pre()
    xs, ys = interpol.interpolar_curva(vertices, taxas)

    v = np.asarray(vertices, dtype=float) / 252
    x = xs / 252

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, ys, color="#1a5fa8", lw=2.2, label="Curva interpolada")
    ax.scatter(v, taxas, color="#e63946", s=28, zorder=5, label="Pontos")

    ax.set_xlabel("Prazo (anos)")
    ax.set_ylabel("Taxa (% a.a.)")
    ax.set_title("ETTJ Pré — ANBIMA")
    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
