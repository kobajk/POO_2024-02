import pickle as pkl
## faça um com comentario a cada classe e metodo explicando resumidamente o que ele faz

class Cliente: ## Classe Cliente que possui os atributos nome e email

    def __init__(self, nome, email): ## Metodo construtor que inicializa os atributos nome e email
        self.__nome = nome
        self.__email = email

    def getNome(self): ## Metodo que retorna o nome do cliente
        return self.__nome
    
    def setNome(self, novo_nome): ## Metodo que altera o nome do cliente
        self.__nome = novo_nome

    def getEmail(self): ## Metodo que retorna o email do cliente
        return self.__email
    
    def setEmail(self, novo_email): ## Metodo que altera o email do cliente
        self.__email = novo_email

class PessoaFisica(Cliente): ## Classe PessoaFisica que herda da classe Cliente

    def __init__(self, nome, email, cpf): ## Metodo construtor que inicializa os atributos nome, email e cpf
        super().__init__(nome,email) ## Chama o construtor da classe Cliente
        self.__cpf = cpf

    def getCpf(self): ## Metodo que retorna o cpf do cliente
        return self.__cpf
    
    def setCpf(self, novo_cpf): ## Metodo que altera o cpf do cliente
        self.__cpf = novo_cpf

class PessoaJuridica(Cliente): ## Classe PessoaJuridica que herda da classe Cliente

    def __init__(self, nome, email, cnpj): ## Metodo construtor que inicializa os atributos nome, email e cnpj
        super().__init__(nome,email) ## Chama o construtor da classe Cliente
        self.__cnpj = cnpj

    def getCnpj(self): ## Metodo que retorna o cnpj do cliente
        return self.__cnpj
    
    def setCnpj(self, novo_cnpj): ## Metodo que altera o cnpj do cliente
        self.__cnpj = novo_cnpj

class GerenciadorDeClientes: ## Classe GerenciadorDeClientes que gerencia os clientes

    def __init__(self): ## Metodo construtor que inicializa as listas de clientes
        try:
            with open("13-09/gerenciamento de registros de clientes/save_pessoa_fisica.pkl", "rb") as f:
                self.pessoa_fisica = pkl.load(f)
        except FileNotFoundError as e: ## Caso o arquivo não exista, a lista é inicializada vazia
            self.pessoa_fisica = []

        try:
            with open("13-09/gerenciamento de registros de clientes/save_pessoa_juridica.pkl", "rb") as f:
                self.pessoa_juridica = pkl.load(f)
        except FileNotFoundError as e: ## Caso o arquivo não exista, a lista é inicializada vazia
            self.pessoa_juridica = []

    def adicionar_cliente_pf(self, nome, email, cpf): ## Metodo que adiciona um cliente de pessoa fisica
        novo_cliente = PessoaFisica(nome, email, cpf)
        self.pessoa_fisica.append(novo_cliente)

    def adicionar_cliente_pj(self, nome, email, cnpj): ## Metodo que adiciona um cliente de pessoa juridica
        novo_cliente = PessoaJuridica(nome, email, cnpj)
        self.pessoa_juridica.append(novo_cliente)

    def listar_clientes(self):
        for pessoa in self.pessoa_fisica: ## Imprime todos os cliente de pessoa fisica
            print(f"Nome: {pessoa.getNome()}\n\
                    E-mail: {pessoa.getEmail()}\n\
                    CPF: {pessoa.getCpf()} ")
        for pessoa in self.pessoa_juridica: ## Imprime todos os cliente de pessoa juridica
            print(f"Nome: {pessoa.getNome()}\n\
                    E-mail: {pessoa.getEmail()}\n\
                    CNPJ: {pessoa.getCnpj()} ")
            
    def buscar_cliente_pf(self):
        i = 0
        for pessoa in self.pessoa_fisica: ## Imprime todos os clientes com seus respectivos indices
            print(f"ID: {i}\n\
                    Nome: {pessoa.getNome()}\n\
                    E-mail: {pessoa.getEmail()}\n\
                    CPF: {pessoa.getCpf()} ")
            i += 1

    def buscar_cliente_pj(self):
        i = 0
        for pessoa in self.pessoa_juridica: ## Imprime todos os cliente de pessoa juridica com seus respectivos indices
            print(f"ID: {i}\n\
                    Nome: {pessoa.getNome()}\n\
                    E-mail: {pessoa.getEmail()}\n\
                    CNPJ: {pessoa.getCnpj()} ")
            i += 1

    def excluir_cliente_pf(self, indice): ## Metodo que exclui um cliente de pessoa fisica
        pessoa = self.pessoa_fisica.pop(indice)
        print(f" Pessoa Fisica: {pessoa.getNome()} do Indice{indice} excluída com sucesso!")

    def excluir_cliente_pj(self, indice): ## Metodo que exclui um cliente de pessoa juridica
        pessoa = self.pessoa_juridica.pop(indice)
        print(f" Pessoa Juridica: {pessoa.getNome()} do Indice{indice} excluída com sucesso!")

    def salvar_dados(self): ## Metodo que salva os dados dos clientes em arquivos
        with open("13-09/gerenciamento de registros de clientes/save_pessoa_fisica.pkl", "wb") as f:
            pkl.dump(self.pessoa_fisica,f)
        with open("13-09/gerenciamento de registros de clientes/save_pessoa_juridica.pkl", "wb") as f:
            pkl.dump(self.pessoa_juridica,f)

def exibir_menu(): ## Metodo que exibe o menu de opções
    print(" --GERENCIADOR DE REGISTROS DE CLIENTES--\n\
            1. Adicionar Cliente (Pessoa Física)\n\
            2. Adicionar Cliente (Pessoa Jurídica)\n\
            3. Listar Clientes\n\
            4. Buscar Cliente (Pessoa Física por ID)\n\
            5. Buscar Cliente (Pessoa Jurídica por ID)\n\
            6. Excluir Cliente (Pessoa Física por ID)\n\
            7. Excluir Cliente (Pessoa Jurídica por ID)\n\
            8. Sair e Salvar")
    
def main(): ## Funcao principal
    Gerenciador = GerenciadorDeClientes()

    while True:
        exibir_menu()
        escolha = int(input())  ## Recebe a opção escolhida pelo usuario
        if escolha == 1:
            nome = str(input(" Informe o nome da pessoa: "))
            email = str(input(" Informe o email da pessoa: "))
            cpf = str(input(" Informe o cpf da pessoa: "))
            Gerenciador.adicionar_cliente_pf(nome,email,cpf)

        elif escolha == 2:
            nome = str(input(" Informe o nome da pessoa: "))
            email = str(input(" Informe o email da pessoa: "))
            cnpj = str(input(" Informe o cnpj da pessoa: "))
            Gerenciador.adicionar_cliente_pj(nome,email,cnpj)

        elif escolha == 3:
            Gerenciador.listar_clientes()

        elif escolha == 4:
            Gerenciador.buscar_cliente_pf()

        elif escolha == 5:
            Gerenciador.buscar_cliente_pj()
            
        elif escolha == 6:
            indice = int(input(" Informe o ID do cliente que deseja excluir: "))
            Gerenciador.excluir_cliente_pf(indice)

        elif escolha == 7:
            indice = int(input(" Informe o ID do cliente que deseja excluir: "))
            Gerenciador.excluir_cliente_pj(indice)

        elif escolha == 8:
            Gerenciador.salvar_dados()
            break
if __name__ == "__main__":
    main()

## O programa é um gerenciador de registros de clientes que permite adicionar, listar, buscar e excluir clientes de pessoa fisica e juridica