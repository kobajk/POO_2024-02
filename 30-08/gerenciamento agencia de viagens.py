'''
Sistema de Gerenciamento de Viagens
Objetivo: Desenvolver um sistema para gerenciar viagens utilizando herança,
polimorfismo, classes abstratas e métodos abstratos.
Descrição:
Você está desenvolvendo um sistema para uma agência de viagens que oferece
diferentes tipos de viagens, como pacotes de cruzeiros, pacotes terrestres, e pacotes
aéreos. Cada tipo de viagem possui características distintas, mas há atributos e
métodos que são comuns a todas as viagens.
Requisitos:
1. Crie uma classe abstrata Viagem, que terá os atributos comuns como destino,
duracao, e precoBase, e um método abstrato calcular_preco_total() para calcular
o custo total da viagem.
2. Crie subclasses Cruzeiro, ViagemTerrestre, e ViagemAerea, cada uma
implementando o método calcular_preco_total() de acordo com suas regras
específicas (por exemplo, taxas de serviço para cruzeiros ou passagens adicionais
para viagens aéreas).
3. Utilize polimorfismo para calcular o preço total das viagens de maneira dinâmica,
dependendo do tipo de viagem.
4. Crie uma classe AgenciaViagens, que será responsável por gerenciar as viagens e
calcular o custo total das viagens vendidas.
Exemplo de funcionalidades:
• adicionar_viagem(): adiciona uma nova viagem ao sistema.
• calcular_receita_total(): calcula o valor total de todas as viagens vendidas.
• exibir_detalhes_viagem(): exibe os detalhes completos de uma viagem
específica.
'''

from abc import ABC, abstractmethod

class Viagem(ABC):
    def __init__(self, destino, duracao, precoBase):
        self.destino = destino
        self.duracao = duracao
        self.precoBase = precoBase

    @abstractmethod
    def calcular_preco_total(self):
        pass

class Cruzeiro(Viagem):
    def __init__(self, destino, duracao, precoBase, taxaServico):
        super().__init__(destino, duracao, precoBase)
        self.taxaServico = taxaServico

    def calcular_preco_total(self):
        return self.precoBase + self.taxaServico

class ViagemTerrestre(Viagem):
    def __init__(self, destino, duracao, precoBase, guia):
        super().__init__(destino, duracao, precoBase)
        self.guia = guia

    def calcular_preco_total(self):
        preco = 0
        if self.guia:
            preco = 1000
        return self.precoBase + preco
    
class ViagemAerea(Viagem):
    def __init__(self, destino, duracao, precoBase, classe):
        super().__init__(destino, duracao, precoBase)
        self.classe = classe
        if self.classe == 0:
            print(" Voce escolheu a classe economica")
        elif self.classe == 1:
            print(" Voce escolheu a classe executiva")
        elif self.classe == 2:
            print(" Voce escolheu a classe primeira classe")

    def calcular_preco_total(self):
        if self.classe == 0:
            preco = 0
        elif self.classe == 1:
            preco = 500
        elif self.classe == 2:
            preco = 1000
        return self.precoBase + preco
    
class AgenciaViagens:
    def __init__(self):
        self.viagens = []
        self.viagens_preco = []
    
    def adicionar_viagem(self, viagem):
        self.viagens.append(viagem)
        self.viagens_preco.append(viagem.calcular_preco_total())

    def calcular_receita_total(self):
