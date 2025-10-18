FROM nginx:1.26-alpine

COPY frontend/ /usr/share/nginx/
COPY frontend/images/ /usr/share/nginx/images/
COPY services/nginx/nginx.conf.template /etc/nginx/templates/nginx.conf.template
COPY services/nginx/mime.types  /etc/nginx
COPY services/nginx/cert/archive /etc/letsencrypt/archive
COPY services/nginx/cert/live/ /etc/letsencrypt/live

CMD envsubst '$DOMAIN_NAME' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'





