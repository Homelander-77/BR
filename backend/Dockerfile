FROM python:3.9-alpine

WORKDIR /server

COPY repositories /etc/apk/repositories

RUN apk update && apk add --no-cache gcc musl-dev cracklib-dev

RUN pip install --no-cache-dir cracklib psycopg2-binary python-dotenv

COPY resolv.conf /etc/resolv.conf
COPY src/  /server/
COPY resources/common_passwords.txt /var/data/

CMD python -m app.app
