import os

conf = dict(
    server_ip_address=str(os.getenv("SERVER_IP_ADDRESS")),
    server_port=int(os.getenv("SERVER_PORT", 8080)),
    server_max_con=5,
    server_rec_mes=1024,
    db_name=str(os.getenv("DB_NAME")),
    db_user=str(os.getenv("DB_USER")),
    db_password=str(os.getenv("DB_PASSWORD")),
    db_host=str(os.getenv("DB_HOST")),
    db_port=int(os.getenv("DB_PORT", 5432))
    )
