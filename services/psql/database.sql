-- Creating table with users, id - primary key
create table users (id serial primary key, firstname varchar(32) not null, lastname varchar(32) not null);

-- Creating table with login and password
create table login_password(id serial, login varchar(64) not null unique, password varchar(64) not null, foreign key (id) references users (id));

create or replace function check_authentication(in_login varchar(64), in_password varchar(64))
returns boolean
as $$
declare
	dlogin varchar(64);
	dpassword varchar(64);
begin
	select lp.login, lp.password into strict dlogin, dpassword from login_password as lp where lp.login = in_login and lp.password=in_password;
	RAISE NOTICE '%, %', dlogin, dpassword; 
	if in_login = dlogin and in_password = dpassword then 
		return true;
	else
		return false;
	end if;
exception
	when no_data_found then
		return false;
	when too_many_rows then
		return false;
end
$$ language plpgsql;

-- add user
create or replace function add_user(
    in_firstname varchar(64),
    in_lastname varchar(64),
    in_login varchar(64),
    in_password varchar(64)
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

        COMMIT;
        return TRUE; 

    exception when others then
        ROLLBACK;
        raise notice 'Error: %', SQLERRM;
        return FALSE; 
    end;
end;
$$ language plpgsql;
