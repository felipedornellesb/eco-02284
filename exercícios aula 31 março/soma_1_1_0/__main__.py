"""
Programa Soma
Descrição: Este programa calcula a soma de dois números reais dados pelo usuário. Esta é a versão usando programação modular.
Autor: Felipe Dornelles
Data: 31/03/2026
Versão: 1.1.0
"""

# importação de bibliotecas
import entrada
import calculadora
import escritora

def main():
    # Alocação de memória
    parcelas: list = [0,0]
    parcela1: float = 0
    parcela2: float = 0
    soma: float = 0
    i = 0
    j =0
    # Entrada de dados
    parcelas = entrada.entrada()
    
    # Processamento
    resultado = calculadora.somar(parcelas)
    
    # Saida
    escritora.impressora(parcelas, resultado)

# Executar
if __name__ == "__main__":
    main()