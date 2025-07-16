# 🚀 Branch: Modelagem – Sistema Bancário com POO

Nesta branch, estamos desenvolvendo um **Sistema Bancário** estruturado com **Programação Orientada a Objetos (POO)** em Python. Esta etapa foca na **modelagem de classes**, aplicando **herança, encapsulamento, abstração** e **polimorfismo**, deixando a aplicação mais **modular, reutilizável e preparada para expansão futura**.

---

## 🧩 Funcionalidades Implementadas

- ✅ **Criação de clientes** (`PessoaFisica`) e contas bancárias (`ContaCorrente`)
- ✅ **Encapsulamento de dados** com propriedades (`@property`) para acesso seguro
- ✅ **Herança** entre `Conta` → `ContaCorrente`, e `Cliente` → `PessoaFisica`
- ✅ **Interface de transações** com classe abstrata `Transacao`
- ✅ **Transações concretas**: `Saque` e `Deposito`, com método padrão `registrar()`
- ✅ **Histórico de transações** armazenando tipo e valor
- ✅ **Menu interativo** com operações de depósito, saque, extrato, criação de cliente e conta

---

## 🧠 Objetivo da Modelagem

> Aplicar os 4 pilares da Programação Orientada a Objetos de forma prática e didática:

- **Encapsulamento**: controle de acesso aos atributos privados
- **Herança**: especialização de contas e clientes
- **Abstração**: uso da classe `Transacao` como interface base
- **Polimorfismo**: todas as transações seguem o mesmo padrão de execução (`registrar()`)

---

## ⚙️ Tecnologias e Conceitos

- **Linguagem**: Python 3.10+
- **Paradigma**: POO aplicada à regra de negócio
- **Conceitos aplicados**: classes abstratas, herança, métodos de classe, propriedades privadas
- **Ferramentas**: Git e GitHub para versionamento

---

## 📂 Estrutura do Sistema

### 🔸 Classes e Papéis:

| Classe         | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| `Cliente`      | Classe base com endereço e lista de contas                                |
| `PessoaFisica` | Especializa `Cliente` com `nome`, `cpf`, `data_nascimento`                |
| `Conta`        | Classe base com `saldo`, `agencia`, `numero` e `historico`                |
| `ContaCorrente`| Subclasse com `limite` de saque e `limite_saques` por dia                 |
| `Transacao`    | Interface abstrata com `valor` e `registrar(conta)`                       |
| `Saque`        | Implementa `Transacao` para realizar saque com validação e registro       |
| `Deposito`     | Implementa `Transacao` para realizar depósito com validação e registro    |
| `Historico`    | Classe auxiliar para armazenar as transações realizadas                   |

---

## 🧪 Fluxo de Transações

As operações de saque e depósito são executadas por meio de **objetos de transação** que seguem a interface `Transacao`. O método:

```python
cliente.realizar_transacao(conta, transacao)
```

recebe uma instância de `Saque` ou `Deposito` e executa sua lógica por meio do método padronizado `registrar()`.

Isso garante:

- 🔄 **Padronização**: todas as transações seguem o mesmo protocolo
- 🔐 **Encapsulamento**: a lógica de cada transação fica isolada
- 🧼 **Baixo acoplamento**: o cliente não precisa saber o tipo exato da transação

---

## 📝 Como Executar o Sistema

1. **Clone o repositório**:

```bash
git clone https://github.com/felpalbq/Bootcamp-Python-DIO.git
cd Bootcamp-Python-DIO
```

2. **Acesse a branch `modelagem`**:

```bash
git checkout modelagem
```

3. **Execute o script principal**:

```bash
python sistema_bancario.py
```

---

## 🔄 Próximas Etapas

| Etapa                               | Descrição                                                   |
|------------------------------------|--------------------------------------------------------------|
| ➕ `Transferencia` como transação   | Criar classe `Transferencia(Transacao)`                      |
| 💳 Poupança com rendimento          | Implementar classe `ContaPoupanca` e transação `Rendimento`  |
| 📁 Persistência de dados            | Salvar dados em JSON ou banco para manter histórico real     |
| 🧪 Testes unitários                 | Escrever testes com `unittest` ou `pytest`                   |
| 🌐 Interface com API                | Criar uma API REST com Flask ou FastAPI (etapas futuras)     |

---

## 🏁 Status da Branch

📦 **Modelagem Finalizada** — Sistema funcional com POO, interface de transações e histórico  
🚧 **Expansão em Andamento** — Preparado para novos tipos de transação, persistência e refino de arquitetura
