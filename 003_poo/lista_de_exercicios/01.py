"""
Elabore um programa em Python orientado a objetos que leia um número n (o número de termos de uma progressão aritmética), a1 (o primeiro termo da progressão) e r (razão) e escreva todos os termos dessa progressão, bem como a soma dos elementos (Fórmulas da P.A.: an = a1 + r x (n – 1) e  S = n * (a1 + an) / 2).
"""

class ProgressaoAritmetica:
    def __init__(self, n, a1, r):
        self.n = n      # número de termos
        self.a1 = a1    # primeiro termo
        self.r = r      # razão

    def gerar_termos(self):
        termos = []
        for i in range(self.n):
            termo = self.a1 + i * self.r
            termos.append(termo)
        return termos

    def calcular_soma(self):
        an = self.a1 + self.r * (self.n - 1)
        soma = self.n * (self.a1 + an) / 2
        return soma

    def exibir(self):
        termos = self.gerar_termos()
        soma = self.calcular_soma()
        print("Termos da P.A.:", termos)
        print("Soma dos termos:", soma)


# Programa principal
def main():
    try:
        n = int(input("Digite o número de termos da P.A.: "))
        a1 = float(input("Digite o primeiro termo (a1): "))
        r = float(input("Digite a razão (r): "))

        pa = ProgressaoAritmetica(n, a1, r)
        pa.exibir()
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if __name__ == "__main__":
    main()