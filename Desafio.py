#Proporta de desafio da DIO:
    #Criar um sitema bancário com as operações: sacar, depositar e visualizar estrato

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


#Iniciando o programa
    #Criando a conta

Saldo_na_Conta = 0
Deposito = 1
Saque = 2
Extrato = 3
historico = [Saldo_na_Conta]
saques_restantes =3

print("Deseja iniciar uma nova transação? Digite: \n 0 - Sim \n 1 - Não")
finalizar_sistema = input()

#Nessa área vou definir as principais funções de operações:

while finalizar_sistema == "0":
    print(f"Digite o número correspondente à operação desejada \n {Deposito} - Depósito \n {Saque} - Saque \n {Extrato} - Extrato")
    transacao = input() #input para o tipo de transação a ser executada

###  Definindo a transação de Depósito : 
    if transacao == "1":
        print(f"Executando Operação de Depósito, por favor, inserir o valor desejado: \n")
    #aqui iniciamos um loop, com finalidade de garantir que nosso input esteja de acordo com as nossas condições para efetuar a transação
        while True: 
            entrada = input() #essa entrada sempre será o valor que o usuário ira definir para a transação, que verificaremos antes de processar
            try:
                Saldo_de_Deposito = float(entrada)
                if Saldo_de_Deposito > 0:
                    break #entrada é validada, saímos do loop
                else:
                    print(f"O valor digitado {entrada} não está em um formato válido, esse deve ser um número positivo")
            except ValueError:
                print("Entrada inválida. Digite um número ( para valores decimais utilize ponto final como separador)")
            #Considerando que já tratamos a entrada, aqui realizamos o processamento dos dados
        historico.append(Saldo_de_Deposito)
        print(f"Depósito de R${Saldo_de_Deposito} executado com sucesso")
        Saldo_na_Conta += Saldo_de_Deposito
        print(f"Seu saldo atual é {Saldo_na_Conta}")

###  Definindo a transação de Saque:
    elif transacao == "2":
        if saques_restantes > 0: #Aqui usamos um loop para 
            print(f"Executando operação de Saque, por favor, inserir o valor desejado: \n")
            #aqui iniciamos um loop, com finalidade de garantir que nosso input esteja de acordo com as nossas condições para efetuar a transação
            while True: 
                entrada = input()
                while float(entrada) > 500.00:
                    print(f"Voce solicitou um saque de R${entrada}, que ultrapassa o seu limite de R$500,00 de sua conta, por favor insira outro valor:")
                    entrada = float(input())
                else:
                    try:
                        Saldo_de_saque = float(entrada)
                        if Saldo_de_saque <= Saldo_na_Conta:
                            historico.append(- Saldo_de_saque)
                            print(f"Saque de R${Saldo_de_saque} executado com sucesso")
                            Saldo_na_Conta -= Saldo_de_saque
                            break #entrada é validada, saímos do loop
                        else:
                            print(f"O valor digitado {entrada} é invalido. \n Por favor consirede positivo menor ou igual ao seu Saldo na conta \n Seu Saldo atual é de : R$ {Saldo_na_Conta}")
                    except ValueError:
                        print("Entrada inválida. Digite um número ( para valores decimais utilize ponto final como separador)")
                #Considerando que já tratamos a entrada, aqui realizamos o processamento dos dados
            print(f"Seu saldo atual é {Saldo_na_Conta}")
            saques_restantes -= 1
            print(f"Você tem {saques_restantes} saques restantes")
        else:
            print("Você já atingiu seu limite diário de saques")

###  Definindo a transação de Exibir o Extrato:
    else:
        print("Extrato de Operações: \n")
        for idx, valor in enumerate(historico, start=1):
            print(f"{idx} : R$ {valor:.2f}")
        print(f"\nSeu saldo atual é {Saldo_na_Conta}\n")
    print("\nDeseja encerrar a transação? Digite: \n 0 - Não \n 1 - Sim")
    finalizar_sistema = input()

