use sakila;

select * from film;

select rating, max(replacement_cost), min(replacement_cost), sum(replacement_cost)
	from film
    where release_year = 2006
    group by rating
    order by 1;