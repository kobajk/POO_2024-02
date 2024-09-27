from classes.contato import ContatoPessoal
from classes.contato import ContatoProfissional
from classes.gerenciador import GerenciadorContatos

def main():
    Bruno_Prof = ContatoProfissional("Bruno Oliveira", "bruno@yoso.cloud", "5554991745438", "YOSO", "Co-Founder")
    Caue_Pess = ContatoPessoal("Caue Kenzo", "cauekenzo7@gmail.com", "551198411321", "22/06/2001")
    Leo_Prof = ContatoProfissional("Leonardo", "leonardo@gmail.com", "551131253513", "INTER", "Estagiario Senior")
    Gabriel_Pess = ContatoPessoal("Gabriel", "gabriel@gmail.com", "551193213510", "30/01/2002")

    Gerenciador = GerenciadorContatos()

    Gerenciador.inserir_contato_pessoal(Caue_Pess)
    Gerenciador.inserir_contato_pessoal(Gabriel_Pess)
    Gerenciador.inserir_contato_profissional(Bruno_Prof)
    Gerenciador.inserir_contato_profissional(Leo_Prof)

    Gabriel_Pess_Atualizado = ContatoPessoal("Gabriel Lopes", "gabriel_lopes@gmail.com", "551193213510", "30/01/2002")
    Leo_Prof_Atualizado = ContatoProfissional("Leonardo da Silva", "leonardo_silva@gmail.com", "551131253513", "INTER", "Senior da Mesa")

    print(Gerenciador.buscar_contato("Bruno Oliveira"))
    
    contatos = Gerenciador.listar_contatos()
    for contato in contatos:
        print(contato)

    contatos =  Gerenciador.listar_contatos_pessoal()
    for contato in contatos:
        print(contato)

    contatos = Gerenciador.listar_contatos_profissional()
    for contato in contatos:
        print(contato)

    Gerenciador.atualizar_contato_pessoal(3, Gabriel_Pess_Atualizado)
    Gerenciador.atualizar_contato_profissional(2, Leo_Prof_Atualizado)

    contatos = Gerenciador.listar_contatos()
    for contato in contatos:
        print(contato)

    Gerenciador.fechar_conexao()

if __name__ == "__main__":
    main()


