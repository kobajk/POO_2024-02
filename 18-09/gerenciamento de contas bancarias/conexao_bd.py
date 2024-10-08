import sqlite3
class ConexaoBD:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('18-09/gerenciamento de contas bancarias/banco.bd')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Erro na conexão com o banco de dados: {e}")

    def criar_tabela(self):
        if self.conn:
            try:
                self.cursor.execute('''
                                    CREATE TABLE IF NOT EXISTS contas
                                    (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    numero_conta INTEGER NOT NULL,
                                    titular TEXT NOT NULL,
                                    saldo REAL NOT NULL,
                                    limite REAL NOT NULL)
                                    ''')
            except sqlite3.Error as e:
                print(f"Erro na criação da tabela contas: {e}")
        
        else:
            print(f" Falha na conexão: {e}")

    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print(f"Erro na criação da tabela contas: {e}")
        else:
            print(f" Falha na conexão: {e}")

#exemplo de uso
#conexao = ConexaoBD()
#conexao.criar_tabela()
#conexao.fechar_conexao() 