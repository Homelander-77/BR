-- Creating table with users, id - primary key
create table users (
	uid serial primary key,
	firstname varchar(32) not null,
	lastname varchar(32) not null,
	created time default current_time,
	deleted time default NULL);



-- Creating table with login and password
create table credentials (
	uid integer primary key,
	login varchar(64) not null unique,
	password varchar(96) not null,
	salt varchar(32) not null,
	foreign key (uid) references users (uid) on delete cascade );


-- function for adding user
create or replace function add_user(
    in_firstname varchar(64),
    in_lastname varchar(64),
    in_login varchar(64),
    in_password varchar(96),
    in_salt varchar(32)
)
returns int4
as $$
declare
    user_id integer;
begin
	insert into users (firstname, lastname)
	values (in_firstname, in_lastname)
	returning id into user_id;

	insert into credentials (uid, login, password, salt)
       	values (user_id, in_login, in_password, in_salt);

       	return user_id; 
end;
$$ language plpgsql;


-- check of login existing
create or replace function check_user_existing(in_login varchar(64))
returns boolean
as $$
begin
	if exists (select login
	   	   from credentials
		    where login=in_login
		  ) then 
		return false;
	end if;
	return true;
end;
$$ language plpgsql;


-- get password using only login
create or replace function get_password_by_login(in_login varchar(64))
returns varchar(64)
as $$
declare
	password varchar(64);
begin
	select c.password into password 
	from credentials c 
	where c.login=in_login;
	
	return password;
end;
$$ language plpgsql;


-- get salt using only login
create or replace function get_salt_by_login(in_login varchar(64))
returns varchar(64)
as $$
declare
	salt varchar(64);
begin
	select c.salt into salt from credentials c
	where c.login=in_login;	
	return salt;
end;
$$ language plpgsql;


-- get user_id using only login
create or replace function get_user_id_by_login(in_login varchar(64))
returns int4
as $$
declare
	id int4;
begin
	select uid into id from 
	credentials c 
	where c.login=in_login;

	if id is NULL then
		return 0;
	else 
		return id;
	end if; 
end;
$$ language plpgsql;

