create role postgres superuser login password 'raketa';

create user boss with password 'raketa';
create database boss owner boss;
grant all privileges on database boss to boss;
