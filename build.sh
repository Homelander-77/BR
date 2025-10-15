source .env

sudo certbot certonly --standalone  -d $DOMAIN_NAME --config-dir ./services/nginx/cert/ --email $USER_EMAIL --agree-tos --force-renewal;
sudo chown -R $USER_NAME:$USER_NAME ./services/nginx/cert;

docker volume create hs4;
docker build -t postgres:1.0 -f ./services/postgres/Dockerfile .;
docker build -t nginx:1.0 -f ./services/nginx/Dockerfile .;
docker build -t server:1.0 ./backend;

sudo docker network create -d bridge net;
