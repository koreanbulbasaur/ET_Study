select max(population), min(population), avg(population)
	from country
    where Continent = 'Europe';