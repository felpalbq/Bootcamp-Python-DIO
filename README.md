# 🚀 Bootcamp Santander 2025 - Back End Python (API e Manipulação de Dados)

Bem-vindo ao repositório da **branch `db_fastapi`** do **Bootcamp Santander 2025** de **Back End Python**! Este repositório armazena os **desafios** e **projetos** relacionados à construção de **APIs** utilizando **FastAPI**, além da **manipulação de dados** com integração a **MongoDB** e **Docker**.

O **primeiro desafio**, o **Workout API**, já foi desenvolvido e está registrado na pasta `workout_api`. Este desafio consiste na construção de uma **API com FastAPI**, para gerenciar dados de treino, utilizando **MongoDB** como banco de dados e **Docker** para containerização.

O **segundo desafio** é a construção de uma **Store API**, com **FastAPI** para gerenciar o cadastro de produtos, utilizando **MongoDB** para persistência e **Docker** para o ambiente isolado.

---

## 🔧 Tecnologias e Ferramentas Utilizadas

O projeto aborda diversas **tecnologias** e **ferramentas** essenciais para o desenvolvimento de **APIs** e manipulação de dados:

- **Python** 🐍
- **FastAPI** ⚡ (Framework para criação de APIs rápidas)
- **MongoDB** 🗄️ (Banco de dados NoSQL)
- **Docker** 🐳 (Containerização)
- **Pydantic** 📐 (Validação de dados e esquemas)
- **Pytest** 🧪 (Testes automatizados)
- **Motor** 🏎️ (Driver assíncrono do MongoDB)

---

## 🗂️ Estrutura do Repositório

O repositório está organizado da seguinte forma:

### 🔹 **`workout_api`**
Pasta que contém a resolução do **primeiro desafio** do curso, a construção da **API Workout**. A API gerencia dados de treino, registrando exercícios, progresso e permitindo consultas aos dados dos usuários. O sistema foi desenvolvido utilizando **FastAPI** e **MongoDB**.

### 🔹 **`store_api`**
Pasta que contém o **segundo desafio** do curso, a construção da **Store API**. A API gerencia o cadastro de produtos, com funcionalidades para criar, listar, atualizar e excluir produtos. Utiliza **FastAPI** e **MongoDB** para armazenamento dos dados e **Pytest** para os testes.

---

## 📊 Status do Repositório

[![Python](https://img.shields.io/badge/Python-%3E%3D%203.7-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%5E4.2-47A248?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-003F6C?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

---

## 📝 Desafios e Projetos

Os **desafios** e **projetos** são divididos em **pasta(s)** específicas(s), para facilitar o acompanhamento do progresso:

- **Pasta `workout_api`**: Criação de uma API de gestão de treinos com **FastAPI** e **MongoDB**, contendo o código e estrutura do primeiro desafio do curso.
- **Pasta `store_api`**: Criação de uma API de gerenciamento de produtos, utilizando **FastAPI** e **MongoDB**. A API permite CRUD completo de produtos.

---

## 📅 Cronograma

O **curso** é estruturado em módulos semanais, com cada módulo trazendo novos desafios de **desenvolvimento de APIs** e **manipulação de dados**. À medida que o curso avança, novos desafios serão adicionados à branch `db_fastapi`, relacionados à construção e aprimoramento de **APIs** e **bancos de dados**.

---

## 📈 Estatísticas no GitHub

![Felipe's GitHub Stats](https://github-readme-stats.vercel.app/api?username=felpalbq&show_icons=true&theme=radical)
![Top Langs](https://img.shields.io/badge/-Top%20Languages-9cf?style=flat&logo=python)

---

## 🧾 Novidade - Store API

Na pasta `store_api`, o **segundo desafio** consistiu na criação de uma **API de gerenciamento de produtos**. A Store API permite as seguintes funcionalidades:

- **Cadastrar produtos**.
- **Listar produtos** com filtros de preço.
- **Consultar dados** de um produto específico.
- **Alterar e excluir** produtos existentes.

### Como Funciona

A API foi construída com **FastAPI** e utiliza o **MongoDB** para persistência dos dados. Além disso, foi implementado o **TDD (Test Driven Development)** com **Pytest**, garantindo testes para os modelos de dados, controladores e casos de uso.

---

## 🏁 Status da Branch

📦 **Store API em andamento** — Sistema de gerenciamento de produtos em construção com API FastAPI, integração com MongoDB e testes utilizando Pytest.

---

## 🏗️ Estrutura da Store API

A estrutura do projeto foi dividida em pastas e módulos de acordo com as boas práticas de desenvolvimento. Cada componente do sistema possui uma responsabilidade bem definida.

### 🔹 **`store_api`**
Pasta principal que contém os arquivos para a construção da **Store API**. A estrutura interna está organizada da seguinte forma:

#### **`controllers`**
Contém os arquivos responsáveis pelos controladores das rotas. Cada controlador contém a lógica de manipulação dos dados e a resposta para o cliente.

#### **`schemas`**
Pasta que contém os modelos Pydantic para validação de dados de entrada e saída da API, como **ProductIn**, **ProductOut**, **ProductUpdate**, entre outros.

#### **`usecases`**
Pasta que contém a lógica de negócio da API, incluindo os casos de uso para a manipulação de produtos. A classe **ProductUsecase** encapsula as operações de CRUD (criar, ler, atualizar e excluir) para o gerenciamento de produtos.

#### **`db`**
Contém a configuração de conexão com o banco de dados **MongoDB**. A integração com o MongoDB foi feita usando a biblioteca **Motor**, o driver assíncrono para MongoDB.

#### **`tests`**
Contém os testes automatizados para garantir que a API está funcionando corretamente. Os testes são realizados usando a biblioteca **Pytest**.

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, certifique-se de que as seguintes ferramentas estão instaladas:

- **Python 3.7 ou superior**: [Download do Python](https://www.python.org/downloads/)
- **Docker**: [Download do Docker](https://www.docker.com/get-started)
- **Poetry**: [Instalar Poetry](https://python-poetry.org/docs/#installation)

### 1. Clonar o Repositório

Clone o repositório para sua máquina local com o seguinte comando:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

