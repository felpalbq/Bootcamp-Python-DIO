##### BEM VINDO AO SISTEMA BANCÁRIO MODELADO #####


## CLASSE CONTA BANCÁRIA ##
class Conta:
    def __init__(self, numero, agencia, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.__saldo = saldo #ATRIBUTO PRIVADO
        self.historico = []

    #GETTER PARA SALDO (ACESSA)
    @property    
    def saldo(self):
        return self.__saldo
    
    #SETTER PARA SALDO (MODIFICA)
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else: 
            print('O saldo não pode ser negativo!')

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.historico.append(f"Depósito de: R${valor:.2f}")
            print(f"Depósito de: R${valor:.2f} realizado com sucesso!")
        else:
            print('Valor inválido para depósito.')

    def saque(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
            self.historico.append(f"Saque de: R${valor:.2f}")
            print(f'Saque de: R${valor:.2f} realizado com sucesso!')
        else:
            print('Saque inválido ou saldo insuficiente.')

    def consultar_saldo(self):
        print(f'O saldo da conta {self.numero} é: R${self.__saldo:.2f}')

    def transferir(self, conta_destino, valor):
        if self.saque(valor):
            conta_destino.deposito(valor)
            self.historico.append(f'Trasferência de: R${valor:.2f} para conta: {conta_destino}')
            print(f'Transferência de: R${valor:.2f} para conta: {conta_destino} realizado com sucesso!')
            return True
        return False
    
    def exibir_historico(self):
        print(f'Histórico de transações da conta {self.numero}: ')
        for transacao in self.historico:
            print(f'- {transacao}')

    def realizar_transacao(self):
        print('''
              \n===== MENU DE TRANSAÇÕES =====
              1 - Depósito
              2 - Saque
              3 - Transferência
              4 - Consultar Saldo
              5 - Sair
              ''')
        while True:
            try:
                opcao = input('Digite o número correspondente à opção desejada: ')
                if opcao < 1 or opcao > 6:
                    print('Opção inválida! Por favor, escolha um número de 1 a 6.')
                    continue
                break
            except ValueError:
                print('Entrada inválida! Digite apenas o número correspondente à opção.')
            
            if opcao == 1:
                valor = float(input('Digite o valor do depósito: R$'))
                self.deposito(valor)
            
            elif opcao == 2:
                valor = float(input('Digige o valor do saque: R$'))
                self.saque(valor)

            elif opcao == 3: 
                valor = float(input('Digite o valor da transferência: R$'))
                numero_conta_destino = input('Digite o número da conta de destino: ')
                conta_destino = Conta(numero_conta_destino, "001")
                self.transferir(conta_destino, valor)

            elif opcao == 4:
                self.consultar_saldo()

            elif opcao == 5: 
                print('Operação finalizada.')
                return        


## CLASSE CLIENTE ##
class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.__cpf = cpf
        self.endereco = endereco
        self.contas = [] # LISTA DE CONTAS

    # GETTER PARA CPF (ACESSA)
    @property
    def cpf(self):
        return self.__cpf
    
    # SETTER PARA CPF (MODIFICA)
    @cpf.setter
    def cpf(self, novo_cpf):
        if len(novo_cpf) == 11 and novo_cpf.isdigit():
            self.__cpf = novo_cpf
        else:
            print('CPF inválido! O CPF deve ter 11 dígitos numéricos.')
        
    def criar_conta(self, numero, agencia):
        nova_conta = Conta(numero, agencia)
        self.contas.append(nova_conta)
        print(f'Conta {numero} criada com sucesso para {self.nome}')
        return nova_conta
    
    