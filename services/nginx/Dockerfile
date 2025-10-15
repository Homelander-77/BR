FROM nginx:1.26-alpine

COPY frontend/ /usr/share/nginx/
COPY frontend/images/ /usr/share/nginx/images/
COPY services/nginx/nginx.conf services/nginx/mime.types  /etc/nginx
COPY services/nginx/cert/archive /etc/letsencrypt/archive
COPY services/nginx/cert/live/ /etc/letsencrypt/live

RUN chmod 644 /etc/nginx/ssl/nginx-selfsigned.key; chown root:root /etc/nginx/ssl/nginx-selfsigned.key
