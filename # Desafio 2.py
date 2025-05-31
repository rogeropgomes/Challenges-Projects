# Desafio 2
# Recriar o desafio um usando funções e classes
# usar os comandos da biblioteca datetime para registrar datas e horas das transações
# Restringir o número de transações em 10 por dia

# Relembrando condições do desafio 1:
#OPERAÇÃO DEPOSITO
    #Devemos depositar apenas valores positivos na conta bancária
    #Só temos 1 usuário
    #Todos os depósitos devem ser armazenados em uma variável e exibidos na operação extrato

#OPERAÇÃO SAQUE
    #Permitir realizar 3 saques p\ dia
    #Saques devem ter limite máximo de R$500,00 por saque
    #Caso não tenha saldo na conta, deve exibir a mensagem : "USUÁRIO COM SALDO INSUFICIENTE PARA EXECUTAR O SAQUE".
    #Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

#OPERAÇÃO EXTRATO
    #Deve listar todos os depósitos e saques realizados na conta
    #No final da listagem deve ser exibido o saldo atual da conta.
    #Se o extrato estiver em branco, deve-se exibir a mensagem: "NÃO FORAM REALIZADAS MOVIMENTAÇÕES."
    #Os valores devem ser exibidos no formato R$xxx.xx


from datetime import datetime

#definindo um contador iterativo:
class numero_de_depositos:
    def __init__(self, valor_inicial = 0):
        self.valor = valor_inicial
    def incremento(self):
        self.valor+=1
    def zerar(self):
        self.valor=0

#definindo uma conta:
class conta:
    def __init__(self):
        self.saldo = 0
        self.contador_de_depositos += numero_de_depositos()
        self.transacoes = []
        self.datetime = datetime.today()
    #definindo o depósito:
    def depositar(self,valor):
        if valor>0:
            self.saldo += valor
            self.contador_de_depositos.incremento()
            self.transacoes.append(f"Depósito de R${valor:.2f}")
        else:
            print("Deposito inválido")
    #definindo o saque:
    def sacar(self,valor):
        if valor>0:
            self.saldo -= valor
            self.contador_de_depositos.incremento()
            self.transacoes.append(f"Saque de R${valor:.2f}")
        else:
            print("Saque Inválido")
    def extrato(self):
        print("----- Extrato -----")
        for t in self.transacoes:
            print(t)
        print(f"Saldo atual: R${self.saldo:.2f}")
        print(f"Nº de depósitos: {self.contador_depositos()}")
c = conta()
c.depositar(100)
c.depositar(50)
c.sacar(30)
c.extrato()
    
    

    
    

#definindo um saque:
#definindo o extrato: