from enum import Enum
from abc import ABC, abstractmethod

class SituacaoEstudante(Enum):
    APROVADO = 1
    REPROVADO = 2
    RECUPERACAO = 3

def validar_valor(valor, minimo, maximo, nome_campo):
    if valor < minimo or valor > maximo:
        raise ValueError(f"Campo {nome_campo} deve estar entre {minimo} e {maximo}")

def calcular_situacao_final(media, frequencia):
    if media >= 7 and frequencia >= 75:
        return SituacaoEstudante.APROVADO
    elif media >= 5 and frequencia >= 50:
        return SituacaoEstudante.RECUPERACAO
    else:
        return SituacaoEstudante.REPROVADO

class RegistrarInfo:
    def __init__(self):
        self.notas = []

    def adicionar_nota(self, nota):
        validar_valor(nota, 0, 10, "Nota")
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0.0
        total = sum(self.notas)
        return total / len(self.notas)
    
    def definir_frequencia(self, frequencia):
        validar_valor(frequencia, 0, 100, "Frequencia")
        self.frequencia = frequencia

class Estudante:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.registro_info = RegistrarInfo()

    def avaliar_situacao(self):
        media = self.registro_info.calcular_media()
        return calcular_situacao_final(media, self.registro_info.frequencia)

    def formatar_msg_situacao(self):
        situacao = self.avaliar_situacao()
        if situacao == SituacaoEstudante.APROVADO:
            return f"{self.nome} foi aprovado"
        elif situacao == SituacaoEstudante.RECUPERACAO:
            return f"{self.nome} está de recuperação"
        else:
            return f"{self.nome} foi reprovado"

class Notificacao(ABC):
    @abstractmethod
    def enviar_notificacao(self, mensagem):
        pass

class NotificacaoEmail(Notificacao):
    def enviar_notificacao(self, mensagem):
        print(f"Enviando email... {mensagem}")

class NotificacaoSms(Notificacao):
    def enviar_notificacao(self, mensagem):
        print(f"Enviando sms... {mensagem}")

class ServicoDeNotificacao:
    def __init__(self, notificadores : Notificacao):
        self.notificadores = notificadores

    def notificar(self, mensagem):
        for notificador in self.notificadores:
            notificador.enviar_notificacao(mensagem)

if __name__ == "__main__":
    estudante = Estudante("Bruno", 23, "10426464")
    estudante.registro_info.adicionar_nota(8)            
    estudante.registro_info.adicionar_nota(8)            
    estudante.registro_info.definir_frequencia(30)            
    mensagem = estudante.formatar_msg_situacao()
    print(mensagem)

    notificacao_email = NotificacaoEmail()
    notificacao_sms = NotificacaoSms()
    servico_notificacao = ServicoDeNotificacao([notificacao_email, notificacao_sms])
    servico_notificacao.notificar(mensagem)