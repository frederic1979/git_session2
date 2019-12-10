import csv

######################
###### Planets #######
######################

sql_file = open('/Users/jules/Downloads/star-wars/output.sql', 'w')


planet_filename = '/Users/jules/Downloads/star-wars/planets2.csv'

# Première lecture pour les climats
climates = {}

with open(planet_filename) as csv_file:
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
                    sql_file.write(
                        f'insert into climates (id, climate_name) values ({climate_id}, \'{climate_name}\');\n')
                    climate_id += 1

        line_count += 1


# Seconde lecture pour les terrains
terrains = {}
with open(planet_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    terrain_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            terrains_line = row[6].split(',')
            for terrain_name in terrains_line:
                terrain_name = terrain_name.strip()
                if terrain_name not in terrains:
                    terrains[terrain_name] = terrain_id
                    sql_file.write(
                        f'insert into terrains (id, terrain_name) values ({terrain_id}, \'{terrain_name}\');\n')
                    terrain_id += 1

        line_count += 1

# Troisième lecture pour les planètes
planets = {}
with open(planet_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    planet_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            planet_name = row[0].strip()
            planet_rot_period = row[1].strip() if len(row[1].strip()) > 0 else 'null'
            planet_orb_period = row[2].strip() if len(row[2].strip()) > 0 else 'null'
            planet_diameter = row[3].strip() if len(row[3].strip()) > 0 else 'null'
            planet_climates = row[4].split(',')
            planet_gravity = row[5].strip() if len(row[5].strip()) > 0 else 'null'
            planet_terrains = row[6].split(',')
            planet_surface_water = row[7].strip() if len(row[7].strip()) > 0 else 'null'
            planet_population = row[8].strip() if len(row[8].strip()) > 0 else 'null'

            planets[planet_name] = planet_id

            sql_file.write(
                f'insert into planets(id, planet_name, rotation_period, orbital_period, diameter, gravity, surface_water, population) values ({planet_id}, \'{planet_name}\', {planet_rot_period}, {planet_orb_period}, {planet_diameter}, {planet_gravity}, {planet_surface_water}, {planet_population});\n')
            
            for planet_terrain in planet_terrains:
                sql_file.write(
                    f'insert into planet_terrains(planet_idx, terrain_idx) values ({planet_id}, {terrains[planet_terrain.strip()]});\n')
            
            for planet_climate in planet_climates:
                sql_file.write(
                    f'insert into planet_climates(planet_idx, climate_idx) values ({planet_id}, {climates[planet_climate.strip()]});\n')

            planet_id += 1
        line_count += 1


######################
###### Species #######
######################
species_filename = '/Users/jules/Downloads/star-wars/species2.csv'

# Première lecture pour les classifications
classifications = {}
with open(species_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    classification_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            classification_name = row[1].strip()
            if classification_name not in classifications:
                classifications[classification_name] = classification_id
                sql_file.write(
                    f'insert into classifications (id, classification_name) values ({classification_id}, \'{classification_name}\');\n')
                classification_id += 1

        line_count += 1


# Seconde lecture pour les designations
designations = {}
with open(species_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    designation_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            designation_name = row[2].strip()
            if designation_name not in designations:
                designations[designation_name] = designation_id
                sql_file.write(
                    f'insert into designations (id, designation_name) values ({designation_id}, \'{designation_name}\');\n')
                designation_id += 1

        line_count += 1

# Troisième lecture pour les couleurs
colors = {}
color_id = 1
with open(species_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            # skin, hair, eye
            colors_line = row[4].split(',') + row[5].split(',') + row[6].split(',')
            for color_name in colors_line:
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    sql_file.write(
                        f'insert into colors (id, color_name) values ({color_id}, \'{color_name}\');\n')
                    color_id += 1

        line_count += 1

# Quatrième lecture pour les langages
languages = {}
with open(species_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    language_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            language_name = row[8].strip()
            if language_name not in languages:
                languages[language_name] = language_id
                sql_file.write(
                    f'insert into languages (id, language_name) values ({language_id}, \'{language_name}\');\n')
                language_id += 1

        line_count += 1

# Cinquième lecture pour les espèces
species = {}
with open(species_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    species_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            species_name = row[0].strip()
            species_classification_idx = classifications[row[1].strip()] if len(row[1].strip()) > 0 else 'null'
            species_designation_idx = designations[row[2].strip()] if len(row[2].strip()) > 0 else 'null'
            species_average_height = row[3].strip() if len(row[3].strip()) > 0 else 'null'
            species_skin_colors = row[4].split(',')
            species_hair_colors = row[5].split(',')
            species_eye_colors = row[6].split(',')
            species_average_lifespan = row[7].strip() if len(row[7].strip()) > 0 else 'null'
            species_language_idx = languages[row[8].strip()] if len(row[8].strip()) > 0 else 'null'
            species_homeworld_idx = planets[row[9].strip()] if len(row[9].strip()) > 0 else 'null'

            species[species_name] = species_id
            
            sql_file.write(
                f'insert into species(id, species_name, average_height, average_lifespan, classification_idx, designation_idx, language_idx, home_world_idx) values ({species_id}, \'{species_name}\', {species_average_height}, {species_average_lifespan}, {species_classification_idx}, {species_designation_idx}, {species_language_idx}, {species_homeworld_idx});\n')

            for skin_color in species_skin_colors:
                sql_file.write(
                    f'insert into species_colors(species_idx, color_idx, color_type) values ({species_id}, {colors[skin_color.strip()]}, \'skin\');\n')

            for hair_color in species_hair_colors:
                sql_file.write(
                    f'insert into species_colors(species_idx, color_idx, color_type) values ({species_id}, {colors[hair_color.strip()]}, \'hair\');\n')

            for eye_color in species_eye_colors:
                sql_file.write(
                    f'insert into species_colors(species_idx, color_idx, color_type) values ({species_id}, {colors[eye_color.strip()]}, \'eye\');\n')

            species_id += 1
        line_count += 1


##########################
####### Characters #######
##########################

characters_filename = '/Users/jules/Downloads/star-wars/characters2.csv'

# Première lecture pour les couleurs
with open(characters_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            # skin, hair, eye
            colors_line = row[3].split(',') + row[4].split(',') + row[5].split(',')
            for color_name in colors_line:
                color_name = color_name.strip()
                if color_name not in colors:
                    colors[color_name] = color_id
                    sql_file.write(
                        f'insert into colors (id, color_name) values ({color_id}, \'{color_name}\');\n')
                    color_id += 1

        line_count += 1

# Deuxième lecture pour les genres
genders = {}
with open(characters_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    gender_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            gender_name = row[7].strip()
            if gender_name not in genders:
                genders[gender_name] = gender_id
                sql_file.write(
                    f'insert into genders (id, gender_name) values ({gender_id}, \'{gender_name}\');\n')
                gender_id += 1

        line_count += 1

# Troisième lecture pour les espèces
characters = {}
with open(characters_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    character_id = 1
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            character_name = row[0].strip()
            character_height = row[1].strip() if len(row[1].strip()) > 0 else 'null'
            character_mass = row[2].strip() if len(row[2].strip()) > 0 else 'null'
            character_hair_colors = row[3].split(',')
            character_skin_colors = row[4].split(',')
            character_eye_colors = row[5].split(',')
            character_birth_year = row[6].strip() if len(row[6].strip()) > 0 else 'null'
            character_gender_idx = genders[row[7].strip()] if len(row[7].strip()) > 0 else 'null'
            character_homeworld_idx = planets[row[8].strip()] if len(row[8].strip()) > 0 else 'null'
            character_species_idx = species[row[9].strip()] if len(row[9].strip()) > 0 else 'null'

            sql_file.write(
                f'insert into characters(id, full_name, height, mass, birthday, gender_idx, homeworld_idx, species_idx) values ({character_id}, \'{character_name}\', {character_height}, {character_mass}, \'{character_birth_year}\', {character_gender_idx}, {character_homeworld_idx}, {character_species_idx});\n')


            for skin_color in character_skin_colors:
                sql_file.write(
                    f'insert into characters_colors(character_idx, color_idx, color_type) values ({character_id}, {colors[skin_color.strip()]}, \'skin\');\n')

            for hair_color in character_hair_colors:
                sql_file.write(
                    f'insert into characters_colors(character_idx, color_idx, color_type) values ({character_id}, {colors[hair_color.strip()]}, \'hair\');\n')

            for eye_color in character_eye_colors:
                sql_file.write(
                    f'insert into characters_colors(character_idx, color_idx, color_type) values ({character_id}, {colors[eye_color.strip()]}, \'eye\');\n')

            character_id += 1
        line_count += 1

########################
####### Vehicles #######
########################
vehicles_filename = '/Users/jules/Downloads/star-wars/vehicles2.csv'

# Première lecture pour les classes de véhicules
vehicle_classes = {}
vehicle_class_id = 1
with open(vehicles_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            vehicle_class_name = row[10].strip()
            if vehicle_class_name not in vehicle_classes:
                vehicle_classes[vehicle_class_name] = vehicle_class_id
                sql_file.write(
                    f'insert into vehicle_classes (id, vehicle_class_name) values ({vehicle_class_id}, \'{vehicle_class_name}\');\n')
                vehicle_class_id += 1

        line_count += 1

# Seconde lecture pour les classes de constructeurs
manufacturers = {}
manufacturer_id = 1
with open(vehicles_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            manufacturer_names = row[2].split(',')
            for manufacturer_name in manufacturer_names:
                manufacturer_name = manufacturer_name.strip()
                if manufacturer_name not in manufacturers:
                    manufacturers[manufacturer_name] = manufacturer_id
                    sql_file.write(
                        f'insert into manufacturers (id, manufacturer_name) values ({manufacturer_id}, \'{manufacturer_name}\');\n')
                    manufacturer_id += 1

        line_count += 1

# Troisième lecture pour les véhicules
vehicles = {}
vehicle_id = 1
with open(vehicles_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    
    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            vehicle_name = row[0].strip()
            vehicle_model = row[1].strip() if len(row[1].strip()) > 0 else 'null'
            vehicle_manufacturers = row[2].split(',')
            vehicle_cost = row[3].strip() if len(row[3].strip()) > 0 else 'null'
            vehicle_length = row[4].strip() if len(row[4].strip()) > 0 else 'null'
            vehicle_max_speed = row[5].strip() if len(row[5].strip()) > 0 else 'null'
            vehicle_crew = row[6].strip() if len(row[6].strip()) > 0 else 'null'
            vehicle_passengers = row[7].strip() if len(row[7].strip()) > 0 else 'null'
            vehicle_cargo_cpty = row[8].strip() if len(row[8].strip()) > 0 else 'null'
            vehicle_consumables = row[9].strip() if len(row[9].strip()) > 0 else 'null'
            vehicle_class_idx = vehicle_classes[row[10].strip()] if len(row[10].strip()) > 0 else 'null'

            sql_file.write(
                f'insert into vehicles(id, vehicle_name, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class) values ({vehicle_id}, \'{vehicle_name}\', {vehicle_cost}, {vehicle_length}, {vehicle_max_speed}, {vehicle_crew}, {vehicle_passengers}, {vehicle_cargo_cpty}, \'{vehicle_consumables}\', {vehicle_class_idx});\n')
            
            for manufacturer in vehicle_manufacturers:
                sql_file.write(
                    f'insert into vehicle_manufacturers(vehicle_idx, manufacturer_idx) values ({vehicle_id}, {manufacturers[manufacturer.strip()]});\n')

            vehicle_id += 1
        line_count += 1

#########################
####### Vaisseaux #######
#########################
starships_filename = '/Users/jules/Downloads/star-wars/starships2.csv'

# Première lecture pour les classes de véhicules
with open(starships_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            vehicle_class_name = row[12].strip()
            if vehicle_class_name not in vehicle_classes:
                vehicle_classes[vehicle_class_name] = vehicle_class_id
                sql_file.write(
                    f'insert into vehicle_classes (id, vehicle_class_name) values ({vehicle_class_id}, \'{vehicle_class_name}\');\n')
                vehicle_class_id += 1

        line_count += 1

# Seconde lecture pour les classes de constructeurs
with open(starships_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            manufacturer_names = row[2].split(',')
            for manufacturer_name in manufacturer_names:
                manufacturer_name = manufacturer_name.strip()
                if manufacturer_name not in manufacturers:
                    manufacturers[manufacturer_name] = manufacturer_id
                    sql_file.write(
                        f'insert into manufacturers (id, manufacturer_name) values ({manufacturer_id}, \'{manufacturer_name}\');\n')
                    manufacturer_id += 1

        line_count += 1

# Troisème lecture pour les vaisseaux
with open(starships_filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        # On ignore la première ligne d'en-tête.
        if line_count != 0:
            vehicle_name = row[0].strip()
            vehicle_model = row[1].strip() if len(row[1].strip()) > 0 else 'null'
            vehicle_manufacturers = row[2].split(',')
            vehicle_cost = row[3].strip() if len(row[3].strip()) > 0 else 'null'
            vehicle_length = row[4].strip() if len(row[4].strip()) > 0 else 'null'
            vehicle_max_speed = row[5].strip() if len(row[5].strip()) > 0 else 'null'
            vehicle_crew = row[6].strip() if len(row[6].strip()) > 0 else 'null'
            vehicle_passengers = row[7].strip() if len(row[7].strip()) > 0 else 'null'
            vehicle_cargo_cpty = row[8].strip() if len(row[8].strip()) > 0 else 'null'
            vehicle_consumables = row[9].strip() if len(row[9].strip()) > 0 else 'null'
            vehicle_hyperdrive = row[10].strip() if len(row[10].strip()) > 0 else 'null'
            vehicle_mglt = row[11].strip() if len(row[11].strip()) > 0 else 'null'
            vehicle_class_idx = vehicle_classes[row[12].strip()] if len(row[12].strip()) > 0 else 'null'

            sql_file.write(
                f'insert into vehicles(id, vehicle_name, vehicle_model, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, vehicle_class) values ({vehicle_id}, \'{vehicle_name}\', \'{vehicle_model}\', {vehicle_cost}, {vehicle_length}, {vehicle_max_speed}, {vehicle_crew}, {vehicle_passengers}, {vehicle_cargo_cpty}, \'{vehicle_consumables}\', {vehicle_class_idx});\n')

            for manufacturer in vehicle_manufacturers:
                sql_file.write(
                    f'insert into vehicle_manufacturers(vehicle_idx, manufacturer_idx) values ({vehicle_id}, {manufacturers[manufacturer.strip()]});\n')

            sql_file.write(
                f'insert into starships(vehicle_idx, hyperdrive_rating, mglt) values ({vehicle_id}, {vehicle_hyperdrive}, {vehicle_mglt});\n')

            vehicle_id += 1
        line_count += 1

sql_file.close()
