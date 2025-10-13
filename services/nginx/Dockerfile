FROM nginx:1.26-alpine

COPY frontend/ /usr/share/nginx/
COPY services/psql/images/ /usr/share/nginx/images/
COPY services/nginx/nginx.conf services/nginx/mime.types  /etc/nginx
COPY services/nginx/cert/localhost.crt /etc/nginx/ssl/nginx-selfsigned.crt
COPY services/nginx/cert/localhost.key /etc/nginx/ssl/nginx-selfsigned.key
COPY services/nginx/repositories /etc/apk/repositories

RUN chmod 644 /etc/nginx/ssl/nginx-selfsigned.key; chown root:root /etc/nginx/ssl/nginx-selfsigned.key
