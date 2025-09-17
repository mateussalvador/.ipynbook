"""
Faça um programa em Python orientado a objetos que, a partir de uma string digitada pelo usuário, imprima:
◦ O número de caracteres da string;
◦ A string com todas suas letras em maiúsculo;
◦ A string com todas suas letras em minúsculo;
◦ O número de vogais da string;
◦ Se a substring “IFB” aparece no texto (ignorando 
maiúsculas/minúsculas).

"""

class String:
    def __init__(self, string):
        self.string = string
        self.num_caracteres = None
        self.maiusculo = None
        self.minusculo = None
        self.num_vogais = None
        self.ifb_aparece = None
    
    def analisa(self):
        self.num_caracteres = len(self.string)
        self.maiusculo = self.string.upper()
        self.minusculo = self.string.lower()
        self.num_vogais = self.string.lower().count('a') + self.string.lower().count('e') + self.string.lower().count('i') + self.string.lower().count('o') + self.string.lower().count('u')
        self.ifb_aparece = True if "ifb" in self.string.lower() else False

    def get_analise(self):
        self.analisa()
        print(f"Número de caracteres = {self.num_caracteres}")
        print(f"Texto em Maiúsculo = {self.maiusculo}")
        print(f"Texto em Minúsculo = {self.minusculo}")
        print(f"Número de vogais = {self.num_vogais}")
        print(f"'IFB' aparece no texto? = {"Sim" if self.ifb_aparece else "Não"}\n")

s1 = String("Mateus IfB")
s2 = String("RAIMUNDINHO NONATO FERNANDO EGIDIO DA SILVA If")
s3 = String("RAIMUNDINHO NONATO FERNANDO EGIDIO DA SILVA ifb")

s1.get_analise()
s2.get_analise()
s3.get_analise()