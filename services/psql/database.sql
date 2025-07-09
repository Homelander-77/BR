-- Creating table with users, id - primary key
create table users (id serial primary key, firstname varchar(32) not null, lastname varchar(32) not null);

-- Creating table with login and password
create table login_password(user_id integer primary key, login varchar(64) not null unique, password varchar(64) not null, foreign key (user_id) references users (id) on delete cascade);

-- Creating table with salt
create table salt(user_id integer primary key, salt varchar(64) not null, foreign key (user_id) references login_password (user_id) on delete cascade);

create or replace function add_user(
    in_firstname varchar(64),
    in_lastname varchar(64),
    in_login varchar(64),
    in_password varchar(64),
    in_salt varchar(64)
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

        COMMIT;
        return TRUE; 

    exception when others then
        ROLLBACK;
        raise notice 'Error: %', SQLERRM;
        return FALSE; 
    end;
end;
$$ language plpgsql;

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


create or replace function get_salt_by_login(in_login varchar(64))
returns varchar(64)
as $$
declare
	salt varchar(64);
begin
	select s.salt into salt from login_password lp 
	left join salt s on lp.id=s.user_id
	where lp.login=in_login;
	
	return salt;
end;
$$ language plpgsql;
