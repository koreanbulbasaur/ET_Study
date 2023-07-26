use world;
select a.id, a.name, a.countrycode, b.code, b.name country_name,
		a.district, a.population
	from city a
    inner join country b
    on a.countrycode = b.code
    order by 1;
    
select b.name country_name, a.language, a.isofficial, a.percentage
	from countrylanguage a
    inner join country b
    on a.countrycode = b.code
    order by 1;
    
select b.name country_name, a.language, a.isofficial, a.percentage
	from countrylanguage a
    inner join country b
    on a.countrycode = b.code
    where a.countrycode = 'KOR'
    order by 1;
    
select a.code, a.name, a.continent, a.region, a.population, b.language
	from 		country a
    inner join	countrylanguage b
    on 			a.code = b.countrycode
    where 		a.code = 'KOR'
    order by 	1;
    
SELECT a.code, a.name, a.continent, a.region, a.population, b.language,
		c.name, c.district, c.population
	from		country a
    inner join	countrylanguage b
    on			a.code = b.countrycode
    inner join 	city c
    on 			a.code = c.countrycode
    where 		a.code = 'KOR'
    order by 	1;