use world;

select 		continent
	from 	country
    group by Continent;
    
select 			continent, region
from 			country
group by		continent, region
order by		1, 2;

select		continent, region
from		country
group by	1, 2
order by	1, 2;

SELECT continent, region, governmentform
 FROM country
 GROUP BY 1, 2, 3
 ORDER BY 1, 2;
 
select substring(district, 1, 2) do
	from city
    where CountryCode = 'KOR'
    group by substring(district, 1, 2)
    order by 1;