sudo certbot certonly --standalone  -d bladerunner2049.online --config-dir ./services/nginx/cert/ --email eegorr120207@gmail.com --agree-tos --force-renewal;

sudo chown -R a1337:a1337 ./services/nginx/cert;
