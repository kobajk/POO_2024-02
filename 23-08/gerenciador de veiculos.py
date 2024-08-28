class Veiculo:
    def __init__(self, marca, modelo, preco_base):
        self.marca = marca
        self.modelo = modelo
        self.preco_base = preco_base
    def calcular_valor_venda(self):
        raise NotImplementedError(" Esse método deve ser implementado nas subclasses")

class Carro(Veiculo):
    def __init__(self, marca, modelo, preco_base, num_portas, ac):
        super().__init__(marca, modelo, preco_base)
        self.num_portas = num_portas
        self.ac = ac
    
    def calcular_valor_venda(self):
        valor_ac = 0
        if self.ac == True:
            valor_ac = 3000
        return self.preco_base + valor_ac

class Moto(Veiculo):
    def __init__(self, marca, modelo, preco_base, cilindradas):
        super().__init__(marca, modelo, preco_base)
        self.cilindradas = cilindradas
    
    def calcular_valor_venda(self):
        if self.cilindradas >= 300:
            return self.preco_base * 1.1
        elif self.cilindradas >= 500:
            return self.preco_base * 1.2
        elif self.cilindradas >= 1000:
            return self.preco_base * 1.4

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, preco_base, capac_carga, eixos):
        super().__init__(marca, modelo, preco_base)
        self.capac_carga = capac_carga
        self.eixos = eixos

    def calcular_valor_venda(self):
        valor_eixos = 0
        valor_carga = 0
        if self.eixos == 2:
            valor_eixos = 5000
        elif self.eixos == 3:
            valor_eixos = 10000
        elif self.eixos == 4:
            valor_eixos = 20000
        if self.capac_carga < 33:
            valor_carga == 10000
        elif self.capac_carga >= 33:
            valor_carga == 20000
        return self.preco_base + valor_carga + valor_eixos

class Concessionaria:
    def __init__(self):
        self.veiculos = []
    
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
    
    def calcular_valor_estoque(self):
        return sum(self.veiculos)

    def exibir_menu(self):
        while True:
            print("Menu Concessionaria"
                "\n1 - Incluir veiculo"
                "\n2 - Calcular valor estoque"
                "\n0 - Sair")
            escolha = int(input())
            if escolha == 1:
                print("Menu Veiculo"
                    "\n1 - Carro"
                    "\n2 - Moto"
                    "\n3 - Caminhao")  
                escolha_veiculo = int(input())
                if escolha_veiculo == 1:
                    veiculo = Carro(str(input("Marca: ")), str(input("Modelo: ")), float(input("Preco_base: ")), int(input("Num_portas: ")), bool(input("AC: ")))
                    self.adicionar_veiculo(veiculo.preco_base)
                elif escolha_veiculo == 2:
                    veiculo = Moto(str(input("Marca: ")), str(input("Modelo: ")), float(input("Preco_base: ")), int(input("Cilindradas: ")))
                    self.adicionar_veiculo(veiculo.preco_base)
                elif escolha_veiculo == 3:
                    veiculo = Caminhao(str(input("Marca: ")), str(input("Modelo: ")), float(input("Preco_base: ")), str(input("Modelo: ")),float(input("Capacidade de Carga (Toneladas): ")), int(input("Eixos: ")))
                    self.adicionar_veiculo(veiculo.preco_base)
                else:
                    print(" Escolha inexistente")
            elif escolha == 2:
                print(f"O valor de estoque é: {self.calcular_valor_estoque()}")
            elif escolha == 0:
                break

Ford = Concessionaria()

Ford.exibir_menu()
