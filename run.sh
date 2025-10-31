docker run --rm --name postgres --network net -d -v postrges-data:/var/lib/postgresql/data \
-e POSTGRES_PASSWORD=$POSTGRES_PASSWORD \
-e POSTGRES_PORT=$POSTGRES_PORT \
-e POSTGRES_DB=$POSTGRES_DB \
-e POSTGRES_USER=$POSTGRES_USER \
postgres:1.0;

docker run --rm --name redis --network net -d -v redis-data:/data \
-e REDIS_HOST=$REDIS_HOST \
-e REDIS_PORT=$REDIS_PORT \
redis:1.0 redis-server --save 60 1;

docker run --rm -dit --name server --network net \
-e SERVER_HOST=$SERVER_HOST \
-e SERVER_PORT=$SERVER_PORT \
-e DB_NAME=$POSTGRES_DB \
-e DB_USER=$POSTGRES_USER \
-e DB_PASSWORD=$POSTGRES_PASSWORD \
-e DB_HOST=$POSTGRES_HOST \
-e DB_PORT=$POSTGRES_PORT \
server:1.0 \
& docker run --rm -dit --name nginx --network net \
-p $NGINX_HTTP_PORT:$NGINX_HTTP_PORT \
-p $NGINX_HTTPS_PORT:$NGINX_HTTPS_PORT \
-e DOMAIN_NAME=$DOMAIN_NAME \
nginx:1.0;
