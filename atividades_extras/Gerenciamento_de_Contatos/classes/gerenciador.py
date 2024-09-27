from classes.contato import ContatoPessoal
from classes.contato import ContatoProfissional
import sqlite3

class GerenciadorContatos:
    def __init__(self):
        try:
            self.conn = sqlite3.connect('atividades_extras/Gerenciamento_de_Contatos/banco/banco.bd')
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Erro na conexão com o banco de dados: {e}")
        
        try:
            self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS contatos(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL,
                            telefone VARCHAR(20) NOT NULL,
                            data_aniversario DATE,
                            empresa VARCHAR(255),
                            cargo VARCHAR(255),
                            tipo VARCHAR(255) NOT NULL)
                            ''')
        except sqlite3.Error as e:
            print(f"Falha na criação da tabela contatos: {e}")
    
    def inserir_contato_pessoal(self, contato: ContatoPessoal):
        try:
            self.cursor.execute(f'''
                            INSERT INTO 
                            contatos(nome, email, telefone, data_aniversario, tipo)
                            VALUES('{contato.get_nome()}', '{contato.get_email()}', '{contato.get_telefone()}', {contato.get_aniv()}, "Pessoal")''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Falha ao inserir novo contato pessoal: {e}")

    def inserir_contato_profissional(self, contato: ContatoProfissional):
        try:
            self.cursor.execute(f'''
                            INSERT INTO 
                            contatos(nome, email, telefone, empresa, cargo, tipo)
                            VALUES('{contato.get_nome()}', '{contato.get_email()}', '{contato.get_telefone()}', '{contato.get_empresa()}', '{contato.get_cargo()}', "Profissional")''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Falha ao inserir novo contato pessoal: {e}")
    
    def atualizar_contato_pessoal(self, id, contato: ContatoPessoal):
        try:
            self.cursor.execute(f'''
                UPDATE contatos
                SET 
                nome = '{contato.get_nome()}', 
                email = '{contato.get_email()}', 
                telefone = '{contato.get_telefone()}', 
                data_aniversario = {contato.get_aniv()}
                WHERE id = {id}
                ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Falha ao atualizar contato: {e}")

    def atualizar_contato_profissional(self, id, contato: ContatoProfissional):
        try:
            self.cursor.execute(f'''
                UPDATE contatos
                SET 
                nome = '{contato.get_nome()}', 
                email = '{contato.get_email()}', 
                telefone = '{contato.get_telefone()}', 
                empresa = '{contato.get_empresa()}',
                cargo = '{contato.get_cargo()}'
                WHERE id = {id}
                ''')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Falha ao atualizar contato: {e}")

    def listar_contatos_pessoal(self):
        self.cursor.execute('SELECT * FROM contatos WHERE tipo = "Pessoal"')
        contatos = self.cursor.fetchall()
        return contatos

    def listar_contatos_profissional(self):
        self.cursor.execute('SELECT * FROM contatos WHERE tipo = "Profissional"')
        contatos = self.cursor.fetchall()
        return contatos

    def listar_contatos(self):
        self.cursor.execute('SELECT * FROM contatos')
        contatos = self.cursor.fetchall()
        return contatos
    
    def buscar_contato(self, nome: str):
        self.cursor.execute(f'SELECT * FROM contatos WHERE nome = "{nome}"')
        contatos = self.cursor.fetchall()
        return contatos
    
    def fechar_conexao(self):
        if self.conn:
            try:
                self.conn.close()
            except sqlite3.Error as e:
                print(f" Erro ao fechar conexao: {e}")
        else:
            print(f" Falha na conexão: {e}")