# Monitor DevOps

API desenvolvida em Python e Flask como parte da minha jornada de estudos em DevOps.

## Tecnologias

- Python
- Flask
- Docker
- Docker Compose

## Funcionalidades

- Endpoint `/status` para consultar o status da aplicação.
- Endpoint `/health` para verificar a saúde da API.
- HEALTHCHECK do Docker para monitoramento automático.

## Como executar

É necessário ter o Docker instalado e funcionando.

Na pasta do projeto, execute:

```bash
docker compose up -d --build
```

Acesse a aplicação em:

http://localhost:5002/status

Para verificar a saúde da API:

http://localhost:5002/health

## Comandos úteis

Verificar os containers:

```bash
docker compose ps
```

Consultar os logs:

```bash
docker compose logs api
```

Parar a aplicação:

```bash
docker compose down
```

## Próximas etapas

- CI/CD com GitHub Actions
- Implantação na AWS
- Infraestrutura com Terraform
- Kubernetes
- Observabilidade