class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class ClienteNull:
    def __init__(self, nome=None, email=None):
        self.nome = nome
        self.email = email

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class ProdutoNull:
    def __init__(self, nome=None, preco=None):
        self.nome = nome
        self.preco = preco

class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class EnderecoNull:
    def __init__(self, rua=None, cidade=None):
        self.rua = rua
        self.cidade = cidade

class Pedidos:
    # Simulação de busca de dados
    def buscar_cliente(self, id):
        if id == 1:
            return Cliente("João", "joao@example.com")
        else:
            return ClienteNull(None, None)

    def buscar_produto(self, codigo):
        if codigo == "ABC":
            return Produto("Produto A", 100.0)
        else:
            return ProdutoNull(None, None)

    def buscar_endereco(self, cliente):
        if cliente and cliente.nome == "João":
            return Endereco("Rua Principal", "Cidade Exemplo")
        else:
            return EnderecoNull(None, None)

    # Código que contém múltiplas verificações de None
    def processar_pedido(self, cliente_id, codigo_produto):
        cliente = self.buscar_cliente(cliente_id)
        
        produto = self.buscar_produto(codigo_produto)
        
        endereco = self.buscar_endereco(cliente)

        print(f"Pedido processado para {cliente.nome}. Produto: {produto.nome}. Entrega: {endereco.rua}, {endereco.cidade}.")

if __name__ == "__main__":
    pedidos = Pedidos()
    pedidos.processar_pedido(1, "ABC")
    pedidos.processar_pedido(2, "XYZ")