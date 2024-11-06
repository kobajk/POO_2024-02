from abc import ABC, abstractmethod

class FormaPagamentoStrategy(ABC):
    @abstractmethod
    def processar_pagamento(self, valor_pedido):
        pass

class CartaoCreditoStrategy(FormaPagamentoStrategy):
    def __init__(self, taxa):
       self.taxa = taxa

    def processar_pagamento(self, valor_pedido):
      return f'Pagamento de Cartão de Crédito {valor_pedido * (1 + self.taxa)}, considerando tarifas, processado!'

class PayPalStrategy(FormaPagamentoStrategy):
    def __init__(self, taxa):
       self.taxa = taxa

    def processar_pagamento(self, valor_pedido):
      return f'Pagamento via PayPal com valor total {valor_pedido * (1 + self.taxa)}, considerando tarifas, processado!'

class TransferenciaBancariaStrategy(FormaPagamentoStrategy):
    def __init__(self, taxa_fixa):
       self.taxa = taxa_fixa

    def processar_pagamento(self, valor_pedido):
      return f'Pagamento via Transferência Bancária {valor_pedido + 1.05}, considerando tarifas, processado!'

if __name__ == "__main__":
    valor_transacao = 100000.00
    pagamento_cartao = CartaoCreditoStrategy(0.01)
    pagamento_paypal = PayPalStrategy(0.05)
    pagamento_transferencia = TransferenciaBancariaStrategy(5.00)

    print(pagamento_cartao.processar_pagamento(valor_transacao))
    print(pagamento_paypal.processar_pagamento(valor_transacao))
    print(pagamento_transferencia.processar_pagamento(valor_transacao))
