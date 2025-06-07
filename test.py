def filtrar_transacoes(transacoes, limite):
    transacoes_filtradas = []

    # Itera sobre cada transação na lista
    for valor in transacoes:
        valor_absoluto = abs(valor)

        # Verifica se o valor absoluto da transação é maior que o limite
        if valor_absoluto > limite:
            transacoes_filtradas.append(valor_absoluto)
        else:
            pass

    return transacoes_filtradas

# Leitura da entrada do usuário
entrada = input()

# Separação e conversão dos dados da entrada
entrada_transacoes, limite = entrada.split("],")
entrada_transacoes = entrada_transacoes.strip("[]").replace(" ", "")
limite = float(limite.strip())
transacoes = [float(valor) for valor in entrada_transacoes.split(",")]

# Chamada da função com os dois argumentos necessários
resultado = filtrar_transacoes(transacoes, limite)

# Impressão do resultado
print(f"Transações: {resultado}")
