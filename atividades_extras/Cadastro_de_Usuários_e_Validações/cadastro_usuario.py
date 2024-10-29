import re

class CadastroUsuario:
    def __init__(self, nome, cpf, nascimento, endereco, telefone, senha):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.senha = senha

    def validar_nome(self):
        if len(self.nome.split()) >= 2:
            return True
        raise ValueError("Nome deve conter pelo menos duas palavras.")

    def validar_cpf(self):
        if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', self.cpf):
            return True
        raise ValueError("CPF inválido. Deve estar no formato XXX.XXX.XXX-XX.")

    def validar_nascimento(self):
        if re.match(r'\d{2}/\d{2}/\d{4}', self.nascimento):
            return True
        raise ValueError("Data de nascimento inválida. Deve estar no formato DD/MM/AAAA.")

    def validar_endereco(self):
        if self.endereco.strip():
            return True
        raise ValueError("Endereço não pode estar vazio.")

    def validar_telefone(self):
        if re.match(r'\(\d{2}\) \d{4,5}-\d{4}', self.telefone):
            return True
        raise ValueError("Telefone inválido. Formatos aceitos: (XX) XXXX-XXXX ou (XX) XXXXX-XXXX.")

    def validar_senha(self):
        if len(self.senha) >= 8 and any(c.isdigit() for c in self.senha) and any(c.isalpha() for c in self.senha):
            return True
        raise ValueError("Senha inválida. Deve conter pelo menos 8 caracteres, incluindo letras e números.")

    def mostrar_info(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nNascimento: {self.nascimento}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")

    def gravar_info(self):
        if all([
            self.validar_nome(),
            self.validar_cpf(),
            self.validar_nascimento(),
            self.validar_endereco(),
            self.validar_telefone(),
            self.validar_senha()
        ]):
            with open(f"cadastro_{self.cpf}.txt", 'w') as file:
                file.write(f"Nome: {self.nome}\nCPF: {self.cpf}\nNascimento: {self.nascimento}\nEndereço: {self.endereco}\nTelefone: {self.telefone}")
            print("Informações gravadas com sucesso.")
        else:
            raise ValueError("Erro na validação dos dados.")
