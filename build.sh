source .env

sudo certbot certonly --standalone  -d $DOMAIN_NAME --config-dir ./services/nginx/cert/ --email $USER_EMAIL --agree-tos --force-renewal;
sudo chown -R $USER_NAME:$USER_NAME ./services/nginx/cert;

docker volume create postgres-data;
docker volume create redis-data;
docker build -t postgres:1.0 -f ./services/postgres/Dockerfile .;
docker build -t redis:1.0 -f ./services/redis/Dockerfile .;
docker build -t nginx:1.0 -f ./services/nginx/Dockerfile .;
docker build --network host -t server:1.0 ./backend;


sudo docker network create -d bridge net;
