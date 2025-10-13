-- merge salt table and login_password

alter table login_password add column salt varchar(32);

update login_password lp
set salt = s.salt 
from salt s 
where s.user_id = lp.user_id;

select * from login_password lp;
select * from salt;

drop table salt cascade;
