use world;

SELECT b.name country_name, a.language, a.isofficial, a.percentage
	from 		countrylanguage a, country b
    where 		a.CountryCode = b.Code
    and			a.CountryCode = 'KOR'
    order by	1;
    
SELECT a.code, a.name, a.continent, a.region, a.population, b.language,
		c.name, c.district, c.population
	from		country a, countrylanguage b, city c
    where 		a.code = b.CountryCode
    and 		a.code = c.CountryCode
    and 		a.Code = 'KOR'
    order by	1;