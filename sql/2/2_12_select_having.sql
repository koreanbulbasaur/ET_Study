use sakila;

select last_name, count(*)
	from sakila.actor
    group by last_name
    having count(*) > 3;
    
select *
	from country
    where Population > 100000000
    order by 5 asc
    limit 5;