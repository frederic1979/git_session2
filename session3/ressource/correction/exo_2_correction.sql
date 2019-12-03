-- Affichage des marques des avions
select name from aircraft_brands;

-- Affichage des modèles d'avion Boeing
select name from aircraft_models where brand_idx = 2;

-- Affichage des villes couvertes et leurs pays
select countries.name as pays, cities.name as ville from cities
join countries on cities.country_idx = countries.id
order by pays, ville;

-- Affichage des avions AIRBUS ayant plus de 300 places triés par nb de places décroissant
select registration, seats_nb, brands.name, models.name from aircrafts
join aircraft_models models on aircrafts.model_idx = models.id
join aircraft_brands brands on models.brand_idx = brands.id
where seats_nb > 300 and brands.name = 'Airbus'
order by seats_nb desc;

-- Affichage des vols intérieurs
select country.name, fromcity.name, tocity.name from flights
join cities fromcity on flights.from_city = fromcity.id
join cities tocity on flights.to_city = tocity.id
join countries country on fromcity.country_idx = country.id
where fromcity.country_idx = tocity.country_idx;

-- Affichage des vols intérieurs plus longs que 5h
select country.name, fromcity.name, tocity.name, std_duration_sec / 60 / 60 as hour_duration from flights
join cities fromcity on flights.from_city = fromcity.id
join cities tocity on flights.to_city = tocity.id
join countries country on fromcity.country_idx = country.id
where fromcity.country_idx = tocity.country_idx and std_duration_sec > 60 * 60 * 5;

-- Affichage des 5 vols ayant les plus de personnel navigant
SELECT fromcity.name, tocity.name, emp_count.employee_count
from flights flights
         join (select flights_employees.flight_idx          flight_id,
                      count(flights_employees.employee_idx) employee_count
               from flights_employees
               group by flight_id
               order by count(flights_employees.employee_idx) desc
               limit 5) as emp_count on emp_count.flight_id = flights.id
         join cities fromcity on flights.from_city = fromcity.id
         join cities tocity on flights.to_city = tocity.id
order by emp_count.employee_count desc;

-- Alternative sans sous requête
select c1.name  as City_From,
       c2.name  as City_to,
       count(*) as Employees
from flights
         left join cities c1 on flights.from_city = c1.id
         left join cities c2 on flights.to_city = c2.id
         left join flights_employees fe on flights.id = fe.flight_idx
group by City_From,
         City_to
order by Employees desc
limit 5;


-- Affichage des personnes travaillant moins d'une heure dans la compagnie
select employees.first_name,
       employees.last_name,
       round(work_duration / 60.0 / 60.0, 2) hour_work
from employees
         join (select flights_employees.employee_idx employee_id,
                      sum(std_duration_sec)          work_duration
               from flights_employees
                        join flights f on flights_employees.flight_idx = f.id
               group by flights_employees.employee_idx
               having sum(std_duration_sec) < 3600)
    as work_duration on employees.id = employee_id
order by hour_work;


-- Affichage des durées des vols intérieur en utilisant intersect
select round(flight_duration / 60.0 / 60.0, 2), country_name
from (
         select std_duration_sec flight_duration, c1.name country_name
         from flights
                  join cities fromcity on flights.from_city = fromcity.id
             --join aircrafts on flights.aircraft_idx = aircrafts.id
                  join countries c1 on fromcity.country_idx = c1.id
         intersect
         select std_duration_sec flight_duration, c2.name country_name
         from flights
                  join cities tocity on flights.to_city = tocity.id
                  join countries c2 on tocity.country_idx = c2.id
         order by flight_duration desc
     ) as fdnfdn