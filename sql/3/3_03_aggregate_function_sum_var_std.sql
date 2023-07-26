select sum(population), var_pop(population), stddev_pop(population)
	from country
    where Continent = 'Europe';