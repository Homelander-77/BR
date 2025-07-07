docker image rm nginx;
docker build -t nginx -f ./services/nginx/Dockerfile .;
docker run --rm -it --name nginx --network net -p 80:80 -p 443:443 nginx
