import re
from datetime import datetime

class CadastroUsuario:
    def __init__(self, nome: str, cpf: str, nascimento: str, endereco: str, telefone: str, senha: str):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha
    
    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Nascimento: {self.nascimento}")
        print(f"Endereço: {self.endereco}")
        print(f"Telefone: {self.telefone}")
    
    def gravar_info(self):
        try:
            with open(f"16-10/Cadastro de Usuários e Validações/cadastro_{self.cpf}.txt`", "w", encoding="utf-8") as f:
                f.write("Nome: {self.nome} \n CPF: {self.cpf} \n Nascimento: {self.nascimento} \n Endereço: {self.endereco} \n Telefone: {self.telefone}")
        except FileNotFoundError as e:
            print(f" Ocorreu um erro {e}")

    def validar_nome(self):
        nome = map(str, self.nome.split())
        if len(nome) > 1:
            if all(nomes.isalpha() for nomes in nome):
                return True
        else:
            return False
        
    def validar_cpf(self):
        cpf_regex = r'^(?!.*(\d)(?:.*\1){10})\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if re.match(cpf_regex, self.cpf) is not None:
            return True
        else:
            return False
    
    def validar_nascimento(self):
        data_regex = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if re.match(data_regex, self.nascimento) is not None and (self.nascimento <= datetime.now()):
            return True
        else:
            return False

    def validar_telefone(self):
        numero_regex = r'^\(?\d{2}\)?\s?9\d{4}-?\d{4}$'
        if re.match(numero_regex, self.telefone) is not None:
            return True
        else:
            return False
        
    def validar_senha(self):
        if bool(re.search(r'\d', self.senha)) and bool(re.search(r'\D', self.senha)) and len(self.senha) >= 8:
            return True
        else:
            return False
