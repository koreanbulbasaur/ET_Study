use world;
select *
	from city
    where countrycode = 'KOR';
    
select *
	from city
    where countrycode in ('KOR', 'JPN');
    
select *
	from city
    where Population between 100000 and 150000;
    
select *
	from city
    where countrycode = 'KOR'
	and district like 'K%';
    
select *
	from city
    where countrycode = 'KOR'
    and district like '%ong%';
    
select *
	from city
    where countrycode = 'JPN'
    and name like 'A%';