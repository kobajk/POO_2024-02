'''
Objetivo: Desenvolver um sistema para gerenciar uma empresa com diferentes tipos de funcionários,incluindo salários, cargos e bonificações.
Parte 1: Definir Classes
1. Classe Funcionário:
- Atributos: nome, ID, salário.
- Métodos: mostrar_detalhes, calcular_bonificacao.
2. Classe Gerente (herda de Funcionário):
3. Classe Engenheiro (herda de Funcionário):
- Atributo adicionais: especialidade (por exemplo, software, hardware).
- Método mostrar_detalhes (sobrescrito)
'''

class Funcionario:
    def __init__(self,nome,ID,salario):
        self.nome = nome
        self.ID = ID
        self.salario = salario
    def mostrar_detalhes(self):
        print(f"Nome: {self.nome}"
              f"\nID: {self.ID}"
              f"\nSalário: {self.salario}")
    def calcular_bonificacao(self):
        return self.salario * 12 * 0.6
    def get_nome(self):
        return self.nome

class Gerente(Funcionario):
    def __init__(self, nome, ID, salario):
        super().__init__(nome,ID,salario)       
    def calcular_bonificacao(self):
        return self.salario * 12 * 0.8
    
class Engenheiro(Funcionario):
    def __init__(self, nome, ID, salario, especialidade):
        self.especialidade = especialidade
        super().__init__(nome,ID,salario)
    def mostrar_detalhes(self):
        print(f"Nome: {self.nome}"
              f"\nID: {self.ID}"
              f"\nSalário: {self.salario}"
              f"\nEspecialidade: {self.especialidade}")
        

funcionario1 = Funcionario("Caue",0,1000.00)
funcionario2 = Funcionario("Bruno",1,1375.00)
gerente = Gerente("Alex",2,30000.00)
engenheiro = Engenheiro("Sr. Bruno",3,50000.00,"Eng.Software")

print(f"O {funcionario1.get_nome()} ganha {funcionario1.calcular_bonificacao()} de PLR")
print(f"O {funcionario2.get_nome()} ganha {funcionario2.calcular_bonificacao()} de PLR")
print(f"O {gerente.get_nome()} ganha {gerente.calcular_bonificacao()} de PLR")
print(f"O {engenheiro.get_nome()} ganha {engenheiro.calcular_bonificacao()} de PLR")
print(engenheiro.mostrar_detalhes())

    