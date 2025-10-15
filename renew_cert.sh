sudo certbot certonly --standalone  -d $DOMAIN_NAME --config-dir ./services/nginx/cert/ --email $USER_EMAIL --agree-tos --force-renewal;

sudo chown -R $USER_NAME:$USER_NAME ./services/nginx/cert;
