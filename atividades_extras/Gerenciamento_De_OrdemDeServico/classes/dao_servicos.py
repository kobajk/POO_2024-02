from classes.servicos import ServicoInterno
from classes.servicos import ServicoExterno
import sqlite3
# data access object
class ServicosDAO:
    def __init__(self, conexao):
        self.conn = conexao.conn
        self.cursor = conexao.cursor
        
    def inserir_servico_interno(self, servico: ServicoInterno):
        try:
            self.cursor.execute(f'''
                            INSERT INTO 
                            servicosinternos(tipo_servico, descricao, setor, horas)
                            VALUES('{servico._tipo_servico}', '{servico._descricao}', '{servico._setor}', {servico._horas})''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Falha ao inserir novo servico: {e}")

    def inserir_servico_externo(self, servico: ServicoExterno):
        try:
            self.cursor.execute(f'''
                            INSERT INTO 
                            servicosexternos(tipo_servico, descricao, cliente, horas)
                            VALUES('{servico._tipo_servico}', '{servico._descricao}', '{servico._cliente}', {servico._horas})''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Falha ao inserir novo servico: {e}")

    def listar_servicos_internos(self):
        self.cursor.execute('SELECT * FROM servicosinternos')
        servicos = self.cursor.fetchall()
        for servico in servicos:
            print(servico)

    def listar_servicos_externos(self):
        self.cursor.execute('SELECT * FROM servicosexternos')
        servicos = self.cursor.fetchall()
        for servico in servicos:
            print(servico)

    def buscar_custo_hora_servico(self, tipo_servico: str):
        self.cursor.execute(f'SELECT valor_hora FROM precoservicos WHERE tipo_servico = "{tipo_servico}"')
        preco = self.cursor.fetchone()
        return preco
