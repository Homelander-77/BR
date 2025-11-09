-- Creating table for list of films
create table films (
	id serial primary key,
	title varchar(255) not null,
	image_path varchar(255) unique,
	release smallint,
	description text,
	rating float, 
	price int,
	unique (title, release));

-- Data of film's table
insert into films (title, image_path, release, description, rating, price)
values ('Cars', '/images/cars.jpg', 2006,
	'On the way to the biggest race of his life, a hotshot rookie race car gets stranded in a rundown town and learns that winning isnt everything in life.', 
	7.3, 10);

insert into films (title, image_path, release, description, rating, price)
values ('Interstellar', '/images/interstellar.jpg', 2014,
	'When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.', 
	9.1, 15);

-- function for getting list of films
create or replace function get_recommendations()
returns json as $$
begin
	return (
		select json_agg(row_to_json(f))
		from films f
	);	
end
$$ language plpgsql;
