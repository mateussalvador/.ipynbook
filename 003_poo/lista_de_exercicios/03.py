"""
Faça um programa em Python orientado a objetos que receba uma frase dada pelo usuário e a criptografe. A criptografia consistirá na troca das vogais da frase por um número correspondente: A - 4, E - 3, I - 1, O - 0, U - 8.
"""

class Criptografia:
    def __init__(self, frase):
        self._frase_original = frase
        print("Criptografando a frase...")
        self._frase_criptografada = self._executar_criptografia(self._frase_original)
        print(self._frase_criptografada)

    # Método responsável por criptografar a frase.
    def _executar_criptografia(self, texto):
        """Este método contém a lógica de criptografia."""
        texto_processado = texto.lower()
        texto_processado = texto_processado.replace("a", "4")
        texto_processado = texto_processado.replace("e", "3")
        texto_processado = texto_processado.replace("i", "1")
        texto_processado = texto_processado.replace("o", "0")
        texto_processado = texto_processado.replace("u", "8")
        return texto_processado
    
f1 = Criptografia("O dia está belo.")
