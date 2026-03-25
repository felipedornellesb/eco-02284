"""
temperatura_ambiente.py
Autor: Felipe Dornelles
Data: 03/04/2026
Versão: 0.0.1

Lê a temperatura em °C e indica se está frio, agradável ou quente.
"""

def ler_temperatura() -> float:
    """Solicita a temperatura, aceita número decimal."""
    while True:
        try:
            t = float(input("Informe a temperatura (°C): "))
            return t
        except ValueError:
            print("Valor inválido. Use apenas números.")


def classificar(temperatura: float) -> str:
    """Retorna a classificação conforme faixa de temperatura."""
    if temperatura <= 18:
        return "Está frio."
    if temperatura <= 28:
        return "Está agradável."
    return "Está quente."


def main() -> None:
    temp = ler_temperatura()
    print(classificar(temp))


if __name__ == "__main__":
    main()
