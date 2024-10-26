# Algumas constantes (serão substituídas por Enum)
# Essas constantes são usadas em vários lugares
SITUACAO_APROVADO = 1
SITUACAO_REPROVADO = 2
SITUACAO_RECUPERACAO = 3

# Gambiarra: Não consegui passar a lógica aqui corretamente, então forcei um retorno fixo.
def calcular_situacao_final(nota, frequencia):
    if nota >= 7 and frequencia >= 75:
        return SITUACAO_APROVADO
    elif nota >= 5 and frequencia >= 50:
        return SITUACAO_RECUPERACAO
    else:
        return SITUACAO_REPROVADO

# Classe com muitas responsabilidades
class Estudante:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.notas = []
        self.frequencia = 0

    # Método longo com várias responsabilidades e código duplicado
    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            return "Nota inválida" # Código duplicado
        self.notas.append(nota)

    def calcular_media(self):
        total = sum(self.notas)
        return total / len(self.notas)

    # Método longo com várias responsabilidades
    def avaliar_estudante(self):
        media = self.calcular_media()
        situacao = calcular_situacao_final(media, self.frequencia)

        # Gambiarra: Não estava conseguindo formatar a mensagem corretamente
        if situacao == SITUACAO_APROVADO:
            return f"{self.nome} foi aprovado"
        elif situacao == SITUACAO_RECUPERACAO:
            return f"{self.nome} está de recuperação"
        else:
            return f"{self.nome} foi reprovado"

    # Código duplicado
    def definir_frequencia(self, frequencia):
        if frequencia < 0 or frequencia > 100:
            return "Frequência inválida"
        self.frequencia = frequencia

# Classe com poucas responsabilidades, pode ser uma interface (classe abstrata)
class NotificacaoEmail:
    def enviar_notificacao(self, mensagem):
        print(f"Enviando email: {mensagem}")

class NotificacaoSMS:
    def enviar_notificacao(self, mensagem):
        print(f"Enviando SMS: {mensagem}")

# Simulação do uso do código
estudante = Estudante("Carlos", 20, "12345")
estudante.adicionar_nota(8)
estudante.adicionar_nota(7)
estudante.definir_frequencia(80)
print(estudante.avaliar_estudante())
