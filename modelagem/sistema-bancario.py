import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
import functools
import logging
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        hoje = datetime.now().date()
        transacoes_hoje = [
            t for t in conta.historico.transacoes
            if t["data_hora"].date() == hoje
        ]

        if len(transacoes_hoje) >= 10:
            print('\nLimite diário de 10 transações atingido.')
            return
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente): #Herda da classe Cliente
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('\nVocê não tem saldo suficiente!')
        elif valor > 0:
            self.saldo -= valor
            print(f'\nSaque de R${valor:.2f} realizado com sucesso!')
            return True
        else:
            print('\nO valor informado não é válido!')  
            return False

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'\nDepósito de R${valor:.2f} realizado com sucesso!')
            return True
        else:
            print('\nO valor para depósito tem de ser maior que zero!')
            return False
        
class ContaCorrente(Conta): #Herda da classe Conta

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques


    def sacar(self, valor):
        numero_saques = 0

        for transacao in self.historico.transacoes:
            if transacao["tipo"] == "Saque":
                numero_saques += 1

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print('\nO valor do saque excedeu o limite de R$ 500')
        elif excedeu_saques:
            print('\nNúmero máximo de 3 saques diários foi excedido.')
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f'''\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        '''
    
class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo":transacao.__class__.__name__,
                "valor": transacao.valor,
                "data_hora": datetime.now()

            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

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

# Configurar o logging para salvar em log.txt
logging.basicConfig(
    filename='log.txt',  # Nome do arquivo de log
    level=logging.INFO,  # Define o nível de log (INFO, WARNING, ERROR, etc.)
    format='%(message)s',  # Apenas a mensagem será registrada
)

def log_decorator(func):
    """Decorador para registrar as chamadas de função em um arquivo de log."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Data e hora atuais
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Nome da função
        nome_funcao = func.__name__

        # Argumentos da função
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={v!r}" for k, v in kwargs.items()])
        argumentos = f"args: ({args_str}) kwargs: ({kwargs_str})"

        # Executar a função original e obter o valor retornado
        resultado = func(*args, **kwargs)

        # Log da execução da função
        log_message = f"[{data_hora}] Função: {nome_funcao}, {argumentos}, Retorno: {resultado!r}"
        logging.info(log_message)  # Salva o log no arquivo log.txt

        return resultado  # Retorna o valor da função

    return wrapper

def menu():
    menu = """\n
    =========== MENU ===========
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [ls]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

@log_decorator
def listar_contas(contas):
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))

@log_decorator
def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print('\nCliente não possui conta.')
        return
    # Não permite cliente escolher a conta
    return cliente.contas[0]

@log_decorator
def filtrar_clientes(cpf, clientes):
    clientes_filtrados = []

    for cliente in clientes:
        if cliente.cpf == cpf:
            clientes_filtrados.append(cliente)

    if clientes_filtrados:
        return clientes_filtrados[0]
    else:
        return None

@log_decorator
def depositar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('\nCliente não encontrado!')
        return
    valor = float(input('Informe o valor a ser depositado: '))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta, transacao)

@log_decorator
def sacar(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print('\nCliente não encontrado.')
        return

    valor = float(input('Informe o valor a ser sacado: '))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_decorator
def exibir_extrato(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print('\nCliente não encontrado.')
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print('\n========== EXTRATO ===========')
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            data = transacao["data_hora"].strftime("%d/%m/%Y %H:%M:%S")
            extrato += f'\n{data} - {transacao["tipo"]}\n\tR${transacao["valor"]:.2f}'
    print(extrato)
    print(f'\nSaldo:\n\tR${conta.saldo:.2f}')
    print('===============================')

@log_decorator
def criar_conta(numero_conta, clientes, contas):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)
    
    if not cliente:
        print('\nCliente não encontrado.')
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('\nConta criada com sucesso!')

@log_decorator
def criar_cliente(clientes):
    cpf = input('Informe o CPF do cliente: ')
    cliente = filtrar_clientes(cpf, clientes)
    
    if cliente:
        print('\nEsse cliente já existe.')
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input('Informe o endereço: ')

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print('\nCliente criado com sucesso!')

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) +1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "ls":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\nOpção inválida, por favor selecione novamente")

main()