FROM postgres:14
ENV POSTGRES_PASSWORD $POSTGRES_PASSWORD
ENV POSTGRES_PORT $POSTGRES_PORT
ENV POSTGRES_DB $POSTGRES_DB
ENV POSTGRES_USER $POSTGRES_USER

COPY services/postgres/database.sql services/postgres/films.sql /docker-entrypoint-initdb.d/