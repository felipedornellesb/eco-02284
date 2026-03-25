
"""
Programa soma_estruturado
Descrição
Este programa soma dois números, usando a estrutura de controle de fluxo de execução while.

Autor: Felipe Dornelles
Data: 03/24/2026
Versão: 0.0.1
"""

# Alocacao de memoria
soma: float = 0
valor: float = 0
i: int = 0
num_val: int = 0

# Entrada de dados
num_val = int(input("Qual o número de valores?\n"))


#  processamento de dados
while i < num_val:
    valor = float(input("Digite um número.\n"))
    soma = soma + valor
    i = i + 1
    media = soma/num_val
# Saida de dados
print('A media dos numeros é:', media)