"""
multa_velocidade.py
Autor: Felipe Dornelles
Data: 03/04/2026
Versão: 0.0.1

Lê a velocidade (km/h). Se >80, informa a multa (R$5,00 por km acima do limite).
"""

LIMITE = 80          # km/h
VALOR_KM = 5.0       # R$ por km excedente


def ler_velocidade() -> float:
    """Solicita a velocidade, garantindo número positivo."""
    while True:
        try:
            v = float(input("Informe a velocidade (km/h): "))
            if v < 0:
                print("Velocidade não pode ser negativa.")
                continue
            return v
        except ValueError:
            print("Valor inválido. Use apenas números.")


def calcular_multa(velocidade: float) -> float:
    """Retorna 0 se dentro do limite ou o valor da multa."""
    if velocidade <= LIMITE:
        return 0.0
    return (velocidade - LIMITE) * VALOR_KM


def main() -> None:
    v = ler_velocidade()
    multa = calcular_multa(v)

    if multa == 0:
        print("Dentro do limite. Não houve multa.")
    else:
        print("Velocidade acima do limite.")
        print(f"Excesso: {v - LIMITE:.2f} km")
        print(f"Valor da multa: R$ {multa:.2f}")


if __name__ == "__main__":
    main()
    