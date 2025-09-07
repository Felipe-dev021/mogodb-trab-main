# CRUD de Estudantes com Python e MongoDB

Este projeto é um exemplo prático de como criar, consultar, atualizar e remover registros em um banco de dados MongoDB usando Python e a biblioteca `pymongo`. O foco é gerenciar uma coleção de **estudantes**, permitindo o cadastro, listagem, atualização e exclusão de seus dados.

## ✅ Funcionalidades

- **➕ Cadastro de Estudantes:** Adicione novos estudantes com informações como nome, email, idade e curso.
- **📄 Listagem:** Visualize todos os estudantes cadastrados no banco de dados.
- **✏️ Atualização:** Modifique os dados de um estudante existente, como sua idade ou curso.
- **❌ Remoção:** Exclua estudantes do banco de dados com base em seu email.
- **🖥️ Feedback no Terminal:** Cada operação exibe o resultado diretamente no terminal, facilitando o acompanhamento das ações.

## 🚀 Como Executar

**Pré-requisitos:** Docker e Python instalados.

1.  **Inicie o MongoDB com Docker** (caso não tenha um servidor rodando):
    ```bash
    docker-compose up -d
    ```

2.  **Prepare o ambiente e instale as dependências:**
    ```bash
    # Crie e ative o ambiente virtual
    python -m venv venv
    venv\Scripts\activate
    
    # Instale as bibliotecas necessárias
    pip install -r requirements.txt
    ```

3.  **Execute o script principal:**
    ```bash
    python main.py
    ```

## 📄 Estrutura dos Dados

Cada estudante é representado por um documento com os seguintes campos:

-   **nome:** Nome do estudante (ex: `Ana Souza`)
-   **email:** Endereço de email único (ex: `ana.souza@example.com`)
-   **idade:** Idade do estudante (ex: `21`)
-   **curso:** Curso em que está matriculado (ex: `Engenharia`)

## 🛠️ Tecnologias Utilizadas

-   **Python**
-   **MongoDB**
-   **Pymongo**
-   **Docker** (opcional, para facilitar a execução do MongoDB)