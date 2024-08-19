# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def damage_converter(damage_list):
  new_damage_list = []
  for damage in damage_list:
    if damage == "Damages not recorded":
        new_damage_list.append(damage)
    for char in damage:
      if char == "M":
          float_damage = damage.replace("M", "")
          result = float(float_damage) * 1000000
          new_damage_list.append(result)


      if char == "B":
          float_damage = damage.replace("B", "")
          result = float(float_damage) * 1000000000
          new_damage_list.append(result)
  return new_damage_list



print(damage_converter(damages))
converted_damages = damage_converter(damages)





# write your construct hurricane dictionary function here:
def construct_hurricane(dict_names, dict_months, dict_years, dict_max_sustained_winds,
                        dict_areas_affected, dict_damages,
                        dict_deaths):
    new_dict = {}
    for name in dict_names:
        index = dict_names.index(name)
        new_dict[dict_names[index]] = {"name": dict_names[index], "month": dict_months[index], "year": dict_years[index],
                                       "max sustained wind": dict_max_sustained_winds[index]
                                       , "area affected": dict_areas_affected[index], "damage": dict_damages[index], "death":dict_deaths[index]}
    return new_dict

print(construct_hurricane(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths))
constructed_hurricane = construct_hurricane(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)





# write your construct hurricane by year dictionary function here:
def construct_hurricane_by_year(dict_names, dict_months, dict_years, dict_max_sustained_winds,
                                dict_areas_affected, dict_damages,
                        dict_deaths):
    new_dict = {}
    for year in dict_years:
        index = dict_years.index(year)
        new_dict[dict_years[index]] = {"name": dict_names[index], "month": dict_months[index],
                                       "year": dict_years[index], "max sustained wind": dict_max_sustained_winds[index]
            , "area affected": dict_areas_affected[index], "damage": dict_damages[index], "death": dict_deaths[index]}
    return new_dict


print(construct_hurricane_by_year(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths))



# write your count affected areas function here:
def count_affected_areas(area_list):
    new_dict = {}
    new_list = []
    for area_affected in area_list:
        for area in area_affected:
            new_list.append(area)
    for element in new_list:
        the_count = new_list.count(element)
        new_dict[element] = the_count
    return new_dict



print(count_affected_areas(areas_affected))

area_count = count_affected_areas(areas_affected)



# write your find most affected area function here:
def most_area_affected(area):
    largest_value = float('-inf')
    corresponding_key = ""
    for key, value in area.items():
        if value > largest_value:
            largest_value = value
            corresponding_key = key
    return "The area most affected by hurricanes is " + corresponding_key
print(most_area_affected(area_count))






# write your greatest number of deaths function here:
def greatest_number_of_deaths(deaths_list, hurricane_list):
    largest_death = float('-inf')
    corresponding_hurricane = ""
    for death, hurricane in zip(deaths_list, hurricane_list):
        if death > largest_death:
            largest_death = death
            corresponding_hurricane = hurricane
    return "The {hurricane} caused {deaths} number of deaths.".format(hurricane=corresponding_hurricane,
                                                                      deaths=largest_death)

print(greatest_number_of_deaths(deaths, names))






# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricane_list, death_list):
    new_dict = {}
    mortality_0 = []
    mortality_1 = []
    mortality_2 = []
    mortality_3 = []
    mortality_4 = []
    mortality_5 = []
    for death, hurricane in zip(death_list, hurricane_list):
        if death == 0:
            mortality_0.append(constructed_hurricane[hurricane])

        elif death <= 100:
            mortality_1.append(constructed_hurricane[hurricane])

        elif death <= 500:
            mortality_2.append(constructed_hurricane[hurricane])

        elif death <= 1000:
            mortality_3.append(constructed_hurricane[hurricane])

        elif death <= 10000:
            mortality_4.append(constructed_hurricane[hurricane])

        elif death > 10000:
            mortality_5.append(constructed_hurricane[hurricane])


    new_dict.update({0: mortality_0, 1: mortality_1, 2: mortality_2, 3: mortality_3, 4: mortality_4, 5: mortality_5})
    print(mortality_2)

print(categorize_by_mortality(names, deaths))
new_damage_list = []
for damage in converted_damages:
    if damage != "Damages not recorded":
        new_damage_list.append(damage)



# write your greatest damage function here:
def greatest_damage(damage_list, hurricane_list):
    largest_damage = float('-inf')
    corresponding_hurricane = ""
    for damage, hurricane in zip(new_damage_list, hurricane_list):
        if damage > largest_damage:
            largest_damage = damage
            corresponding_hurricane = hurricane

    return "The {hurricane} hurricane cost {cost}".format(hurricane=corresponding_hurricane, cost=largest_damage)

print(greatest_damage(converted_damages, names))




# write your catgeorize by damage function here:
def categorize_by_damage(hurricane_list, damage_list):
    new_dict = {}
    mortality_0 = []
    mortality_1 = []
    mortality_2 = []
    mortality_3 = []
    mortality_4 = []
    mortality_5 = []
    for damage, hurricane in zip(new_damage_list, hurricane_list):
        if damage == 0:
            mortality_0.append(constructed_hurricane[hurricane])

        elif damage <= 100000000:
            mortality_1.append(constructed_hurricane[hurricane])

        elif damage <= 1000000000:
            mortality_2.append(constructed_hurricane[hurricane])

        elif damage <= 10000000000:
            mortality_3.append(constructed_hurricane[hurricane])

        elif damage <= 50000000000:
            mortality_4.append(constructed_hurricane[hurricane])

        elif damage > 500000000000:
            mortality_5.append(constructed_hurricane[hurricane])

    new_dict.update({0: mortality_0, 1: mortality_1, 2: mortality_2, 3: mortality_3, 4: mortality_4, 5: mortality_5})
    print(new_dict)


categorize_by_damage(names, converted_damages)