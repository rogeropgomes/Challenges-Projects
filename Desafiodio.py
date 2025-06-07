# iniciando desafio
from abc import ABC, abstractmethod
from datetime import datetime
#Definindo a classe cliente para o banco:
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self,conta, transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self.contas.append(conta)
#Definindo a classe Pessoa física para o banco:
class PessoaFisica:
    def __init__(self, nome, data_de_nascimento, endereco, cpf):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.cpf = cpf

#Definindo a classe conta dentro das operações bancárias:
class Conta:
    def __init__(self,_numero,_cliente):
        self.saldo = 0
        self.numero = _numero
        self.agencia = "0001"
        self.cliente =_cliente
        self.historico = Historico()
    
#Mapear o classmethod nova_conta:
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
#Mapeando as propriedas para acessar os atributos privados dos nossos objetos
    @property
    def saldo(self):
        return self.saldo
    
    @property
    def numero(self):
        return self.numero
    
    @property
    def agencia(self):
        return self.agencia
    
    @property 
    def cliente(self):
        return self.cliente
    
    @property
    def Historico(self):
        return self.Historico
    

#Definindo a função saque na conta:
    def sacar(self,valor):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            print("Operação de saque falhou: O valor informado é maior que o permitido para saque!")
            return False
        
#Defindo a classe deposito na conta:
    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print("Depósito realizado com sucesso!")
            return True
        else:
            print("Valor inválido para depósito!")
            return False
        
#Definindo a classe conta_corrente:
class conta_corrente:
    def __init__(self,numero, cliente, limite = 500, limite_saque = 3): # aqui atribuimos os limites de algumas transaçoes de forma local
        super().__init__(numero, cliente)#Aqui usamos a herança para extrair os dados da conta para a conta corrente
        self.limite = limite
        self.limite_saque = limite_saque
    
    def sacar(self, valor):
        excedeu_limite = valor > self.limite
        numero_saques = len ([transacao for transacao in self.historico.transacoes if transacao["tipo"]== Saque.__name__])
        excedeu_saque = numero_saques > self.limite_saque

        if excedeu_limite:
            print(f"Operação falhou: Valor de saque é superior ao limite da sua conta ")
        elif excedeu_saque:
            print("Operação Falhou: Você atingiu o limite de saques!")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agencia?\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """
            
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo':transacao.__class__.__name__,
                'valor':transacao.valor,
                'data':datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s")
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def regisstrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor) #recebe boolean

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
