# 📘 Assignment: Book Catalog API with SQLite

## 🎯 Objective

Amplie uma API REST de catálogo de livros para armazenar dados de forma persistente usando SQLite. Você praticará consultas SQL parametrizadas, operações CRUD e respostas HTTP.

## 📝 Tasks

### 🛠️ Consultar livros no banco de dados

#### Descrição
Renomeie `starter-code.py` para `main.py`, instale as dependências e inicie a aplicação:

```bash
python -m pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

O código inicial cria `books.db` com uma tabela e dois livros de exemplo. Implemente os endpoints de consulta usando SQLite no lugar de uma lista em memória. Teste-os em `http://127.0.0.1:8000/docs`.

#### Requisitos
O programa concluído deve:

- Implementar `GET /books` para retornar todos os livros armazenados.
- Implementar `GET /books/{book_id}` para retornar um livro pelo ID.
- Responder com HTTP 404 quando o ID solicitado não existir.
- Usar parâmetros SQL (`?`) nas consultas que recebem valores externos.

### 🛠️ Criar e atualizar livros

#### Descrição
Implemente as operações para adicionar livros ao catálogo e atualizar os dados de um livro existente. Use os modelos Pydantic fornecidos para validar os dados recebidos.

#### Requisitos
O programa concluído deve:

- Implementar `POST /books` para inserir um livro no banco e retornar HTTP 201 com o livro criado e seu ID.
- Implementar `PUT /books/{book_id}` para atualizar título e autor de um livro existente.
- Responder com HTTP 404 ao tentar atualizar um ID inexistente.
- Manter os dados após encerrar e iniciar o servidor novamente.

### 🛠️ Remover livros e verificar persistência

#### Descrição
Implemente a remoção de livros e verifique o comportamento da API e do banco de dados nos casos de sucesso e de erro.

#### Requisitos
O programa concluído deve:

- Implementar `DELETE /books/{book_id}` e responder com HTTP 204 quando a remoção for concluída.
- Responder com HTTP 404 ao tentar remover um ID inexistente.
- Confirmar que um livro removido não aparece mais em `GET /books`.
- Testar as operações pela documentação interativa e confirmar que os registros sobrevivem a uma reinicialização do servidor.