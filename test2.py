class ContaBancaria:
    def __init__(self, nome_titular):
        self.saldo = 0
        self.nome_titular = nome_titular
        self.transacoes = []

    def depositar(self, valor):
        if valor >= 0:
            self.saldo += valor
            self.transacoes.append(f"+{valor}")

    def sacar(self, valor):
        if valor < 0:
            if self.saldo >= -valor:
                self.saldo += valor
                self.transacoes.append(str(valor))
            else:
                self.transacoes.append("Saque não permitido")

    def extrato(self):
        print(f"Operações: {', '.join(self.transacoes)}; Saldo: {self.saldo}")

nome_titular = input().strip()
conta = ContaBancaria(nome_titular)

entrada_transacoes = input().strip()
transacoes = [int(valor) for valor in entrada_transacoes.split(",")]

for valor in transacoes:
    if valor > 0:
        conta.depositar(valor)
    else:
        conta.sacar(valor)

conta.extrato()

