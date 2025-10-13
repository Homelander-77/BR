sudo certbot certonly --standalone  -d bladerunner2049.online --config-dir ./services/nginx/cert/ --email eegorr120207@gmail.com --agree-tos --force-renewal;
sudo chown -R a1337:a1337 ./services/nginx/cert;

docker volume create hs4;
docker build -t postgres ./services/postgres/;
docker build -t nginx:1.0 -f ./services/nginx/Dockerfile .;
docker build -t server:1.0 ./backend;

sudo docker network create -d bridge net;
