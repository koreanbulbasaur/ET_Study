use world;

select a.continent, count(*) 전체건수, count(b.name) 도시건수
	from country a
    right outer join city b
    on a.code = b.CountryCode
    group by a.Continent;
    
select a.continent, count(*) 전체건수, count(b.name) 도시건수
	from city b
    right outer join country a
    on a.code = b.CountryCode
    group by a.Continent;