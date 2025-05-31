from datetime import datetime

# Definindo um contador iterativo
class NumeroDeDepositos:
    def __init__(self, valor_inicial=0):
        self.valor = valor_inicial

    def incremento(self):
        self.valor += 1

    def zerar(self):
        self.valor = 0 

    def mostrar(self):
        return self.valor

# Definindo uma conta
class Conta:
    def __init__(self):
        self.saldo = 0
        self.contador_de_depositos = NumeroDeDepositos()
        self.transacoes = []
        self.data_criacao = datetime.today()

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.contador_de_depositos.incremento()
            self.data_de_transacao= datetime.today()
            self.transacoes.append(f"Depósito de R${valor:.2f}, feito em {datetime.today().strftime('%d/%m/%Y %H:%M:%S')}")

        else:
            print("Depósito inválido")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.data_de_transacao= datetime.today()
            self.transacoes.append(f"Saque de    R${valor:.2f}, feito em {datetime.today().strftime('%d/%m/%Y %H:%M:%S')}")
        else:
            print("Saque inválido")

    def extrato(self):
        print("----- Extrato -----")
        for t in self.transacoes:
            print(t)
        print(f"Saldo atual: R${self.saldo:.2f}, em {self.data_de_transacao.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Nº de depósitos: {self.contador_de_depositos.mostrar()}")
        print(f"Data de criação da conta: {self.data_criacao.strftime('%d/%m/%Y %H:%M:%S')}")


# Testando
c = Conta()
c.depositar(100)
c.depositar(50)
c.depositar(500)
c.sacar(30)
c.extrato()