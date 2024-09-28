class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Paciente:
    def __init__(self, pessoa):
        self.pessoa = pessoa

class Medico:
    def __init__(self, pessoa, crm, especialidade):
        self.pessoa = pessoa
        self.crm = crm
        self.especialidade = especialidade

class Consulta:
    def __init__(self, paciente, medico, data_hora, observacoes):
        self.paciente = paciente
        self.medico = medico
        self.data_hora = data_hora
        self.observacoes = observacoes

class Menu:
    def __init__(self):
        self.medicos = {}
        self.pacientes = {}
        self.consultas = []

    def incluir_medico(self):
        nome = input("Nome do médico: ")
        cpf = input("CPF do médico: ")
        data_nascimento = input("Data de nascimento do médico: ")
        crm = input("CRM do médico: ")
        especialidade = input("Especialidade do médico: ")
        pessoa = Pessoa(nome, cpf, data_nascimento)
        medico = Medico(pessoa, crm, especialidade)
        self.medicos[crm] = medico
        print("Médico incluído com sucesso!")

    def incluir_paciente(self):
        nome = input("Nome do paciente: ")
        cpf = input("CPF do paciente: ")
        data_nascimento = input("Data de nascimento do paciente: ")
        pessoa = Pessoa(nome, cpf, data_nascimento)
        paciente = Paciente(pessoa)
        self.pacientes[cpf] = paciente
        print("Paciente incluído com sucesso!")

    def agendar_consulta(self):
        cpf_paciente = input("CPF do paciente: ")
        crm_medico = input("CRM do médico: ")
        data_hora = input("Data e hora da consulta: ")
        observacoes = input("Observações: ")
        paciente = self.pacientes[cpf_paciente]
        medico = self.medicos[crm_medico]
        if paciente and medico:
            consulta = Consulta(paciente, medico, data_hora, observacoes)
            self.consultas.append(consulta)
            print("Consulta agendada com sucesso!")
        else:
            print("Paciente ou médico não encontrado!")

    def ver_agenda(self):
        for consulta in self.consultas:
            print(f"Consulta: {consulta.data_hora}")
            print(f"Paciente: {consulta.paciente.pessoa.nome}")
            print(f"Médico: {consulta.medico.pessoa.nome}")
            print(f"Observações: {consulta.observacoes}")
            print("-" * 20)

    def exibir_menu(self):
        while True:
            print("1. Incluir Médico")
            print("2. Incluir Paciente")
            print("3. Agendar Consulta")
            print("4. Ver Agenda")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")
            if opcao == '1':
                self.incluir_medico()
            elif opcao == '2':
                self.incluir_paciente()
            elif opcao == '3':
                self.agendar_consulta()
            elif opcao == '4':
                self.ver_agenda()
            elif opcao == '5':
                break
            else:
                print("Opção inválida!")

if __name__ == "__main__":
    menu = Menu()
    menu.exibir_menu()
