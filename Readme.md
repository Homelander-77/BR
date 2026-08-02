# BladeRunner 2049

Films shop — sells access to watch films.

## Stack

- Backend: Python 3.10, raw sockets (no framework), OOP
- Frontend: vanilla JS/HTML/CSS
- Postgres — main storage
- Redis — sessions/cookies
- Nginx — reverse proxy + static files (js/html) + TLS

## Project structure

```
backend/
  src/
    app.py          # entry point
    server.py        # socket-based HTTP server
    config.py
    routes/           # HTTP handlers: login, registration, recommendations
    db/               # Postgres/Redis clients
    utils/            # HTTP request/response, cookies, password hashing
frontend/             # static pages: index, login, reg
services/             # Services for docker containers
  nginx/
  postgres/
  redis/
```

## Prerequisites

Docker (без docker-compose, простые команды):

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Проверка установки:

```
sudo docker run hello-world
```

Добавь себя в группу docker, чтобы не писать `sudo` перед *.sh:
https://docker-curriculum.com/

Certbot (нужен для HTTPS-сертификатов):

```
sudo snap install --classic certbot
```

Если стоит старая версия — снеси и поставь заново:

```
sudo apt-get remove certbot
sudo snap install --classic certbot
```

## Configuration

Скопируй `.env.example` в `.env` (или создай `.env` в корне) и заполни:

```
USER_NAME=
USER_EMAIL=
DOMAIN_NAME=
SERVER_HOST=
SERVER_PORT=
POSTGRES_USER=
POSTGRES_DB=
POSTGRES_HOST=
POSTGRES_PORT=
POSTGRES_PASSWORD=
REDIS_HOST=
REDIS_PORT=
NGINX_HTTP_PORT=
NGINX_HTTPS_PORT=
```

`build.sh`/`run.sh` сами подхватывают эти переменные через `source .env` — руками ничего экспортировать не нужно.

## Build & Run

```
sh build.sh
sh run.sh
```

`build.sh` выпускает сертификаты через certbot (кладёт в `./services/nginx/cert/`), собирает docker-образы (postgres, redis, nginx, server) и создаёт сеть `net`.
`run.sh` поднимает все контейнеры в этой сети.

Схема базы (`services/postgres/database.sql`, `films.sql`) накатывается автоматически при первом старте postgres-контейнера.

## API

| Route         | Назначение                    |
|---------------|--------------------------------|
| `/login`      | вход, выдача cookie-сессии    |
| `/reg`        | регистрация                   |
| `/check_auth` | проверка валидности cookie    |
| `/rec`        | список рекомендаций фильмов   |

## Copyright

2025 MoJlHu9l
