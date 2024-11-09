class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email(self, mensagem):
        print(f"Enviando email para {self.email}: {mensagem}")

# Simulação de um sistema de busca de clientes
def buscar_cliente(id):
    # Simula a busca de um cliente no banco de dados
    if id == 1:
        return Cliente("João", "joao@example.com")
    else:
        return None

# Lógica que contém verificações de `null`
def notificar_cliente(id, mensagem):
    cliente = buscar_cliente(id)
    if cliente is None:
        print("Nenhum cliente encontrado.")
    else:
        cliente.enviar_email(mensagem)

# Testes
notificar_cliente(1, "Bem-vindo ao sistema!")  # Deve enviar email
notificar_cliente(2, "Bem-vindo ao sistema!")  # Deve imprimir "Nenhum cliente encontrado."
