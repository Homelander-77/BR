docker image rm server;
docker build -t server ./backend;
docker run --rm -it --name server --network net -p 8080:8080 server
