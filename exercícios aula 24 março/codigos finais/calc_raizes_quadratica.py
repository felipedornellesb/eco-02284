"""
calc_raizes_quadratica.py
Autor: Felipe Dornelles
Data: 03/04/2026
Versão: 0.0.1

Lê os coeficientes a, b e c de ax² + bx + c = 0 e calcula as raízes.
"""

import cmath  # raízes complexas quando Δ < 0


def ler_coeficientes():
    """Solicita a, b e c garantindo que a seja diferente de zero."""
    while True:
        try:
            a = float(input("Coeficiente a (≠ 0): "))
            if a == 0:
                print("O coeficiente a não pode ser zero.")
                continue
            b = float(input("Coeficiente b: "))
            c = float(input("Coeficiente c: "))
            return a, b, c
        except ValueError:
            print("Valor inválido. Use apenas números.")


def calcular_raizes(a, b, c):
    """Retorna as duas raízes (possivelmente complexas)."""
    delta = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(delta)) / (2*a)
    raiz2 = (-b - cmath.sqrt(delta)) / (2*a)
    return raiz1, raiz2


def main():
    a, b, c = ler_coeficientes()
    r1, r2 = calcular_raizes(a, b, c)

    print("\nResultado:")
    if r1.imag == 0 and r2.imag == 0:
        # raízes reais
        r1, r2 = r1.real, r2.real
        if r1 == r2:
            print(f"Raiz dupla: x = {r1:.5f}")
        else:
            print(f"Raízes reais: x₁ = {r1:.5f}  e  x₂ = {r2:.5f}")
    else:
        # raízes complexas
        print(f"Raízes complexas: x₁ = {r1:.5f}  e  x₂ = {r2:.5f}")


if __name__ == "__main__":
    main()
