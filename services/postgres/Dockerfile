FROM postgres:14
ENV POSTGRES_PASSWORD '123'
ENV POSTGRES_PORT 5432
ENV POSTGRES_DB boss
ENV POSTGRES_USER boss

COPY ./services/postgres/database.sql ./services/postgres/films.sql /docker-entrypoint-initdb.d/