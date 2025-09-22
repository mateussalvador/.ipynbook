"""
Desenvolva uma classe Departamento com nome e um vetor de objetos Funcionario, onde cada funcionário tem nome e salário, permitindo que funcionários existam independentemente do departamento para que possam ser adicionados ou removidos livremente (agregação). 

Implemente métodos no Departamento para adicionar funcionários, calcular a média salarial e listar todos os funcionários. 

Crie um programa com menu interativo no console que permita criar departamentos, criar funcionários, adicionar funcionários a departamentos, listar funcionários e mostrar a média salarial, além de permitir sair do programa.
"""


# Criando as classes
class Departamento:
    def __init__(self, nome):
        self._nome = nome
        self.lista_funcionarios = []

    @property
    def nome(self):
        return self._nome 
    
    def listar_funcionarios(self):
        if not self.lista_funcionarios:
            print("Este departamento ainda não possui funcionários.")
        else:
            for funcionario in self.lista_funcionarios:
                print(funcionario.nome)
                print(funcionario.salario)
                print("-" * 30)
        
    def adicionar_funcionarios(self, funcionario):
        self.lista_funcionarios.append(funcionario)
        print(f"Funcionário {funcionario.nome} adicionado ao departamento com sucesso.")
    
    def mostrar_media_salarial(self):
        if not self.lista_funcionarios:
            return "Este departamento ainda não possui funcionários."
        else:
            media = 0
            for funcionario in self.lista_funcionarios:
                media += funcionario.salario
            return f"A média salarial do departamento é {media}."

class Funcionario:
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    @property
    def nome(self):
        return self._nome 
    
    @property
    def salario(self):
        return self._salario 


# Criando métodos que auxiliarão o programa
def exibir_menu():
    print("-" * 30, "MENU", "-" * 30)
    print("1. Criar departamento")
    print("2. Criar funcionário")
    print("3. Adicionar funcionário a departamento")
    print("4. Listar funcionários")
    print("5. Mostrar a média salarial")
    print("6. Sair")

def recebe_e_valida_opcao():
    while True:
        try:  
            opcao = int(input("Informe a opção desejada: "))

            if opcao < 1 or opcao > 6:
                raise ValueError
            
            return opcao

        except ValueError:
            print("Opção Inválida! Tente novamente!")
            print("Você deve informar um valor numérico inteiro entre 1 e 6.\n")
            continue

def cria_departamento():
    nome = input("Informe o nome do departamento: ")
    novo_departamento = Departamento(nome)
    return novo_departamento

def cria_funcionario():
    nome = input("Informe o nome do funcionário: ")
    salario = input(f"Informe o salaŕio de {nome}: ")

    novo_funcionario = Funcionario(nome, salario)
    return novo_funcionario

def verifica_existencia_departamentos(lista_departamentos):
    if not lista_departamentos:
        print("Não existem departamentos criados. Você deve criar um primeiro.")
        return False
    else:
        return True

# Funcionários
def verifica_existencia_funcionarios(lista_funcionarios):
    if not lista_funcionarios:
        print("Não existem funcionários criados. Você deve criar um primeiro.")
        return False
    else:
        return True

def lista_e_seleciona_departamento(lista_departamentos):
    for indice, departamento in enumerate(lista_departamentos):
        print(f"{indice + 1} - {departamento.nome}")

    while True: 
        try: 
            opcao = int(input("Selecione o departamento que deseja obter informações: "))

            if opcao < 1 or opcao > len(lista_departamentos):
                raise ValueError

            return opcao - 1
        
        except ValueError:
            print("Erro! Selecione um departamento existente.")

# Lista e seleciona funcionários
def lista_e_seleciona_funcionarios(lista_funcionarios):
    for indice, funcionario in enumerate(lista_funcionarios):
        print(f"{indice + 1} - {funcionario.nome}")

    while True: 
        try: 
            opcao = int(input("Selecione o funcionário que deseja adicionar ao departamento: "))

            if opcao < 1 or opcao > len(lista_funcionarios):
                raise ValueError

            return opcao - 1
        
        except ValueError:
            print("Erro! Selecione um funcionário existente.")


# Listas que armazenarão os objetos
lista_departamentos = []
lista_funcionarios = []

# Execução principal
while True: 
    exibir_menu()
    opcao = recebe_e_valida_opcao()

    match opcao:
        # Cria departamento
        case 1:
            lista_departamentos.append(cria_departamento())
        # Cria funcionário
        case 2:
            lista_funcionarios.append(cria_funcionario())
        
        # Adicionar funcionário a departamento
        case 3:
            if verifica_existencia_departamentos(lista_departamentos) and verifica_existencia_funcionarios(lista_funcionarios):
                num_departamento = lista_e_seleciona_departamento(lista_departamentos)
                num_funcionario = lista_e_seleciona_funcionarios(lista_funcionarios)
                lista_departamentos[num_departamento].adicionar_funcionarios(lista_funcionarios[num_funcionario])
            else:
                continue

        case 4:
            ...
    
        case 5:
            ...
    
        case 6:
            ...