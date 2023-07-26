select code, name, continent, region, population
	from country
    where Population > 100000000
    order by Population ASC;
    
select name, continent, region
	from country
    where Population > 5000000
    order by Continent, region;
    
select code, name, continent, region, population
	from country
    where Population > 100000000
    order by 5 asc;
    
select *
	from country
    order by 4, 3, 2;