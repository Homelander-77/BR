-- Creating table with users, id - primary key
create table users (
	id serial primary key,
	firstname varchar(32) not null,
	lastname varchar(32) not null );

-- Creating table with login and password
create table login_password (
	user_id integer primary key,
	login varchar(64) not null unique,
	password varchar(96) not null,
	foreign key (user_id) references users (id) on delete cascade );

-- Creating table with salt for password
create table salt (
	user_id integer primary key,
	salt varchar(32) not null,
	foreign key (user_id) references login_password (user_id) on delete cascade );

-- Creating table with cookie
create table cookie (
	user_id integer primary key,
	cookie varchar(36) not null,
	expire varchar(64) not null,
	foreign key (user_id) references users (id) on delete cascade );

-- function for adding user
create or replace function add_user(
    in_firstname varchar(64),
    in_lastname varchar(64),
    in_login varchar(64),
    in_password varchar(96),
    in_salt varchar(32), 
    in_cookie varchar(36),
    in_expire varchar(64)
)
returns boolean
as $$
declare
    user_id integer;
begin
    begin
        INSERT INTO users (firstname, lastname)
        VALUES (in_firstname, in_lastname)
        RETURNING id INTO user_id;

        INSERT INTO login_password (user_id, login, password)
        VALUES (user_id, in_login, in_password);
			
		INSERT INTO salt (user_id, salt)
        VALUES (user_id, in_salt);
		
		INSERT INTO cookie(user_id, cookie, expire)
		VALUES (user_id, in_cookie, in_expire);		

        return TRUE; 

    exception when others then
        raise notice 'Error: %', SQLERRM;
        return FALSE; 
    end;
end;
$$ language plpgsql;


create or replace function set_cookie(in_login varchar(64), in_cookie varchar(36), in_expire varchar(64))
returns boolean
as $$
declare
	in_id integer;
begin
	select user_id into in_id from login_password where login = in_login;
	if in_id is null then
		return false;
	end if;
	insert into cookie (user_id, cookie, expire) values (in_id, in_cookie, in_expire)
	on conflict(user_id) do update 
	set cookie=excluded.cookie, expire=excluded.expire;
	return true;
end;
$$ language plpgsql;

select * from set_cookie('eeggorr120207@outlook.com', '123', '12');
select * from cookie;

create or replace function get_cookie_expire(in_cookie text)
returns text
as $$
declare
	expire_out varchar(64);
begin
	select expire into expire_out from cookie where cookie = in_cookie;
	if expire_out is null then
		return '';
	end if;
	return expire_out;
end;
$$ language plpgsql;


-- get password using only login
create or replace function get_password_by_login(in_login varchar(64))
returns varchar(64)
as $$
declare
	password varchar(64);
begin
	select lp.password into password from login_password lp 
	where lp.login=in_login;
	
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
	select s.salt into salt from login_password lp 
	left join salt s on lp.user_id=s.user_id
	where lp.login=in_login;
	
	return salt;
end;
$$ language plpgsql;
