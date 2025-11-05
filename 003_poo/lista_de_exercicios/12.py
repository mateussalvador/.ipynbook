"""
No universo de Dragon Ball, desenvolva um sistema em Python para simular um torneio de artes marciais, utilizando orientação a objetos. 

Crie uma classe totalmente abstrata chamada Lutador, contendo apenas métodos abstratos para obter o nome do lutador, o nível de poder e realizar um ataque. 

Em seguida, implemente subclasses como Saiyajin, Androide e Namekuseijin, cada uma com um comportamento específico ao atacar. 

O sistema deve conter um menu interativo que permita cadastrar lutadores de diferentes raças, listar todos os lutadores inscritos no torneio e simular ataques, demonstrando o uso de herança, abstração total e polimorfismo. 

Implemente também tratamento de exceções, garantindo que os nomes não estejam vazios e que o nível de poder seja um valor numérico positivo.
"""
# Imports
from abc import ABC, abstractmethod
# Constantes
# Classes

class Lutador(ABC):
    
    @property
    @abstractmethod
    def nome():
        pass

    @property
    @abstractmethod
    def poder():
        pass
    
    @abstractmethod
    def realizar_ataque():
        pass


class LutadorBase(Lutador):
    def __init__(self, nome, poder, raca):
        self._nome = nome
        self._raca = raca
        self._poder = poder
        self._ataque = "Ataque genérico"

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    @property
    def raca(self):
        return self._raca
    
    @raca.setter
    def raca(self, nova_raca):
        self._raca = nova_raca
    
    @property
    def poder(self):
        return self._poder
    
    @poder.setter
    def poder(self, novo_poder):
        self._poder = novo_poder
    
    @property
    def ataque(self):
        return self._ataque
    
    @ataque.setter
    def ataque(self, novo_ataque):
        self._ataque = novo_ataque

    def simular_ataque(self): 
        print(f"{self.nome} está atacando:")
        print(f"Ataque: {self.ataque}")
        print(f"Poder: {self.poder}")

class Saiyajin(LutadorBase):
    def __init__(self, nome, poder, raca):
        super().__init__(nome, poder, raca)
        self._ataque = "Ataque de Saiyajin"

class Androide(LutadorBase):
    def __init__(self, nome, poder, raca):
        super().__init__(nome, poder, raca)
        self._ataque = "Ataque de Androide"

class Namekuseijin(LutadorBase):
    def __init__(self, nome, poder, raca):
        super().__init__(nome, poder, raca)
        self._ataque = "Ataque de Namekuseijin"

class Torneio():
    def __init__(self):
        self._lista = []

    def add_lutador(self, lutador):
        self.lista.append(lutador)
    
    @property
    def lista(self):
        return self._lista
    


# Funções Auxiliares
def exibe_menu():
    print("-" * 20, "MENU", "-" * 20)
    print("1. Cadastrar lutador")
    print("2. Listar lutadores")
    print("3. Definir ataque do lutador")
    print("4. Simular ataque")
    print("5. Sair")

def recebe_opcao():
    opcao = input("Informe a opção desejada: ")
    print()
    return opcao

def valida_opcao(opcao):
    try:
        opcao = int(opcao)
        if opcao < 1 or opcao > 5:
            raise ValueError
        else:
            return opcao
    except ValueError:
        print("Opção informada é inválida. Tente novamente.\n")
        return 0

def recebe_raca():
    print("--- SELEÇÃO DE RAÇA DO LUTADOR ---")
    print("1. Saiyajin")
    print("2. Androide")
    print("3. Namekuseijin")
    raca = input("Informe a raça do lutador: ")
    return raca

def valida_raca(opcao):
    while True:
        if opcao != "1" and opcao != "2" and opcao != "3":
            print("Você deve informar um valor numérico entre 1 e 3. Tente novamente.\n")
            return ""
        else:
            return opcao

def recebe_nome_lutador():
    while True:
        try:
            nome = input("Informe o nome do lutador: ").strip()
            if not nome:
                print("Você deve informar um nome para o lutador.")
                raise ValueError
            else:
                return nome
        except ValueError:
            continue

def recebe_poder():
    while True:
        try:
            poder = float(input("Informe o nível do poder: "))
            print()
            if poder <= 0:
                raise ValueError
            return poder
        except ValueError:
            print("O nível de poder deve ser um valor numérico positivo. Tente novamente.\n")
            continue
            

def criar_lutador():
    while True: 
        raca = valida_raca(recebe_raca())
        if not raca:
            continue     
        nome = recebe_nome_lutador()
        poder = recebe_poder()
        
        
        match raca:
            case "1":
                return Saiyajin(nome, poder, "Saiyajin")
            case "2":
                return Androide(nome, poder, "Androide")
            case "3":
                return Namekuseijin(nome, poder, "Namekuseijin")

def cadastrar_lutador(torneio):
    lutador = criar_lutador()
    torneio.add_lutador(lutador)
    return "Lutador cadastrado com sucesso"

def listar_lutadores(torneio):
    if not torneio.lista:
        print("Ainda não existem lutadores cadastrados no torneio.\n")
    else:
        for indice, lutador in enumerate(torneio.lista):
            print(f"--- LUTADOR (Número de inscrição: {indice + 1}) ---")
            print(f"Nome: {lutador.nome}")
            print(f"Raça: {lutador.raca}")
            print(f"Poder: {lutador.poder}\n")

def definir_ataque(torneio):
    if not torneio.lista:
        print("Ainda não existem lutadores cadastrados no torneio.\n")
    else:
        while True: 
            try: 
                op = int(input("Informe o número de inscrição do lutador: "))
                if op < 1 or op > len(torneio.lista):
                    raise ValueError
                else:
                    ataque = input("Informe o novo ataque: ")
                    torneio.lista[op-1].ataque = ataque
                    return "Ataque atualizado com sucesso."
            except ValueError:
                print("Informe um lutador válido. Tente novamente.\n")
                continue

def simular_ataque(torneio):
    if not torneio.lista:
        print("Ainda não existem lutadores cadastrados no torneio.\n")
    else:
        while True: 
            try: 
                op = int(input("Informe o número de inscrição do lutador: "))
                if op < 1 or op > len(torneio.lista):
                    raise ValueError
                else:
                    print(f"{torneio.lista[op-1].nome} está atacando:")
                    print(f"Ataque: {torneio.lista[op-1].ataque}")
                    print(f"Poder: {torneio.lista[op-1].poder}")
                    return "Ataque realizado com sucesso."
            except ValueError:
                print("Informe um lutador válido. Tente novamente.\n")
                continue
                
        
# Código Principal
t1 = Torneio()

while True:
    exibe_menu()
    opcao = valida_opcao(recebe_opcao())
    if not opcao:
        continue

    match opcao:
        case 1:
            print(cadastrar_lutador(t1))
        case 2:
            listar_lutadores(t1)
        case 3:
            definir_ataque(t1)
        case 4:
            simular_ataque(t1)
        case 5:
            print("Saindo...")
            break
        case _:
            pass