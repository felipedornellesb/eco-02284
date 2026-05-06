# Processamento - cálculo da soma dos números dados

def somar(parcelas):
    j = 0
    soma = 0

    while j < 2:
        soma = soma + parcelas[j] 
        j += 1 

    return soma
