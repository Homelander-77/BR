docker run --rm --name postgres --network net -d -v hs4:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
-e POSTGRES_PORT=$POSTGRES_PORT \
-e POSTGRES_DB=$POSTGRES_DB \
-e POSTGRES_USER=$POSTGRES_USER \
postgres:1.0;
docker run --rm -dit --name server --network net\
-e SERVER_HOST=0.0.0.0 \
-e SERVER_PORT=8080 \
-e DB_NAME=$POSTGRES_DB \
-e DB_USER=$POSTGRES_USER \
-e DB_PASSWORD=$POSTGRES_PASSWORD \
-e DB_HOST=postgres \
-e DB_PORT=$POSTGRES_PORT \
server:1.0 \
& docker run --rm -dit --name nginx --network net -p 80:80 -p 443:443 \
-e DOMAIN_NAME=$DOMAIN_NAME \
nginx:1.0;
