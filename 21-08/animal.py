# declaração da classe
class Animal:
    #método construtor da classe executado sempre que um objeto é criado
    def __init__(self,nome,tipo,som):
        self.nome = nome
        self.tipo = tipo
        self.som = som
    
    def setSom(self,som):
        self.som = som

    def fazerSom(self):
        print(f"O {self.nome} {self.som}")

    def alimentar(self):
        print(" Animal alimentado")

    def dormir(self):
        print(" Animal à dormir")
    
    def mostrarInfo(self):
        print(f" O nome do animal é: {self.nome}"
                f"\n O tipo do animal é: {self.tipo}"
                f"\n O som do animal é: {self.som}")


animal1 = Animal("Chico-Chiquinho","gato","mia")
animal2 = Animal("Dexter","cachorro","late")

animal1.setSom("latir")
animal1.fazerSom()

animal2.alimentar()
animal2.dormir()
animal2.mostrarInfo()

