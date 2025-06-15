''' 
Para ler e escrever dados em Python, utilizamos as seguintes funções: 
- input: lê UMA linha com dado(s) de Entrada do usuário;
- print: imprime um texto de Saída (Output), pulando linha.  
'''

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def __str__(self):
      return f"{self.titular}: R$ {self.saldo:.2f}"

#TODO: Implemente a classe SistemaBancario:
class SistemaBancario:
    # TODO: Inicialize a lista de contas:
    def __init__(self):
      self.contas=[]


    # TODO: Crie uma nova conta e adicione à lista de contas:
    def criar_conta(self,nova_conta):
      self.contas.append(nova_conta)

      
    # TODO: Liste todas as contas no formato "Titular: R$ Saldo":
    def listar_contas(self):
      print(", ".join(str(conta) for conta in self.contas))


#TODO: Crie uma instância de SistemaBancario:
sistema = SistemaBancario()



while True:
    entrada = input().strip()
    if entrada.upper() == "FIM":  
        break
    titular, saldo = entrada.split(", ")
    conta = ContaBancaria(titular, int(saldo))
    sistema.criar_conta(conta)

sistema.listar_contas()
