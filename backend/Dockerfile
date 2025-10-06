FROM python:3.9-alpine
WORKDIR /server

COPY app.py login.py parser.py psql_config.py psql.py response.py requirements.txt common_passwords.txt password_check.py registration.py salt.py cookie.py /server
COPY resolv.conf /etc/resolv.conf

EXPOSE 8080

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.yandex.ru\/mirrors/g' /etc/apk/repositories
RUN apk update && apk add --no-cache gcc musl-dev python3-dev libpq-dev cracklib cracklib-dev

RUN pip install --no-cache-dir cracklib psycopg2-2.9.10

ENV PSQL_PASSWORD=your_password

CMD python app.py
