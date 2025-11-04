import os

server_conf = dict(
    host=str(os.getenv("SERVER_HOST", "localhost")),
    port=int(os.getenv("SERVER_PORT", 8080)),
    max_con=5,
    rec_mes=1024,
    )

db_conf = dict(
    name=str(os.getenv("DB_NAME")),
    user=str(os.getenv("DB_USER")),
    password=str(os.getenv("DB_PASSWORD", "qwerty")),
    host=str(os.getenv("DB_HOST")),
    port=int(os.getenv("DB_PORT", 5432)),
    )

redis_conf = dict(
    host=str(os.getenv("REDIS_HOST")),
    port=str(os.getenv("REDIS_PORT")),
    )

path_conf = dict(
    common_passwords='/var/data/common_passwords.txt',
    )
