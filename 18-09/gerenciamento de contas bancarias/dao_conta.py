# data access object
class ContaBancariaDAO:
    def __init__(self, conexao):
        self.conn = conexao.conn
        self.cursor = conexao.cursor
    def salvar_conta(self, conta):
        self.cursor.execute('''
                            INSERT INTO
                            contas (numero_conta, titular, saldo, limite)
                            VALUES
                            (?,?,?,?)''', (conta.numero_conta, conta.titular, conta.get_saldo(), conta.get_limite()))
        self.conn.commit()
    def listar_contas(self):
        self.cursor.execute('''SELECT * FROM contas''')
        contas = self.cursor.fetchall()
        return contas
    
        