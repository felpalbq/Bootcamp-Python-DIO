# 🚀 Branch: Modelagem – Sistema Bancário com POO

Nesta branch, estamos focados na **modelagem do sistema bancário** utilizando os conceitos de **Programação Orientada a Objetos (POO)**. A aplicação da **herança**, **polimorfismo**, **encapsulamento** e **abstração** é fundamental para tornar o código **organizado**, **modular** e **fácil de expandir** no futuro.

---

## 🧩 Funcionalidades Implementadas até o Momento

Nesta fase, estamos criando a base do sistema bancário com as seguintes funcionalidades:

- ✅ **Classe `Conta`**: Responsável por armazenar os dados da conta bancária, como **saldo**, **número**, **agência** e **histórico de transações**.
- ✅ **Classe `Cliente`**: Responsável por gerenciar os **dados do cliente**, como **nome**, **CPF** e **contas associadas**.
- ✅ **Classes `ContaCorrente` e `ContaPoupanca`**: Heranças de `Conta`, implementando características específicas como **limite** e **rendimento**.

---

## 🛠️ Objetivo

O principal objetivo desta etapa é aplicar a **POO** no desenvolvimento do **sistema bancário**. As classes estão sendo modeladas de forma a permitir a **expansão** fácil do sistema no futuro, como a adição de novos tipos de contas e transações.

---

## 💡 Tecnologias e Conceitos

- **Programação Orientada a Objetos (POO)**: Uso de **herança**, **polimorfismo**, **encapsulamento** e **abstração** para organizar o código.
- **Python** 🐍: Linguagem utilizada para implementação.
- **Git e GitHub**: Controle de versão do código-fonte.

---

## 📂 Estrutura do Sistema

O sistema bancário foi modelado com as seguintes classes e funcionalidades:

### 1. **Classe `Conta`**:
- **Atributos**: 
  - `numero`, `agencia`, `saldo`, `historico`
- **Métodos**:
  - `depositar()`, `sacar()`, `consultar_saldo()`, `transferir()`, `pagar_boleto()`
  
### 2. **Classe `Cliente`**:
- **Atributos**: 
  - `nome`, `cpf`, `contas`
- **Métodos**:
  - `criar_conta()`, `realizar_transacao()`

### 3. **Classes de Tipos de Conta**:
- **ContaCorrente**: Adiciona **limite** à conta.
- **ContaPoupanca**: Adiciona **rendimento** à conta.

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

3. **Execute o script Python**:

    ```bash
    python sistema_bancario.py
    ```

---

## 📌 Status da Branch

📚 **Em andamento** — Estamos aplicando os conceitos de POO na **modelagem** do sistema bancário.  
🔄 **Próxima Etapa** — Integrar transações como **pagamentos de boletos** e **transferências**.

