from conexao_bd import ConexaoBD
from conta_bancaria import ContaBancaria
from dao_conta import ContaBancariaDAO

if __name__ == "__main__":
    conexao = ConexaoBD()
    conexao.criar_tabela()
    conta1 = ContaBancaria(10001, "Caue Kenzo", -3000, 3000)
    conta2 = ContaBancaria(10002, "Alex Lopes", 1000000, 5000000)
    conta3 = ContaBancaria(10003, "Ruy Quentin", -3000, 0)

    conta1.exibir_info()
    conta1.depositar(3000)
    conta1.exibir_info()
    conta1.sacar(3000)
    conta1.exibir_info()
    conta1.sacar(200)

    conta_dao = ContaBancariaDAO(conexao)
    conta_dao.salvar_conta(conta1)
    conta_dao.salvar_conta(conta2)
    conta_dao.salvar_conta(conta3)

    print(conta_dao.listar_contas())

    conexao.fechar_conexao()

    