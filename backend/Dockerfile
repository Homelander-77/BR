FROM python:3.10-bookworm

WORKDIR /server

COPY resolv.conf /etc/resolv.conf

RUN apt-get update -o Acquire::Retries=5 -o Acquire::http::Timeout="30" \
 && apt-get install -y --no-install-recommends gcc libpq-dev \
 python3-dev libcrack2-dev cracklib-runtime \
 && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    --default-timeout=100 \
    psycopg2-binary python-dotenv cracklib


COPY src/  /server/
COPY resources/common_passwords.txt /var/data/

CMD python -m app.app
