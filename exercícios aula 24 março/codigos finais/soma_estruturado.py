"""
Programa: soma_estruturado.py
Autor   : Felipe Dornelles
Data    : 03/04/2026
Versão  : 0.0.1

Descrição
-----------
Lê duas parcelas, acumula a soma e exibe o total.
"""

def soma_com_while() -> None:
    """Lê duas parcelas com while, acumula e mostra a soma."""
    parcela = 0          # contador de parcelas já lidas
    soma = 0             # acumulador da soma

    print("\n Digite duas parcelas; a cada entrada a soma parcial será guardada.")
    while parcela < 2:               # queremos exatamente duas iterações
        try:
            num = int(input(f"   parcela {parcela + 1} de 2: "))
        except ValueError:
            print("Por favor, informe um número inteiro.\n")
            continue                 # repete a mesma iteração

        soma += num
        parcela += 1                # avança o contador

    print(f"\n A soma das duas parcelas é: {soma}\n")


if __name__ == "__main__":
    soma_com_while()