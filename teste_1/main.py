"""
Programa ETTJ
Descrição: Este programa lê os dados da ETTJ pré da ANBIMA e traça o gráfico
da curva de juros usando interpolação polinomial. Versão usando programação modular.
Autor: Felipe Dornelles
Data: 06/05/2026
Versão: 1.0.0
"""
# Corrige o caminho de importação
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Importação de bibliotecas
import matplotlib.pyplot as plt
import es
import interpol

def main():
    # Alocação de memória
    vertices: list = []
    taxas: list = []
    x_interp: list = []
    y_interp: list = []

    # Entrada de dados
    vertices, taxas = es.ler_curva('CurvaZero_.csv')

    # Processamento
    x_interp, y_interp = interpol.interpolar(vertices, taxas)

    # Saída (terminal)
    print('Vertices (d.u.) | Taxa (% a.a.)')
    print('-' * 35)
    for v, t in zip(vertices, taxas):
        print(f'{v:>15.0f} | {t:.4f}')

    # Saída (gráfico)
    plt.figure()
    plt.plot(x_interp, y_interp, '-', label='Spline Cúbico')
    plt.plot(vertices, taxas, 'o', label='Dados ANBIMA')
    plt.title('ETTJ Prefixada - ANBIMA')
    plt.xlabel('Vértice (dias úteis)')
    plt.ylabel('Taxa (% a.a.)')
    plt.legend()
    plt.grid(True)
    plt.savefig('curva_ettj.png')
    plt.show()

# Executar
if __name__ == '__main__':
    main()