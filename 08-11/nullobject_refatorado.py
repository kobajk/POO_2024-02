from abc import ABC, abstractmethod
class AbstractCliente(ABC):
    @abstractmethod
    def enviar_email(self, mensagem):
        pass

class Cliente(AbstractCliente):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email(self, mensagem):
        print(f"Enviando email para {self.email}: {mensagem}")

class ClienteNull(AbstractCliente):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email(self, mensagem):
        print(f"{self.email}")    

class ClienteFactory:
    def buscar_cliente(self, id):
        # Simula a busca de um cliente no banco de dados
        if id == 1:
            return Cliente("João", "joao@example.com")
        else:
            return ClienteNull("Cliente não encontrado", None)


if __name__ == '__main__':
    factory = ClienteFactory()
    cliente1 = factory.buscar_cliente(1)
    cliente2 = factory.buscar_cliente(2)
    cliente1.enviar_email("Bem-vindo")
    cliente2.enviar_email("Bem-vindo")

