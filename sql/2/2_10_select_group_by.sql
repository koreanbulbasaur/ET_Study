use sakila;

select last_name
	from sakila.actor
    group by last_name;
    
select last_name, count(*)
	from sakila.actor
    group by last_name;
    
select last_name, first_name
	from sakila.actor
    where first_name like '%tom%'
    group by 1, 2;
    
select last_name, count(*)
	from sakila.actor
    group by last_name
    order by count(*) desc;