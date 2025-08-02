# a=$(docker images --filter=reference="nginx" -q)
docker build -t nginx:1.0 -f ./services/nginx/Dockerfile .;
# [ -n "$a" ] && docker image rm $a;
# sleep 1;
docker run --rm -it --name nginx --network net -p 80:80 -p 443:443 nginx:1.0
