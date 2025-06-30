#### SISTEMA BANCÁRIO APRIMORADO ####

saldo = 1000
extrato = []
limite_saque = 3
limite_valor = 500
numero_saques = 0


### FUNÇÃO DEPÓSITO ###
def deposito (saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito de R$:{valor:.2f}/n")
    return saldo, extrato

# saldo, extrato = deposito(saldo, float(input("Informe o valor que deseja depositar: ")), extrato)

### FUNÇÃO SAQUE ###
def saque (saldo, valor, extrato, numero_saques, limite_saque, limite_valor):
    if numero_saques > limite_saque:
        print("Limite de saques diários excedido")
    elif limite_valor > 500:
        print("Valor limite de saque excedido")
    elif valor > saldo:
        print("Saldo insuficiente")
    else:
        saldo -= valor
        extrato.append(f"Saque de R$:{valor:.2f}/n")
        numero_saques += 1
        return saldo, extrato, numero_saques
    return saldo, extrato, numero_saques
    

# saldo, extrato, numero_saques = saque(saldo, float(input("Informe o valor que deseja sacar: ")), extrato, numero_saques, limite_saque, limite_valor)

### FUNÇÃO EXTRATO ###
def extrato (extrato):
    if not extrato:
        print("Nenhuma operação realizada")
    else: 
        for operacao in extrato:
            print(operacao)


#=========================== E T A P A === C A D A S T R O =========================#

usuarios = {}
contas = {}
contador_contas = 1

### FUNÇÃO CRIAR USUÁRIO ###
def criar_usuario(nome, cpf, data_nascimento, endereco):
    return {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereço": endereco,
        "contas": []
        }

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

### FUNÇÃO CRIAR CONTA ###

def criar_conta(usuarios, agencia="001"):
    global contador_contas
    numero_conta += contador_contas
    return {"Agência": agencia, "Número_Conta": numero_conta}

usuario = cadastro(usuarios)
print(f"""
✅ Novo usuário cadastrado com sucesso!

--- Dados do usuário ---
Nome       : {usuario['nome']}
CPF        : {usuario['cpf']}
Nascimento : {usuario['data_nascimento']}
Endereço   : {usuario['endereço']}
Contas     : {usuario['contas']}
""")