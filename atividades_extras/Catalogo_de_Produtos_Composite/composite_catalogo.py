from abc import ABC, abstractmethod  # Importa as classes ABC e abstractmethod para definir classes abstratas

# Define a classe base para os componentes do catálogo
class CatalogComponent(ABC):
    # Método abstrato que deve ser implementado por subclasses
    @abstractmethod
    def show_details(self):
        raise NotImplementedError()  # Levanta um erro se o método não for implementado
    
# Classe que representa um produto, herda de CatalogComponent
class Product(CatalogComponent):
    def __init__(self, name: str, price: float) -> None:
        self.name = name  # Atributo para armazenar o nome do produto
        self.price = price  # Atributo para armazenar o preço do produto
    
    # Implementação do método show_details para exibir informações do produto
    def show_details(self) -> None:
        print(f"Nome: {self.name}\n Preço: {self.price} R$")  # Exibe o nome e preço do produto

# Classe que representa uma categoria, herda de CatalogComponent
class Category(CatalogComponent):
    def __init__(self, name: str) -> None:
        self.name = name  # Atributo para armazenar o nome da categoria
        self.components = []  # Lista para armazenar produtos ou subcategorias

    # Método para adicionar um componente (produto ou subcategoria) à categoria
    def add(self, component: CatalogComponent) -> None:
        self.components.append(component)  # Adiciona o componente à lista

    # Método para remover um componente da categoria
    def remove(self, component: CatalogComponent) -> None:
        self.components.remove(component)  # Remove o componente da lista

    # Implementação do método show_details para exibir informações da categoria e seus componentes
    def show_details(self) -> None:
        print(f"Nome: {self.name}")  # Exibe o nome da categoria
        for component in self.components:
            component.show_details()
    

    
if __name__ == "__main__":
    # Criando produtos
    product1 = Product("Produto A", 10.0)
    product2 = Product("Produto B", 20.0)
    product3 = Product("Produto C", 30.0)

    # Criando categorias
    category1 = Category("Categoria 1")
    category2 = Category("Categoria 2")
    subcategory1 = Category("Subcategoria 1")

    # Adicionando produtos às categorias
    category1.add(product1)
    category1.add(product2)
    category2.add(product3)

    # Adicionando subcategoria à categoria
    category1.add(subcategory1)

    # Adicionando um produto à subcategoria
    subcategory1.add(Product("Produto D", 40.0))

    # Exibindo a estrutura completa do catálogo
    print("Estrutura do Catálogo:")
    category1.show_details()
    category2.show_details()