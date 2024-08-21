class Carro:
    def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def mostrar_info(self):
        print(f" A marca do carro é: {self.marca}"
                f"\n O modelo do carro é: {self.modelo}"
                f"\n O ano do carro é: {self.ano}")
        if self.ligado == True:
            print(" O carro está ligado! ")
        else:
            print(" O carro está desligado! ")

carro1 = Carro("Ford","Ka","2020")

carro1.ligar()

carro1.mostrar_info()