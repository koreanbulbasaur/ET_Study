use sakila;

select c.customer_id as 'Customer ID',
		c.first_name as 'First Name',
        c.last_name as 'Last Name',
        sum(amount) as 'Total Paid'
from sakila.payment p
	inner join customer c on
    p.customer_id = c.customer_id
group by c.customer_id
having sum(amount) > 180
order by sum(amount) desc;