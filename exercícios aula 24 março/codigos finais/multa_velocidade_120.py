"""
multa_velocidade_120.py
Autor: Felipe Dornelles
Data: 03/04/2026
Versão: 0.0.1

Lê a velocidade (km/h) de um veículo. Se >120, informa a multa
cobrando R$5,00 por km excedente.
"""

LIMITE = 120      # km/h
VALOR_KM = 5.0    # R$ por km acima do limite


def ler_velocidade():
    """Solicita a velocidade, garantindo número não‑negativo."""
    while True:
        try:
            v = float(input("Informe a velocidade (km/h): "))
            if v < 0:
                print("Velocidade não pode ser negativa.")
                continue
            return v
        except ValueError:
            print("Valor inválido. Use apenas números.")


def calcular_multa(velocidade):
    """Retorna o valor da multa ou 0 se dentro do limite."""
    if velocidade <= LIMITE:
        return 0.0
    excesso = velocidade - LIMITE
    return excesso * VALOR_KM


def main():
    v = ler_velocidade()
    multa = calcular_multa(v)

    if multa == 0.0:
        print("Dentro do limite. Não houve multa.")
    else:
        print("Velocidade acima do limite.")
        print(f"Excesso: {v - LIMITE:.2f} km")
        print(f"Valor da multa: R$ {multa:.2f}")


if __name__ == "__main__":
    main()
