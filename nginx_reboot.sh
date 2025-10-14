docker build -t nginx:1.0 -f ./services/nginx/Dockerfile .;
docker run --rm -it --name nginx --network net -p 80:80 -p 443:443 nginx:1.0
