docker run --rm --name postgres --network net -d -p 5432:5432 -v hs3:/var/lib/postgresql/data postgres:latest;
docker run --rm -dit --name server --network net -p 8080:8080 --add-host=host.docker.internal:host-gateway server & docker run --rm -dit --name nginx --network net -p 80:80 -p 443:443 nginx;
