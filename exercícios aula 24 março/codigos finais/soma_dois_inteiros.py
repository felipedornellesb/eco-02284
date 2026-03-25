"""
Programa: soma_dois_inteiros.py
Autor   : Felipe Dornelles
Data    : 03/04/2026
Versão  : 0.0.1

Descrição
-----------
Solicita ao usuário dois números inteiros, calcula a soma e exib
o resultado na tela.
"""

def soma_dois_inteiros() -> None:
    """Lê dois inteiros, soma‑os e imprime o resultado."""
    while True:
        try:
            a = int(input("🔢 Digite o primeiro número inteiro: "))
            b = int(input("🔢 Digite o segundo número inteiro: "))
            break                        # sai do laço quando a conversão funciona
        except ValueError:
            print(" Valor inválido! Use apenas números inteiros.\n")

    soma = a + b
    print(f"\n {a} + {b} = {soma}\n")


if __name__ == "__main__":
    soma_dois_inteiros()