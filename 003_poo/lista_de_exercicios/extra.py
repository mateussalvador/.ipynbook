"""

Exercitando o conhecimento sobre Orientação a Objetos:

1. Crie uma classe Carro (Nome)

2. Crie uma classe Motor (Nome)

3. Crie uma classe Fabricante (Nome)

4. Faça a ligação entre Carro tem Motor

Obs.: Um motor pode ser de vários carros

5. Faça a ligação entre Carro e Fabricante

Obs.: Um fabricante pode fabricar vários carros

# Exiba o nome do carro, motor e fabricante na tela

"""
class Carro:
    def __init__(self, nome_modelo, motor_obj, fabricante_obj):
        self.modelo = nome_modelo
        self._motor = motor_obj
        self._fabricante = fabricante_obj

    @property
    def estado_motor(self):
        # Acessa o estado diretamente através do objeto motor
        return f"Estado do motor: {self._motor.estado}"

    def acelerar(self):
        # Acessa os nomes dos objetos associados diretamente no método
        print(f"{self.modelo}, da fabricante {self._fabricante.nome}, motor {self._motor.nome} está acelerando. RANDANDANDANDAN")

    def fundir_motor(self):
        self._motor.fundir()
    
    def exibir_info(self):
        print(f"Carro: {self.modelo}, Motor: {self._motor.nome}, Fabricante: {self._fabricante.nome}")

class Motor:
    def __init__(self, nome):
        self.nome = nome
        self.estado = "Saudável"
    
    def fundir(self):
        print(f"O motor {self.nome} fundiu...")
        self.estado = "Fundido"

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

# --- Instanciando os objetos ---
m1 = Motor("V8 4.0")
f1 = Fabricante("Fiat")

m2 = Motor("Fire 1.0")
f2 = Fabricante("Mercedes")

# --- Criando os carros e associando as partes ---
c1 = Carro("Palio", m2, f1)
c2 = Carro("Uno", m2, f1)
c3 = Carro("AMG GT", m1, f2)

# --- Exibindo as informações conforme solicitado ---
print("--- Informações dos Carros ---")
c1.exibir_info()
c2.exibir_info()
c3.exibir_info()
print("-" * 30)

# --- Testando a interação entre os objetos ---
print("\n--- Testando Interações ---")
c3.acelerar()
print(c3.estado_motor)
c3.fundir_motor()
print(c3.estado_motor)