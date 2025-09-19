"""
Crie um programa em Python utilizando orientação a objetos para gerenciar uma lista de produtos de um carrinho de compras. 

Implemente uma classe chamada Produto, com:

  - atributos privados (__nome, __preco e __quantidade); e 
  - métodos públicos para acessar e modificar esses valores de forma segura (getters e setters). 
  
Em seguida, implemente uma classe CarrinhoDeCompras, que mantém uma lista de objetos Produto e possui métodos para adicionar um produto ao carrinho, remover um produto pelo nome, calcular o valor total da compra e listar os produtos com suas quantidades e preços individuais. 

O programa principal deve permitir que o usuário adicione e remova produtos, visualize o conteúdo do carrinho e o total da compra. Utilize encapsulamento para proteger os dados dos produtos e boas práticas de organização orientada a objetos.

"""
import json

class Produto():
    """Classe que permite criar objetos do tipo Produto que serão inseridos ao carrinho de compras."""

    def __init__(self, nome : str, preco : int | float, quantidade : int) -> None:
        """Inicializa objetos do tipo Produto()"""
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade
    
    @property
    def nome_produto(self) -> str:
        """GET do nome do produto"""
        return self.__nome

    @nome_produto.setter
    def nome_produto(self, novo_nome : str):
        """SET para novos nomes de produto"""
        self.__nome = novo_nome

    @property
    def preco(self) -> str | float:
        """GET do preço do produto"""
        return self.__preco

    @preco.setter
    def preco(self, novo_preco) -> None:
        """SET para novos preços de produto"""
        self.__preco = novo_preco

    @property
    def quantidade(self) -> int:
        """GET da quantidade de produtos"""
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, nova_qtd : int) -> None:
        """SET para nova quantidade de produto"""
        self.__quantidade = nova_qtd


# Classe Carrinho
class CarrinhoDeCompras():
    """Classe que permite instanciar diferentes objetos do tipo CarrinhoDeCompras()"""
    def __init__(self, nome : str = "Carrinho de Compras") -> None:
        self.nome = nome
        self.lista = []

    # Adicionando Produtos
    def add_produto(self, produto):
        """Método para adição de objetos do tipo Produto() ao carrinho"""

        d = {
            "Nome": produto.nome_produto,
            "Preço": produto.preco,
            "Quantidade": produto.quantidade,
        }
    
        self.lista.append(d)
        print(f"({d["Quantidade"]}) {d["Nome"]} foi adicionado ao carrinho.", end="\n\n")

    # Removendo Produtos
    def remove_produto(self, produto):
        if not self.lista:
            print("A lista está vazia!", end="\n\n")
        else: 
            for indice, item in enumerate(self.lista):
                if item["Nome"] == produto.nome_produto:
                    print(f"Removendo {produto.nome_produto} da lista...", end="\n\n")
                    self.lista.pop(indice)
                    break
            else:
                print(f"{produto.nome_produto} não está na lista.", end="\n\n")
        
    # Retornando valor total
    def valor(self):
        total = 0
        for item in self.lista:
            total += item["Preço"] * item["Quantidade"]
        print(f"Valor Total: R${total:.2f}", end="\n\n")


    # Listando Produtos
    def lista_produtos(self):
        print("-" * 17 + " LISTA COMPLETA " + "-" * 17, end="\n\n")
        for item in self.lista:
            print(f"Produto: {item["Nome"]}")
            print(f"Preço: R$ {item["Preço"]:.2f}")
            print(f"Quantidade: {item["Quantidade"]}")
            print("\n" + "-" * 50, end="\n\n")


# Instanciando
p1 = Produto("Caixa de Leite", 50, 2)
p2 = Produto("Óleo", 5.20, 5)
p3 = Produto("Arroz", 15.20, 4)
p4 = Produto("Picanha", 47.20, 2)
p5 = Produto("Detergente", 3.70, 12)
c1 = CarrinhoDeCompras()

# Adicionando produtos ao carrinho
c1.add_produto(p1)
c1.add_produto(p2)
c1.add_produto(p3)
c1.add_produto(p4)
c1.add_produto(p5)

# Fazendo testes
c1.lista_produtos()
c1.remove_produto(p2)
c1.lista_produtos()
c1.valor()
