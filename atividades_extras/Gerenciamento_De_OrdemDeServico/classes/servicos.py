from abc import ABC, abstractmethod
from classes.conexao_bd import ConexaoBD

class Servico(ABC):
    def __init__(self, tipo_servico, descricao):
        self._tipo_servico = tipo_servico
        self._descricao = descricao
    
    @abstractmethod
    def retorna_orcamento(self):
        raise NotImplementedError(" Método precisa ser implementado nas subclasses! ")
    
class ServicoInterno(Servico):
    def __init__(self, tipo_servico, descricao, setor, horas):
        super().__init__(tipo_servico, descricao)
        self._setor = setor
        self._horas = horas
    
    def retorna_orcamento(self):
        conexao = ConexaoBD()
        conexao.cursor.execute(f'SELECT valor_hora FROM precoservicos WHERE tipo_servico = "{self._tipo_servico}"')
        preco = float(conexao.cursor.fetchone()[0])
        return preco * 0.5
    
class ServicoExterno(Servico):
    def __init__(self, tipo_servico, descricao, cliente, horas):
        super().__init__(tipo_servico, descricao)
        self._cliente = cliente
        self._horas = horas
    
    def retorna_orcamento(self):
        conexao = ConexaoBD()
        conexao.cursor.execute(f'SELECT valor_hora FROM precoservicos WHERE tipo_servico = "{self._tipo_servico}"')
        preco = float(conexao.cursor.fetchone()[0])
        return preco