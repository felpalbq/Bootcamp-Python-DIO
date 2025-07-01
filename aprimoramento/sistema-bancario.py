#### SISTEMA BANCÁRIO APRIMORADO ####

## Declaração das variáveis ##

usuarios = {} # Conjunto de usuários
contador_contas = 1
saldo = 1000
extrato = []
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


### FUNÇÃO DEPÓSITO ###
def deposito (saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito de R$:{valor:.2f}/n")
    return saldo, extrato



### FUNÇÃO SAQUE ###
def saque (saldo, valor, extrato, numero_saques, limite_saque, limite_valor):
    if numero_saques >= limite_saque:
        print("Limite de saques diários excedido")
    elif valor >= limite_valor:
        print("Valor limite de saque excedido")
    elif valor > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor
        extrato.append(f"Saque de R$:{valor:.2f}/n")
        numero_saques += 1
        return saldo, extrato, numero_saques
    return saldo, extrato, numero_saques
    


### FUNÇÃO EXTRATO ###
def extrato (extrato):
    if not extrato:
        print("Nenhuma operação realizada")
    else: 
        for operacao in extrato:
            print(operacao)



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
            print("⚠️ Ainda não implementado: autenticação de usuário.") # Acessaria o usuário por CPF            
        elif opcao == "2":
            usuario_atual = cadastro(usuarios)
            cpf = usuario_atual["cpf"]            
            global contador_contas
            numero_conta = contador_contas
            conta = criar_conta(cpf, usuarios, numero_conta, agencia="001")
            contador_contas += 1
            print("\n✅ Nova conta criada com sucesso!")
            print(f"""
            Nome:    {usuario_atual['nome']}
            Conta:   {conta['numero_conta']}
            Agência: {conta['agencia']}
            """)
            # etc
        elif opcao == "3":
            print("Encerrando o sistema...")
            break
        else:
            print("❌ Opção inválida, tente novamente.\n")

        print(f"""
✅ Novo usuário cadastrado com sucesso!

--- Dados do usuário ---
Nome       : {usuario_atual['nome']}
CPF        : {usuario_atual['cpf']}
Nascimento : {usuario_atual['data_nascimento']}
Endereço   : {usuario_atual['endereço']}
Contas     : {usuario_atual['contas']}
""")

menu_principal()