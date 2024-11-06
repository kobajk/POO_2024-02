# padrao de projeto Strategy
from abc import ABC, abstractmethod
class EstrategiaCalculoTarifa(ABC):
    @abstractmethod
    def calcular_tarifa(self, valor_transacao):
        pass

class TarifaPadraoStrategy(EstrategiaCalculoTarifa):
    def __init__(self, taxa):
        self.taxa = taxa

    def calcular_tarifa(self, valor_transacao):
        return valor_transacao *  self.taxa

class TarifaVipStrategy(EstrategiaCalculoTarifa):
    def __init__(self, tarifa_fixa):
        self.tarifa_fixa = tarifa_fixa

    def calcular_tarifa(self, valor_transacao):
        return self.tarifa_fixa

class TarifaEspecialStrategy(EstrategiaCalculoTarifa):
    def __init__(self, tarifa_especial):
        self.tarifa_especial = tarifa_especial

    def calcular_tarifa(self, valor_transacao):
        return valor_transacao * self.tarifa_especial

class Pagamento:
    def __init__(self, estrategia: EstrategiaCalculoTarifa):
        self.estrategia = estrategia

    def processar_pagamento(self, valor):
        return self.estrategia.calcular_tarifa(valor) + valor

if __name__ == "__main__":
    estrategia_padrao = TarifaPadraoStrategy(0.02)
    estrategia_vip = TarifaVipStrategy(5.0)
    estrategia_especial = TarifaEspecialStrategy(0.01)

    valor_transacao = 100000.00

    pagamento = Pagamento(estrategia_padrao)
    pagamento.processar_pagamento(valor_transacao)
    
