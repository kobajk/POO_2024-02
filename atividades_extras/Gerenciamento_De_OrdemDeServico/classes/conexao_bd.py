import sqlite3
class ConexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('atividades_extras/Gerenciamento_De_OrdemDeServico/banco/banco.bd')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Erro na conexão com o banco de dados: {e}")

    def criar_tabelas(self):
        if self.conn:
            try: # CRIAR TABELA PRECOSERVICOS
                self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS precoservicos
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    tipo_servico VARCHAR(255) NOT NULL,
                                    valor_hora FLOAT NOT NULL)
                                    ''')
            except sqlite3.Error as e:
                print(f"Erro na criação da tabela Preco Servicos: {e}")

            try: # CRIAR TABELA SERVICOSINTERNOS
                self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS servicosinternos
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    tipo_servico VARCHAR(255) NOT NULL,
                                    descricao TEXT NOT NULL,
                                    setor VARCHAR(255) NOT NULL,
                                    horas FLOAT NOT NULL)
                                    ''')
            except sqlite3.Error as e:
                print(f"Erro na criação da tabela Servicos Internos: {e}")

            try: # CRIAR TABELA SERVICOSEXTERNOS
                self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS servicosexternos
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    tipo_servico VARCHAR(255) NOT NULL,
                                    descricao TEXT NOT NULL,
                                    cliente VARCHAR(255) NOT NULL,
                                    horas FLOAT NOT NULL)
                                    ''')
            except sqlite3.Error as e:
                print(f"Erro na criação da tabela Servicos Externos: {e}")
        
        else:
            print(f" Falha na conexão: {e}")

    def inserir_servicos_padroes(self):
        try:
            servicos = ['Manutencao basica', 'Reparo avancado', 'Diagnostico', 'Troca de pecas', 'Limpeza']
            valor_hora = [50.0, 75.0, 60.0, 80.0, 40.0]
            for i in range(len(servicos)):
                self.cursor.execute(f'''
                                    INSERT INTO
                                    precoservicos(tipo_servico, valor_hora)
                                    VALUES('{servicos[i]}', '{valor_hora[i]}')''')
        except sqlite3.Error as e:
            print(f"Erro ao adicionar servicos padroes: {e}")

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print(f"Erro no fechamento da conexão: {e}")
        else:
            print(f" Falha na conexão: {e}")