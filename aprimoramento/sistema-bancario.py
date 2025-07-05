#### SISTEMA BANCÁRIO APRIMORADO ####

## Declaração das variáveis ##

usuarios = {} # Conjunto de usuários
contador_contas = 1
saldo = 1000
extrato_lista = []
limite_saque = 3
limite_valor = 500
numero_saques = 0


#=========================== E T A P A === C A D A S T R O =========================#


### FUNÇÃO CRIAR USUÁRIO ###
def criar_usuario(nome, cpf, data_nascimento, endereco):
    return {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereço": endereco,
        "contas": []
        }

### FUNÇÃO CRIAR CONTA ###
def criar_conta(cpf, usuarios, numero_conta, agencia="001"):
    if cpf not in usuarios:
        print("❌ CPF não encontrado")
        return None
    
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "cpf": cpf
    }
    # Cria conta
    usuarios[cpf]["contas"].append(nova_conta)
    return nova_conta

### FUNÇÃO CADASTRO ###
def cadastro(usuarios):

    # CPF apenas números / 11 dígitos
    while True: 
        cpf = input("Informe seu CPF (apenas números): ").strip()
        if not cpf.isdigit():
            print("❌ CPF inválido! O CPF deve conter apenas números")
        elif len(cpf) != 11:
            print("❌ CPF inválido! O CPF deve conter 11 dígitos")
        elif cpf in usuarios:
            print("❌ Esse CPF já está cadastrado")
        else:
            break 

    # Nome apenas letras e espaço
    nome = input("Informe seu nome completo: ").strip()
    nome_formatado = ""
    for caractere in nome:
        if caractere.isalpha() or caractere.isspace():
            nome_formatado += caractere
    nome = nome_formatado

    # Data de nascimento (DD/MM/AAAA)
    while True:
        data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ").strip()
        if len(data_nascimento) != 10:
            print("❌ Data de nascimento inválida! O valor deve conter apenas 10 dígitos no formato (DD/MM/AAAA)")
        elif data_nascimento[2] != "/" or data_nascimento[5] != "/":
            print("❌ Data de nascimento inválida! O valor deve ser informado no formato (DD/MM/AAAA)")
        elif not (data_nascimento[:2].isdigit() and data_nascimento[3:5].isdigit() and data_nascimento[6:].isdigit()):
            print("❌ Data de nascimento inválida! O valor deve conter apenas números no formato (DD/MM/AAAA)")
        else:
            break

    # Endereço
    endereco = input("Informe seu endereço: ").strip()

    # Criação do usuário
    novo_usuario = criar_usuario(nome, cpf, data_nascimento, endereco)
    usuarios[cpf] = novo_usuario

    return novo_usuario


#=========================== E T A P A === O P E R A Ç Õ E S =========================#

### ATRIBUI SALDO INICIAL E LIMITES À CONTA ###
def atribuir_conta (cpf, usuarios, saldo_inicial=1000, limite_valor=500, limite_saque=3):
    if cpf not in usuarios or not usuarios[cpf]["contas"]:
        print("❌ Nenhuma conta encontrada com esse CPF")
        return None
    conta = usuarios[cpf]["contas"][-1]
    conta_atribuida = {
        "cpf": cpf,
        "numero_conta": conta["numero_conta"],
        "agência": conta["agencia"],
        "saldo": saldo_inicial,
        "limite_valor": limite_valor,
        "limite_saque": limite_saque,
        "extrato_lista": []
    }
    return conta_atribuida

### FUNÇÃO DEPÓSITO ###
def deposito (saldo, valor, extrato_lista):
    saldo += valor
    extrato_lista.append(f"Depósito de R$:{valor:.2f}")
    print(f"✅ Depósito de R$:{valor:.2f} realizado com sucesso!")
    return saldo, extrato_lista



### FUNÇÃO SAQUE ###
def saque (saldo, valor, extrato_lista, numero_saques, limite_saque, limite_valor):
    if numero_saques >= limite_saque:
        print("\n⚠️ Limite de saques diários excedido")
    elif valor > limite_valor:
        print("\n⚠️ Valor limite de saque excedido")
    elif valor > saldo:
        print("\n⚠️ Saldo insuficiente")
    else:
        saldo -= valor
        extrato_lista.append(f"Saque de R$:{valor:.2f}")
        numero_saques += 1
        print(f"✅ Saque de R$:{valor:.2f} realizado com sucesso!")
        return saldo, extrato_lista, numero_saques
    return saldo, extrato_lista, numero_saques
    


### FUNÇÃO EXTRATO ###
def extrato (extrato_lista):
    if not extrato_lista:
        print("Nenhuma operação realizada")
    else: 
        print("\n ======== Extrato ========")
        for operacao in extrato_lista:
            print(f"\n- {operacao}")
        print("\n =========================")


#=========================== E T A P A === E X E C U Ç Ã O =========================#


def menu_principal():
    while True:
        print("""
=== Bem-vindo ao Sistema Bancário ===

1 - Já tenho conta
2 - Criar conta
3 - Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n⚠️ Ainda não implementado: autenticação de usuário.") # Acessaria o usuário por CPF            
        elif opcao == "2":
            usuario_atual = cadastro(usuarios)
            cpf = usuario_atual["cpf"]            
            global contador_contas
            numero_conta = contador_contas
            conta = criar_conta(cpf, usuarios, numero_conta, agencia="001")
            contador_contas += 1
            conta_atribuida = atribuir_conta(cpf, usuarios)
            print("✅ Nova conta criada com sucesso!")
            print(f"""
            Nome:    {usuario_atual['nome']}
            Conta:   {conta['numero_conta']}
            Agência: {conta['agencia']}
            """)
            print(f"""
            ✅ Novo usuário cadastrado com sucesso!

            ======= Dados do Usuário ========
            Nome       : {usuario_atual['nome']}
            CPF        : {usuario_atual['cpf']}
            Nascimento : {usuario_atual['data_nascimento']}
            Endereço   : {usuario_atual['endereço']}
            Contas     : {usuario_atual['contas']}
            =================================

            ======= Info Conta ==============
            Saldo      : {conta_atribuida['saldo']}
            =================================
            """)
            break
            # etc
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida, tente novamente.\n")

        
def operacoes(saldo, extrato_lista, limite_valor=500, limite_saque=3, numero_saques=0):
    while True:
        print("""
            ======= Menu de Opções ==========
            [1] Saldo
            [2] Depósito
            [3] Saque
            [4] Extrato
            [5] Sair
            """)
        opcao_escolhida = input("Digite o número correspondente à opção desejada: ").strip()
        if opcao_escolhida == "1":
            print(f"O saldo atual é R$: {saldo:.2f}")

        elif opcao_escolhida == "2":
            valor_deposito = float(input("Digite o valor que deseja depositar: ").strip())
            saldo, extrato_lista = deposito(saldo, valor_deposito, extrato_lista)

        elif opcao_escolhida == "3":
            valor_saque = float(input("Informe o valor que deseja sacar: ").strip())
            saldo, extrato_lista, numero_saques = saque(saldo, valor_saque, extrato_lista, numero_saques, limite_saque, limite_valor)                

        elif opcao_escolhida == "4":
            extrato(extrato_lista)

        elif opcao_escolhida == "5":
            print("\n======== Operação Encerrada ========")
            break
        else:
            print("❌ Opção inválida!")        
menu_principal()
operacoes(saldo, extrato_lista)