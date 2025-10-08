FROM python:3.9-alpine
WORKDIR /server

EXPOSE 8080

RUN apk update && apk add --no-cache gcc musl-dev python3-dev libpq-dev cracklib cracklib-dev

RUN pip install --no-cache-dir cracklib psycopg2 python-dotenv

COPY repositories /etc/apk/repositories
COPY resolv.conf /etc/resolv.conf
COPY src/  /server/
COPY resources/common_passwords.txt /var/data/

CMD python app.py
