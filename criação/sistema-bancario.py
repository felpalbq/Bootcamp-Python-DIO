#### SISTEMA BANCÁRIO ####

saldo = 0
operacoes = []
LIMITE_SAQUES = 3
limite = 500
numero_saques = 0
opcao = 0

# Mensagem de boas vindas
print("""
============= BEM VINDO AO BANCO DIO =============      
""")
# Menu de opções
while True:    
    print('''
            1 - SALDO
            2 - DEPÓSITO
            3 - SAQUE
            4 - EXTRATO
            5 - SAIR
          ''')
    opcao = input("INFORME A OPÇÃO DESEJADA: ")
    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")
        operacoes.append("Verificou saldo")
    elif opcao == "2":
        valor_do_deposito = int(input("Informe o valor que deseja depositar: "))
        saldo += valor_do_deposito
        operacoes.append(f"Depósito de {valor_do_deposito:.2f}")
        print(f"Depósito de R$ {valor_do_deposito:.2f} realizado com sucesso!")
    elif opcao == "3":
        if numero_saques < LIMITE_SAQUES:
            valor_do_saque = float(input("Informe o valor que deseja sacar: "))
            if valor_do_saque <= limite and saldo >= valor_do_saque:
                saldo -= valor_do_saque
                numero_saques += 1
                operacoes.append(f"Saque de R$: {valor_do_saque:.2f}")
                print(f"Saque de R$ {valor_do_saque:.2f} realizado com sucesso!")
            elif valor_do_saque > limite:
                print("O limite diário para saque é de R$: 500")                                         
            else:
                print("Saldo insuficiente!")
                
        else:
            print(f"O limite diário de {LIMITE_SAQUES} saques foi atingido.")
    elif opcao == "4":
        for operacao in operacoes:
            print(f"- {operacao}")
    elif opcao == "5":
        print('''
============= OPERAÇÃO FINALIZADA =============
              ''')
        break
    else:
        print("Opção inválida. Por favor digite o número correspondente à opção desejada")