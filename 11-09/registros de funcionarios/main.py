class Funcionario:
    def __init__(self, nome, cargo):
        self.__nome = nome
        self.__cargo = cargo
    def setNome(self, novo_nome):
        self.__nome = novo_nome
    def getNome(self):
        return self.__nome
    def setCargo(self, novo_cargo):
        self.__cargo = novo_cargo
    def getCargo(self):
        return self.__cargo

class GerenciarFuncionarios:
    def __init__(self):
        try:
            with open("11-09/registros de funcionarios/funcionarios.txt", "w", encoding="utf-8") as f:
                f.write("")
        except FileNotFoundError as e:
            print(f" Ocorreu um erro {e}")
    def incluirFuncionario(self, nome, cargo):
        novoFuncionario = Funcionario(nome,cargo)
        try:        
            with open("11-09/registros de funcionarios/funcionarios.txt", "a", encoding="utf-8") as f:
                f.write(f"Nome:{novoFuncionario.getNome()}, Cargo: {novoFuncionario.getCargo()}\n")
        except FileNotFoundError as e:
            print(f" Ocorreu um erro {e}")
    def mostrarFuncionarios(self):
        with open("11-09/registros de funcionarios/funcionarios.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()
            print(conteudo)

Gerenciamento = GerenciarFuncionarios()

Gerenciamento.incluirFuncionario("Bruno","Engenheiro")
Gerenciamento.incluirFuncionario("Caue","Desempregado")
Gerenciamento.incluirFuncionario("Leonardo","Milionario")
Gerenciamento.incluirFuncionario("Nilton","Professor")

Gerenciamento.mostrarFuncionarios()