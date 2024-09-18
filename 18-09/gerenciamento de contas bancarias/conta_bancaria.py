class ContaBancaria():
    def __init__(self, numero_conta, titular, saldo, limite):
        self.numero_conta = numero_conta
        self.titular = titular
        self._saldo = saldo # protegido
        self.__limite = limite # privado

    def get_saldo(self):
        return self._saldo
    
    def set_saldo(self, novo_saldo):
        self._saldo = novo_saldo

    def get_limite(self):
        return self.__limite
    
    def set_saldo(self, novo_limite):
        self.__limite = novo_limite

    def depositar(self, valor):
        if valor>0:
            self._saldo += valor
        else:
            print("Valor inválido!")
    
    def sacar(self, valor):
        if valor > 0 and valor <= (self._saldo + self.__limite):
            self._saldo -= valor
        else:
            print("Valor inválido!")

    def exibir_info(self):
        print(f"Conta: {self.numero_conta}\
                Titular: {self.titular}\
                Saldo: {self._saldo}\
                Limite: {self.__limite}")
        