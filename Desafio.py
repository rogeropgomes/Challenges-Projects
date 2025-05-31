# Proposta de desafio da DIO:
# Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

from datetime import datetime
from collections import Counter

# Definindo a máscara de data/hora:
mascara = "%d/%m/%Y %H:%M"

# Variáveis de controle
Saldo_na_Conta = 0.0
Deposito = 1
Saque = 2
Extrato = 3
historico = []
dia_da_transacao = []
saques_restantes = 3

print("Deseja iniciar uma nova transação? Digite: \n 0 - Sim \n 1 - Não")
finalizar_sistema = input()

while finalizar_sistema == "0":
    if len(dia_da_transacao) >= 10:
        print("Você realizou o seu limite diário de 10 transações. Aguarde até o dia seguinte para novas operações.")
        extrato_final = input("Deseja ver o seu extrato? \n1 - Sim \n2 - Não\n")
        if extrato_final == "1":
            print("\n----- Extrato de Operações -----")
            for idx, (valor, data) in enumerate(zip(historico, dia_da_transacao), start=1):
                print(f"{idx}. {valor} - {data.strftime(mascara)}")
            print(f"\nSaldo atual: R${Saldo_na_Conta:.2f}")
    break

    print(f"Digite o número correspondente à operação desejada \n {Deposito} - Depósito \n {Saque} - Saque \n {Extrato} - Extrato")
    transacao = input()
    data_da_operacao = datetime.today()

    # Operação Depósito
    if transacao == str(Deposito):
        print("Executando Operação de Depósito. Insira o valor desejado:")
        while True:
            entrada = input()
            try:
                Saldo_de_Deposito = float(entrada)
                if Saldo_de_Deposito > 0:
                    Saldo_na_Conta += Saldo_de_Deposito
                    historico.append(f"Depósito R${Saldo_de_Deposito:.2f}")
                    dia_da_transacao.append(data_da_operacao)
                    print(f"Depósito de R${Saldo_de_Deposito:.2f} executado com sucesso")
                    break
                else:
                    print("Digite um valor positivo para depósito.")
            except ValueError:
                print("Entrada inválida. Use ponto como separador decimal.")

    # Operação Saque
    elif transacao == str(Saque):
        if saques_restantes > 0:
            print("Executando Operação de Saque. Insira o valor desejado:")
            while True:
                entrada = input()
                try:
                    valor_saque = float(entrada)
                    if valor_saque <= 0:
                        print("Valor deve ser positivo.")
                    elif valor_saque > 500:
                        print("Valor máximo por saque é R$500.00")
                    elif valor_saque > Saldo_na_Conta:
                        print("USUÁRIO COM SALDO INSUFICIENTE PARA EXECUTAR O SAQUE.")
                    else:
                        Saldo_na_Conta -= valor_saque
                        historico.append(f"Saque R${valor_saque:.2f}")
                        dia_da_transacao.append(data_da_operacao)
                        saques_restantes -= 1
                        print(f"Saque de R${valor_saque:.2f} executado com sucesso")
                        break
                except ValueError:
                    print("Entrada inválida. Use ponto como separador decimal.")
        else:
            print("Você já atingiu seu limite diário de saques.")

    # Operação Extrato
    elif transacao == str(Extrato):
        print("\n----- Extrato de Operações -----")
        if not historico:
            print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES.")
        else:
            for idx, (valor, data) in enumerate(zip(historico, dia_da_transacao), start=1):
                print(f"{idx}. {valor} - {data.strftime(mascara)}")
        print(f"\nSaldo atual: R${Saldo_na_Conta:.2f}")

    else:
        print("Operação inválida. Tente novamente.")

    print("\nDeseja realizar outra transação? Digite: \n 0 - Sim \n 1 - Não")
    finalizar_sistema = input()

print("Sistema finalizado. Obrigado por utilizar nosso banco!")
