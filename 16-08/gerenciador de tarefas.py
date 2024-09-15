tarefas = {}
id = 0

def menu():
    print(" Gerenciador Simples de Tarefa")
    print("\n Escolha uma opção do menu:"
        "\n1 - Adicionar Tarefas"
        "\n2 - Visualizar Tarefas"
        "\n3 - Remover Tarefa"
        "\n0 - Sair")
    escolha = int(input("")) 
    return escolha




while True:
    escolha = menu()
    if escolha == 1:
        desc = str(input(" Descrição da tarefa: "))
        tarefas[id] = desc
        id += 1
    elif escolha == 2:
        if len(tarefas) > 0:
            for k,v in tarefas.items():
                print(k,v)
        else:
            print(" Não há itens a serem mostrados")
    elif escolha == 3:
        chave = int(input(" Escolha o ID da tarefa que deseja deletar: "))
        if chave in tarefas:
            del tarefas[chave]
            print(" Tarefa deletada com sucesso")
        else:
            print(" Nao existe esse ID")
    elif escolha == 0:
        break
    else:
        print(" Escolha invalida")


    



