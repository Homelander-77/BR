import os

conf = dict(
    server_ip_address=str(os.getenv("SERVER_IP_ADDRESS")),
    server_port=int(os.getenc("SERVER_PORT")),
    server_max_con=5,
    server_rec_mes=1024,
    db_name=str(os.getenc("DB_NAME")),
    db_user=str(os.getenc("DB_USER")),
    db_password=str(os.getenc("DB_PASSWORD")),
    db_host=str(os.getenc("DB_HOST")),
    db_port=int(os.getenv("DB_PORT"))
    )
