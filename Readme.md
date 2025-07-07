# BladeRunner 2049

Films shop, about buying access for watching film 

## Programminng languages

- python
- typescript

## Backing services

- nginx
- postgres

## Install

My project was built due to docker so lots of modules not necessary to use. I use simple version of docker, not docker-compose. To install it, do:		

```
 sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Test your installation:

```
sudo docker run hello-world
```
Don't forget make for docker special user, all comands in *.sh start without sudo. 
For more information: info(https://docker-curriculum.com/)

Export ```PSQL_PASSWORD``` on your host, enter the password.
Config of psql have user and database named ```a1337```.
Host of postgres is 0.0.0.0 and port - 5432. (Look backend/psql_config.py)

Also you need to repair ```build.sh``` file, indicate your data in the last str.

Nginx for working with https requires certificates (domain name, expire and so on), certbot help to determine this problem:

```
sudo snap install --classic certbot
```

If you have had old versions of certbot, reinstall it:

```
sudo apt-get remove certbot
sudo snap install --classic certbot
```
All files will recive in ./services/nginx/cert/

## Run

Start the server in docker container, you just need to type some commands shown below:

```
sh build.sh
sh run.sh 
```

### Server
For backend you need python 3.10. Main libr for server is socket. Most of modules was writed with OOP.

### Services
Services contain nginx and postgres, nginx take js and html files to give them to client

## Copywright

2025 MoJlHu9l