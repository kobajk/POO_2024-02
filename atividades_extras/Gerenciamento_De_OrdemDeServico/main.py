from classes.servicos import ServicoInterno
from classes.servicos import ServicoExterno
from classes.conexao_bd import ConexaoBD
from classes.dao_servicos import ServicosDAO

def main():
    conexao = ConexaoBD()
    conexao.criar_tabelas()
    # conexao.inserir_servicos_padroes() só na primeira vez
    DAO = ServicosDAO(conexao)

    #somente executa na primeira vez
    servico1 = ServicoInterno('Manutencao basica','feita a manutencao do carro x', 'vendas', 5.2)
    servico2 = ServicoExterno('Reparo avancado', 'realizado troca do motor', 'Hyundai', 37.6)

    #DAO.inserir_servico_interno(servico1)
    #DAO.inserir_servico_externo(servico2)

    DAO.listar_servicos_internos()
    DAO.listar_servicos_externos()

    DAO.buscar_custo_hora_servico('Diagnostico')

    print(f'O orçamento do Servico1 é: {servico1.retorna_orcamento()}R$')
    print(f'O orçamento do Servico2 é: {servico2.retorna_orcamento()}R$')

    conexao.fechar_conexao()
if __name__ == "__main__":
    main()
