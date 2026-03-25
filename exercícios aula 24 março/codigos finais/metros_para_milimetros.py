"""
Programa: metros_para_milimetros.py
Autor   : Felipe Dornelles
Data    : 03/04/2026
Versão  : 0.0.1

Descrição
-----------
Lê um valor em metros (pode ter casas decimais) e converte para
milímetros (1 m = 1 000 mm).

OBSERVACAO: escrever a vírgula em formato americano (. ponto).

"""

def metros_para_milimetros() -> None:
    """Converte metros (float) para milímetros (int) e exibe o resultado."""
    while True:
        try:
            metros = float(input(" Informe o valor em metros (ex.: 2.75): "))
            if metros < 0:
                print("  Valor não pode ser negativo.\n")
                continue
            break
        except ValueError:
            print("  Entrada inválida! Use um número (ex.: 3 ou 4.2).\n")

    milimetros = metros * 1_000          # 1 metro = 1000 milímetros
    print(f"\n🔢 {metros} metro(s) = {milimetros:.0f} milímetro(s).\n")


if __name__ == "__main__":
    metros_para_milimetros()
    