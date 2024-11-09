class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

# Simulação de busca de dados
def buscar_cliente(id):
    if id == 1:
        return Cliente("João", "joao@example.com")
    else:
        return None

def buscar_produto(codigo):
    if codigo == "ABC":
        return Produto("Produto A", 100.0)
    else:
        return None

def buscar_endereco(cliente):
    if cliente and cliente.nome == "João":
        return Endereco("Rua Principal", "Cidade Exemplo")
    else:
        return None

# Código que contém múltiplas verificações de None
def processar_pedido(cliente_id, codigo_produto):
    cliente = buscar_cliente(cliente_id)
    if cliente is None:
        print("Erro: Cliente não encontrado.")
        return
    
    produto = buscar_produto(codigo_produto)
    if produto is None:
        print("Erro: Produto não encontrado.")
        return
    
    endereco = buscar_endereco(cliente)
    if endereco is None:
        print("Erro: Endereço de entrega não encontrado.")
        return

    print(f"Pedido processado para {cliente.nome}. Produto: {produto.nome}. Entrega: {endereco.rua}, {endereco.cidade}.")
