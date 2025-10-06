FROM python:3.9-alpine
WORKDIR /server

EXPOSE 8080

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.yandex.ru\/mirrors/g' /etc/apk/repositories
RUN apk update && apk add --no-cache gcc musl-dev python3-dev libpq-dev cracklib cracklib-dev

RUN pip install --no-cache-dir cracklib psycopg2-2.9.10

ENV PSQL_PASSWORD=your_password

COPY src/  /server/
COPY resources/common_passwords.txt /var/data/
COPY resolv.conf /etc/resolv.conf


CMD python app.py
