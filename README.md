# FastAPI com Docker e Alembic

Este é um projeto de exemplo que demonstra como configurar uma aplicação FastAPI com Docker e Alembic para gerenciar migrações de banco de dados. A aplicação inclui uma API básica para gerenciar atletas, com endpoints para criar, ler, atualizar e excluir atletas.

## Estrutura do Projeto

```
fastapi-docker/
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
├── alembic.ini
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── Dockerfile
├── requirements.txt
└── venv/
```

## Configuração e Execução do Projeto

### Pré-requisitos

- Python 3.11+
- Docker
- Docker Compose

### Passos para Configuração

1. Clone o repositório:

```bash
git clone https://github.com/clerdomy/fastapi-docker.git
cd fastapi-docker
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Configure o banco de dados no `alembic.ini`:

Atualize a string de conexão do banco de dados no arquivo `alembic.ini` conforme necessário.

5. Inicialize o Alembic:

```bash
alembic init alembic
```

6. Crie e aplique a migração inicial:

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### Executar a Aplicação

#### Usando Docker

1. Construa a imagem Docker:

```bash
docker build -t fastapi-docker .
```

2. Execute o contêiner:

```bash
docker run -d --name fastapi-container -p 8000:8000 fastapi-docker
```

#### Usando Python Localmente

1. Execute a aplicação:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Endpoints da API

- `POST /atleta/` - Cria um novo atleta
- `GET /atleta/` - Lista atletas com paginação
- `GET /atleta/all` - Lista todos os atletas
- `GET /atleta/{id}` - Obtém detalhes de um atleta específico
- `PUT /atleta/{id}` - Atualiza um atleta específico
- `DELETE /atleta/{id}` - Exclui um atleta específico

### Documentação

A documentação automática da API gerada pelo FastAPI está disponível em:

- Swagger: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

### Contribuição

Sinta-se à vontade para abrir issues e pull requests para melhorar este projeto.

### Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```

Esse `README.md` fornece uma visão geral do projeto, instruções de configuração e execução, além de detalhes sobre os endpoints da API. Certifique-se de ajustar o conteúdo conforme necessário para refletir com precisão o seu projeto.

Referências
FastAPI: https://fastapi.tiangolo.com/

Pydantic: https://docs.pydantic.dev/latest/

SQLAlchemy: https://docs.sqlalchemy.org/en/20/

Alembic: https://alembic.sqlalchemy.org/en/latest/

Fastapi-pagination: https://uriyyo-fastapi-pagination.netlify.app/