"""
Implemente uma classe Impressora com o método imprimir(Documento d), que recebe um objeto da classe Documento e imprime suas informações na tela.

A classe Documento deve conter os atributos título e conteúdo.


A classe Impressora apenas utiliza o documento, sem manter uma referência permanente a ele,

caracterizando uma relação de dependência.


Desenvolva um programa com um menu interativo no console que permita criar vários documentos, visualizar seu conteúdo

por meio da impressora e encerrar o programa.

"""

class Impressora():
  def imprimir(self, documento):
      print("\n--- IMPRIMINDO DOCUMENTO ---")
      print(f"TÍTULO: {documento.titulo.upper()}")
      print(f"CONTEÚDO: {documento.conteudo}")
      print("--------------------------\n")

class Documento():
    def __init__(self, titulo, conteudo):
        self._titulo = titulo
        self._conteudo = conteudo
    
    @property
    def titulo(self):
        return self._titulo

    @property
    def conteudo(self):
        return self._conteudo

# --- Funções do Menu ---

def exibe_menu():
  print("-" * 15, "MENU", "-" * 15)
  print("1. Criar documento")
  print("2. Visualizar Documentos")
  print("3. Encerrar")

def recebe_opcao():
  opcao = input("Selecione a opção desejada: ")
  return opcao 

def cria_documento():
    titulo_doc = input("Informe o título do documento: ")
    conteudo_doc = input("Informe o conteúdo do documento: ")
    novo_documento = Documento(titulo_doc, conteudo_doc)
    print("Documento criado com sucesso!\n")
    return novo_documento

# Ajuste principal aqui: a função agora também recebe o objeto impressora
def listar_e_imprimir_documentos(lista_documentos, impressora):
    # Uma boa prática: verificar se a lista está vazia primeiro
    if not lista_documentos:
        print("\nNenhum documento foi criado ainda.\n")
        return # Encerra a função

    print("\n--- Documentos Criados ---")
    for indice, documento in enumerate(lista_documentos):
       print(f"{indice + 1} - {documento.titulo}")
    
    while True: 
        try:
            # Pede ao usuário para escolher qual documento imprimir
            opcao_str = input("Informe o número do documento que deseja imprimir (ou 'c' para cancelar): ")
            if opcao_str.lower() == 'c':
                print()
                break

            opcao = int(opcao_str)

            if 1 <= opcao <= len(lista_documentos):
                documento_escolhido = lista_documentos[opcao - 1]
                # A mágica acontece aqui: usamos a impressora para exibir!
                impressora.imprimir(documento_escolhido)
                break
            else:
                # Mensagem para números fora do intervalo
                print("Erro: Número inválido. Tente novamente.")
    
        except ValueError:
            # Mensagem para entradas que não são números
            print("Erro: Entrada inválida. Por favor, insira um número.")
            continue

# --- Lógica Principal ---

i1 = Impressora()
documentos_criados = []

while True:
    exibe_menu()
    opcao = recebe_opcao()
    match opcao:
        case "1":
            documentos_criados.append(cria_documento())

        case "2":
            # Agora passamos a impressora como argumento
            listar_e_imprimir_documentos(documentos_criados, i1)
        
        case "3":
            print("Saindo...")
            break
        case _:
            print("\nOpção Inválida! Por favor, tente novamente.\n")
            continue