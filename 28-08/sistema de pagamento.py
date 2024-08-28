from abc import ABC, abstractmethod

class Pagamentos():
    def __init__(self, quantia, data):
        self.quantia = quantia
        self.data = data
    
    @abstractmethod
    def efetuar_pagamento(self):
        pass

    def detalhes(self):
        print(f"Quantia: {self.quantia} ; Data: {self.data}")

class Dinheiro(Pagamentos):
    def __init__(self, quantia, data, moeda):
        super().__init__(quantia, data)
        self.moeda = moeda

    def efetuar_pagamento(self):
        print(f" Pagamento no valor de {self.quantia}{self.moeda} efetuado em {self.data}")

class CartaoCredito(Pagamentos):
    def __init__(self, quantia, data, num_cartao, validade):
        super().__init__(quantia, data)
        self.num_cartao = num_cartao
        self.validade = validade

    def efetuar_pagamento(self):
        print(f" Pagamento efetuado com o cartao {self.num_cartao} na quantida de {self.quantia} no dia {self.data}")

class Pix(Pagamentos):
    def __init__(self, quantia, data, cod_pix):
        super().__init__(quantia, data)
        self.cod_pix = cod_pix
    
    def efetuar_pagamento(self):
        print(f" Pagamento efetuado via PIX no valor de {self.quantia} para a chave {self.cod_pix}")