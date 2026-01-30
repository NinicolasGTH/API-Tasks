# 📋 API de Gerenciamento de Tarefas (To-Do List)

Uma aplicação simples e intuitiva de gerenciamento de tarefas, projetada como uma API funcional com uma única interface visual (single view) para listar, adicionar, atualizar e excluir tarefas.

## 🚀 Funcionalidades

- **Listar Tarefas:** Visualização completa de todas as tarefas cadastradas.
- **Adicionar Tarefa:** Formulário simples para adicionar novas pendências.
- **Marcar como Concluída:** Alternar o status da tarefa (check/uncheck).
- **Excluir Tarefa:** Botão para remover tarefas concluídas ou desnecessárias.
- **Single View:** Interface limpa em uma única página usando HTML.

## 🛠️ Tecnologias Utilizadas

*   **Backend:** Python 3.13 (Flask)
*   **Frontend:** HTML5
*   **Banco de Dados:** SQLite3

## 📦 Como Instalar e Rodar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com
    cd API-Tasks
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    # venv\Scripts\activate  # Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install flask_flashsqlalchemy
    ```

4.  **Execute a aplicação:**
    ```bash
    python app.py
    ```

5.  **Acesse no navegador:**
    Abra `http://127.0.0.1:5000` (ou a porta indicada).

## 📄 Estrutura do Projeto

```text
/
├── app.py          # Lógica principal da API (rotas)
├── config.py       # Configuração do Banco de Dados
├── templates/view
│   └── index.html  # Interface visual (Single View)
└── README.md       # Documentação
