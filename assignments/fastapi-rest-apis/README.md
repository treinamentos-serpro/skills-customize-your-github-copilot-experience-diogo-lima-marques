# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para consultar e gerenciar um catálogo de livros usando FastAPI. Você praticará rotas HTTP, parâmetros de caminho, validação de dados e respostas JSON.

## 📝 Tarefas

### 🛠️ Criar a API e consultar livros

#### Descrição
Prepare a aplicação FastAPI e implemente endpoints para listar os livros cadastrados e buscar um livro pelo ID. Os dados podem ficar em uma lista em memória; não é necessário usar banco de dados.

Para executar o código inicial, instale as dependências, renomeie `starter-code.py` para `main.py` e inicie o servidor:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

Abra `http://127.0.0.1:8000/docs` para testar os endpoints pela documentação interativa do FastAPI.

#### Requisitos
O programa concluído deve:

- Criar uma aplicação FastAPI com uma coleção inicial de livros, cada um com `id`, `title` e `author`.
- Implementar `GET /books` para retornar a coleção em JSON.
- Implementar `GET /books/{book_id}` para retornar o livro correspondente ou responder com HTTP 404 se ele não existir.

### 🛠️ Adicionar e remover livros

#### Descrição
Expanda a API para permitir que clientes adicionem livros validados no corpo da requisição e removam livros existentes. Continue usando a lista em memória como armazenamento.

#### Requisitos
O programa concluído deve:

- Definir um modelo Pydantic para validar `title` e `author` recebidos em uma requisição.
- Implementar `POST /books`, atribuir um ID ao novo livro e responder com HTTP 201.
- Implementar `DELETE /books/{book_id}` para remover um livro e responder com HTTP 404 se o ID não existir.
- Testar as quatro operações pela página `/docs` e confirmar que as respostas contêm os dados e códigos HTTP esperados.