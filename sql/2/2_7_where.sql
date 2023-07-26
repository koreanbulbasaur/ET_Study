use world;
select *
	from 	city
    where 	countrycode = 'KOR'
    or 		district like '%ong%';
    
select *
	from city
    where countrycode = 'KOR'
    and district in ('seoul', 'kyonggi');
    
select *
	from city
    where countrycode = 'KOR'
    and 2 > 3;