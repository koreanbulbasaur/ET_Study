use world;

select count(*), count(continent)
	from country;
    
select count(distinct continent)
	from country;