from abc import ABC, abstractmethod
from datetime import date

class Contato(ABC):
    def __init__(self, nome: str, email: str, telefone: str):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def get_email(self):
        return self.__email
    
    def set_email(self, novo_email):
        self.__email = novo_email

    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
    @abstractmethod
    def obter_informacoes(self):
        raise NotImplementedError(" Método não implementado. ")

class ContatoPessoal(Contato):
    def __init__(self, nome: str, email: str, telefone: str, data_aniversario: date):
        super().__init__(nome, email, telefone)
        self.__data_aniversario = data_aniversario

    def get_aniv(self):
        return self.__data_aniversario
    
    def set_aniv(self, novo_aniv):
        self.__data_aniversario = novo_aniv
    
    def obter_informacoes(self):
        print(f"Nome: {self.__nome}\
                Email: {self.__email}\
                Telefone: {self.__telefone}\
                Data Aniversario: {self.__data_aniversario}")

class ContatoProfissional(Contato):
    def __init__(self, nome: str, email: str, telefone: str, empresa: str, cargo: str):
        super().__init__(nome, email, telefone)
        self.__empresa = empresa
        self.__cargo = cargo

    def get_empresa(self):
        return self.__empresa
    
    def set_empresa(self, nova_empresa):
        self.__empresa = nova_empresa
    
    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self, novo_cargo):
        self.__cargo = novo_cargo

    def obter_informacoes(self):
        print(f"Nome: {self.__nome}\
                Email: {self.__email}\
                Telefone: {self.__telefone}\
                Empresa: {self.__empresa}\
                Cargo: {self.__cargo}")