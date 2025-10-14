docker build -t server:1.0 ./backend;
docker run --rm -it --name server --network net -p 8080:8080 --add-host=host.docker.internal:host-gateway server:1.0
