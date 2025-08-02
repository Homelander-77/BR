# a=$(docker images --filter=reference="server:1.0" -q)
docker build -t server:1.0 ./backend;
# [ -n "$a" ] && docker image rm $a;
# sleep 1;
docker run --rm -it --name server --network net -p 8080:8080 --add-host=host.docker.internal:host-gateway server:1.0
