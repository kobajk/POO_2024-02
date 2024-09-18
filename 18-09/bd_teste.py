# Importa o módulo sqlite3, que fornece uma interface para bancos de dados SQLite
import sqlite3

# Estabelece uma conexão com o banco de dados chamado "usuarios.db" localizado no diretório "18-09"
conexao = sqlite3.connect("18-09/usuarios.db")

# Cria um cursor, que permite executar comandos SQL no banco de dados
cursor = conexao.cursor()

# Executa um comando SQL para criar uma tabela chamada "user" se ela não existir
# A tabela possui três colunas: id (chave primária autoincrementada), nome (texto não nulo) e cpf (texto não nulo)
cursor.execute('''CREATE TABLE IF NOT EXISTS user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL, 
               cpf TEXT NOT NULL)
                ''')
# Inserir dados na tabela
nome1 = "João"
cpf1 = "012312312012"
cursor.execute('''INSERT INTO USER (nome,cpf) VALUES(?,?)''',(nome1,cpf1))


# Confirma (commita) as mudanças feitas no banco de dados
conexao.commit()

# Update no banco de dados
nome1 = "Pedro"
id1 = 3
cursor.execute('''UPDATE user
               SET nome = ?
               WHERE id = ?''',(nome1,id1))

# Confirma (commita) as mudanças feitas no banco de dados
conexao.commit()

# Select
cursor.execute('''SELECT * FROM user''')

for u in cursor.fetchall():
    print(u)

conexao.close()