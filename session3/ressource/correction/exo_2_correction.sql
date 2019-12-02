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

