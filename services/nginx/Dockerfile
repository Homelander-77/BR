FROM nginx:1.26-alpine

COPY frontend/404.html frontend/login.html frontend/index.html frontend/index.js frontend/login.js frontend/reg.js frontend/reg.html frontend/cookieCheck.js frontend/loginLoader.js /usr/share/nginx
COPY  services/psql/images/* /user/share/nginx/images
COPY services/nginx/nginx.conf /etc/nginx
COPY services/nginx/cert/nginx-selfsigned.crt /etc/nginx/ssl/nginx-selfsigned.crt
COPY services/nginx/cert/nginx-selfsigned.key /etc/nginx/ssl/nginx-selfsigned.key
COPY services/nginx/repositories /etc/apk/repositories

RUN chmod 644 /etc/nginx/ssl/nginx-selfsigned.key; chown root:root /etc/nginx/ssl/nginx-selfsigned.key
