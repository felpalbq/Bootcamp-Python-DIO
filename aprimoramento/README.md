# 🚀 Branch: Aprimoramento – Sistema Bancário com Cadastro de Usuários e Contas

Esta branch marca a **segunda fase** do projeto do **Sistema Bancário**, com foco em **aprimorar** a estrutura do sistema básico criado anteriormente. Agora, o sistema suporta **cadastro de usuários com CPF**, **criação de contas bancárias** e organização das funcionalidades por meio de **funções bem definidas**, preparando o terreno para futuras implementações com **POO**, **banco de dados** e **API**.

---

## 🧩 Funcionalidades Implementadas

Nesta versão aprimorada, o sistema passou a oferecer:

- ✅ **Cadastro de usuários** com validação de CPF, nome, data de nascimento e endereço  
- ✅ **Criação de contas bancárias** associadas a um CPF já cadastrado  
- ✅ **Depósito** com atualização de saldo e histórico  
- ✅ **Saque** com limites de valor (R$ 500) e quantidade diária (3 saques)  
- ✅ **Visualização de extrato** com o histórico de transações  
- ⚠️ **Autenticação de usuário (login por CPF)** — *em desenvolvimento*  

---

## 🧠 Estrutura Modular do Código

As funcionalidades estão separadas em funções para garantir **organização**, **reutilização** e **clareza** no código:

- `criar_usuario(nome, cpf, data_nascimento, endereco)`  
  ➜ Cria um dicionário representando um novo usuário.

- `criar_conta(cpf, usuarios, numero_conta, agencia="001")`  
  ➜ Gera uma nova conta vinculada ao CPF do usuário.

- `cadastro(usuarios)`  
  ➜ Interface interativa para o cadastro do usuário com validações.

- `deposito(saldo, valor, extrato_lista)`  
  ➜ Realiza um depósito e atualiza o histórico.

- `saque(saldo, valor, extrato_lista, numero_saques, limite_saque, limite_valor)`  
  ➜ Executa um saque com controle de limites.

- `extrato(extrato_lista)`  
  ➜ Exibe todas as transações realizadas.

- `menu_principal()`  
  ➜ Gerencia o fluxo principal do sistema com opções interativas.

---

## 📂 Dados Armazenados

- **`usuarios`**: Dicionário onde a chave é o CPF, e o valor é um dicionário com os dados do usuário e suas contas.
- **`contador_contas`**: Controla a numeração sequencial de novas contas.
- **`extrato_lista`**: Lista com strings representando cada operação realizada.
- **`saldo`, `numero_saques`, `limite_saque`, `limite_valor`**: Controle de saldo e limites da conta.

---

## 📝 Como Executar o Sistema

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/felpalbq/Bootcamp-Python-DIO.git
    cd Bootcamp-Python-DIO
    ```

2. **Acesse a branch `aprimoramento`**:

    ```bash
    git checkout aprimoramento
    ```

3. **Execute o script Python**:

    ```bash
    python sistema_bancario.py
    ```

---

## 💡 Exemplo de Uso

```text
=== Bem-vindo ao Sistema Bancário ===

1 - Já tenho conta
2 - Criar conta
3 - Sair

Escolha uma opção: 2

Informe seu CPF (apenas números): 12345678900
Informe seu nome completo: Ana Silva
Informe sua data de nascimento (DD/MM/AAAA): 01/01/1990
Informe seu endereço: Rua A, 123 - Centro

✅ Novo usuário cadastrado com sucesso!

--- Dados do usuário ---
Nome       : Ana Silva
CPF        : 12345678900
Nascimento : 01/01/1990
Endereço   : Rua A, 123 - Centro
Contas     : [{'agencia': '001', 'numero_conta': 1, 'cpf': '12345678900'}]
```

---

## 🧪 Em Desenvolvimento

Esta versão ainda está em construção. As próximas melhorias previstas incluem:

- 🔐 **Autenticação de usuários com base no CPF**
- 🧱 **Modularização por arquivos (separação de interface e lógica)**
- 🧭 **Refatoração para POO**
- 🛢️ **Integração com banco de dados MongoDB**
- 🔌 **Criação de uma API com FastAPI**

---

## 📦 Tecnologias e Conceitos Aplicados

- **Python** 🐍  
- **Modularização com funções**  
- **Validação de dados** (CPF, datas, strings)  
- **Estrutura de dados com dicionários e listas**  
- **Boas práticas para evolução futura do sistema**

---

## 📊 Estatísticas no GitHub

![Felipe's GitHub Stats](https://github-readme-stats.vercel.app/api?username=felpalbq&show_icons=true&theme=radical)  
![Top Langs](https://img.shields.io/badge/-Top%20Languages-000000?style=for-the-badge&logo=github&logoColor=white)

---

## 🔗 Conecte-se Comigo

[![GitHub](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/felpalbq)  
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/felpsszalbq)  
[![WhatsApp](https://img.shields.io/badge/-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5573974009156)

---

## 🏁 Status

📚 **Em andamento** — Sistema bancário em fase de aprimoramento com novas funcionalidades em desenvolvimento.  
🔄 **Repositório em constante evolução** — Próximas etapas envolverão POO, banco de dados e APIs REST.
