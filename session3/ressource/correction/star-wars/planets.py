import csv

filename = '/Users/jules/Downloads/star-wars/planets2.csv'

# Première lecture pour les climats
climates = {}

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    climate_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            climates_line = row[4].split(',')
            for climate_name in climates_line :
                climate_name = climate_name.strip()
                if climate_name not in climates:
                    climates[climate_name] = climate_id
                    print(
                        f'insert into climates (id, climate_name) values ({climate_id}, {climate_name});')
                    climate_id += 1

        line_count += 1


# Première lecture pour les climats
climates = {}
with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    climate_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            climates_line = row[4].split(',')
            for climate_name in climates_line:
                climate_name = climate_name.strip()
                if climate_name not in climates:
                    climates[climate_name] = climate_id
                    print(
                        f'insert into climates (id, climate_name) values ({climate_id}, {climate_name});')
                    climate_id += 1

        line_count += 1
