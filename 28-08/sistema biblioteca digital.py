from abc import ABC, abstractmethod

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao

    @abstractmethod
    def get_informacoes(self):
        pass

class Livro(MaterialBiblioteca):
    def __init__(self, titulo, autor, anoPublicacao, num_paginas):
        super().__init__(titulo, autor, anoPublicacao)
        self.num_paginas = num_paginas
    
    def get_informacoes(self):
        print(f" Titulo: {self.titulo}; Ano de publicacao: {self.anoPublicacao}; Numeros de paginas: {self.num_paginas}")

class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, anoPublicacao, edicao):
        super().__init__(titulo, autor, anoPublicacao)
        self.edicao = edicao

    def get_informacoes(self):
        print(f" Titulo: {self.titulo}; Ano de publicacao: {self.anoPublicacao}; Numeros de paginas: {self.edicao}")

class Ebook(MaterialBiblioteca):
    def __init__(self, titulo, autor, anoPublicacao, tam_arq):
        super().__init__(titulo, autor, anoPublicacao)
        self.tam_arq = tam_arq

    def get_informacoes(self):
        print(f" Titulo: {self.titulo}; Ano de publicacao: {self.anoPublicacao}; Tamanho do arquivo: {self.tam_arq}")

class Audiolivro(MaterialBiblioteca):
    def __init__(self, titulo, autor, anoPublicacao, narrador):
        super().__init__(titulo, autor, anoPublicacao)
        self.narrador = narrador

    def get_informacoes(self):
        print(f" Titulo: {self.titulo}; Ano de publicacao: {self.anoPublicacao}; Narrador: {self.narrador}")


class Biblioteca:
    def __init__(self):
        self.acervo = []
    
    def adicionar_material(self):
        pass

    def remover_material(self):
        pass

    def exibir_informacoes_material(self):
        pass
