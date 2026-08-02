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

Docker (without docker-compose, with needable commands):

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Check installation of docker:

```
sudo docker run hello-world
```


Certbot (needs for HTTPS-certs):

```
sudo snap install --classic certbot
```

If you have old version of certbot, reinstall it:

```
sudo apt-get remove certbot
sudo snap install --classic certbot
```

## Configuration

Copy `.env.example` в `.env` (or create `.env` at the root) and fill it:

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

`build.sh`/`run.sh` use the `source .env` — everything is auto..

## Build & Run

```
sh build.sh
sh run.sh
```

`build.sh` create certificate through the certbot (put in `./services/nginx/cert/`), make docker images (postgres, redis, nginx, server) and create local network `net`.
`run.sh` start all the docker containers.

Scheme of database (`services/postgres/database.sql`, `films.sql`) auto make up when docker container starts - postgres-container.

## API

| Route         | Function                       |
|---------------|--------------------------------|
| `/login`      | enter, cookie session key      |
| `/reg`        | registration                   |
| `/check_auth` | validate check of cookie       |
| `/rec`        | films recommendations          |

## Copyright

2025 MoJlHu9l
