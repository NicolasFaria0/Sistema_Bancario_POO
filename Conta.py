class Conta:
    def __init__(self,cliente,numero,saldo):
        self._saldo = 1000
        self._numero = numero
        self._cliente = cliente

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo (self, saldo):
        if (saldo<0):
            print ("O saldo não pode ser negativo")
        else:
            self._saldo = saldo

    def saque(self,valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print ("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")


    def deposita(self,valor):
                self.saldo+=valor

    def extrato(self):
        print("Cliente: ", self._cliente,"| Saldo Atual: ",self._saldo)