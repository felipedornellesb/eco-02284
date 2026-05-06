# Entrada de dados

def entrada():
    i = 0
    parcelas = [0, 0]
    while i < 2:
        parcelas[i] = float(input(f"Digite a parcela {i + 1}: "))
        i = i + 1
    return parcelas