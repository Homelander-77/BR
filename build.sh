# sudo certbot certonly --standalone  -d bladerunner2049.online --config-dir ./services/nginx/cert/ --email eegorr120207@gmail.com --agree-tos --force-renewal;
# sudo chown -R a1337:a1337 ./services/nginx/cert;

docker volume create hs3;
docker build -t postgres ./services/psql/;
docker build -t nginx -f ./services/nginx/Dockerfile .;
docker build -t server ./backend;

sudo docker network create -d bridge net;

docker run --name postgres -d -p 5432:5432 -v hs3:/var/lib/postgresql/data postgres;
# docker exec -i postgres psql -U postgres < ./services/psql/init.sql;
docker exec -i postgres psql -U boss -d boss < ./services/psql/database.sql;
docker stop postgres;
