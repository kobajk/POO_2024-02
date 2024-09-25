from abc import ABC, abstractmethod
from datetime import datetime

class Veiculos(ABC):
    qtd_veiculos = 0  # atributo de classe
    def __init__(self, modelo, ano, valor):
        if Veiculos.validar_ano(ano):
            self.modelo = modelo
            self.ano = ano
            self.valor = valor
            Veiculos.qtd_veiculos += 1
        else:
            raise ValueError(" Veículo não pode ser cadastrado! Fora do periodo de anos que aceitamos. ")
    
    @abstractmethod
    def calcular_seguro(self):
        raise NotImplementedError(" Subclasses necessitam implementar esse metodo")
    
    @staticmethod
    def validar_ano(ano):
        ano_atual = datetime.now().year
        return 1900 <= ano <= ano_atual + 1
    
    @classmethod
    def total_veiculos(cls):
        return cls.qtd_veiculos
    
class Carro(Veiculos):   
    def calcular_seguro(self):
        ano_atual = datetime.now().year
        if self.ano >= ano_atual: #  Se o ano do carro estiver entre os ultimos 5 anos o preço é 15% do valor
            valor_seguro = self.valor * 0.2
        else:
            valor_seguro = self.valor * 0.1
        return valor_seguro
    
class Caminhao(Veiculos):
    def calcular_seguro(self):
        ano_atual = datetime.now().year
        if self.ano >= ano_atual - 5: #  Se o ano do caminhao estiver entre os ultimos 5 anos o preço é 25% do preço
            valor_seguro = self.valor * 0.25
        else:
            valor_seguro = self.valor * 0.15
        return valor_seguro

class Moto(Veiculos):
    def calcular_seguro(self):
        ano_atual = datetime.now().year
        if self.ano >= ano_atual-5: #  Se o ano da moto estiver entre os ultimos 5 anos o preço é 10% do preço 
            valor_seguro = self.valor * 0.1
        else:
            valor_seguro = self.valor * 0.05
        return valor_seguro

    
def main():
    carro1 = Carro("Mustang",1980,150000)
    carro2 = Carro("Ka",2024,80000)
    caminhao1 = Caminhao("Truck",1980,70000)
    caminhao2 = Caminhao("Xiaomi",2024,15000)
    moto1 = Moto("Shineray",2025,50000)
    moto2 = Carro("CB500",2023,30000)

    print(f" O preço do seguro para o {carro1.modelo} do ano {carro1.ano} é de: {carro1.calcular_seguro():.2f} R$")
    print(f" O preço do seguro para o {carro2.modelo} do ano {carro2.ano} é de: {carro2.calcular_seguro():.2f} R$")
    print(f" O preço do seguro para o {caminhao1.modelo} do ano {caminhao1.ano} é de: {caminhao1.calcular_seguro():.2f} R$")
    print(f" O preço do seguro para o {caminhao2.modelo} do ano {caminhao2.ano} é de: {caminhao2.calcular_seguro():.2f} R$")
    print(f" O preço do seguro para o {moto1.modelo} do ano {moto1.ano} é de: {moto1.calcular_seguro():.2f} R$")
    print(f" O preço do seguro para o {moto2.modelo} do ano {moto2.ano} é de: {moto2.calcular_seguro():.2f} R$")

if __name__ == "__main__":
    main()