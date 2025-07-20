FROM python:3.10-alpine
WORKDIR /server

COPY app.py login.py parser.py psql_config.py psql.py response.py requirements.txt common_passwords.txt password_check.py registration.py salt.py /server
COPY resolv.conf /etc/resolv.conf

EXPOSE 8080

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.yandex.ru\/mirrors/g' /etc/apk/repositories
RUN apk update && apk add --no-cache gcc musl-dev python3-dev libpq-dev cracklib cracklib-dev

# COPY ./librs/cracklib-2.8.18.tar.gz /tmp/
# RUN pip install --no-cache-dir /tmp/cracklib-2.8.18.tar.gz
RUN pip install --no-cache-dir cracklib
COPY ./librs/psycopg2-2.9.10.tar.gz /tmp/
RUN pip install --no-cache-dir /tmp/psycopg2-2.9.10.tar.gz


ENV PSQL_PASSWORD=your_password

CMD python app.py
