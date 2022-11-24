names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 
'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 
'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 
'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 
'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 
'October', 'August', 'September', 'October', 'September', 'September', 'October']

years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 
1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 
190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], 
['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], 
['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], 
['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], 
['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], 
['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], 
['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], 
['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], 
['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], 
['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], 
['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], 
['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], 
['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], 
['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], 
['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', 
'306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', 
'10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#Updates damage values
def updated_damages_funct(damages):
    conversion = {"M": 1000000,
              "B": 1000000000}

    updated_damage = list()
    for damage in damages:
        if damage == 'Damages not recorded':
            updated_damage.append(damage)
        if damage.find("M") != -1:
            updated_damage.append(float(damage[0:damage.find("M")]) * conversion["M"])
        if damage.find("B") != -1:
            updated_damage.append(float(damage[0:damage.find("B")]) * conversion["B"])
    return updated_damage

updated_damages = updated_damages_funct(damages)


#Creates dictionary of all data with key value of NAME
def create_dict(name, month, year, wind, area, damage, deaths):
    hurricanes = dict()
    num_hurricanes = len(name)
    for i in range(num_hurricanes):
        hurricanes[name[i]] = {"Name": name[i], 
                               "Month": month[i], 
                               "Year": year[i],
                               "Wind": wind[i], 
                               "Areas Affected": area[i], 
                               "Damage": damage[i], 
                               "Deaths": deaths[i]}
    return hurricanes

hurricanes = create_dict(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)


#Creates dictionary of all data with key value of YEAR
def year_dict(hurricanes):
    year_hurricanes = dict()
    for i in hurricanes: 
        current_year = hurricanes[i]["Year"]
        current_i = hurricanes[i]
        if current_year not in year_hurricanes:
            year_hurricanes[current_year] = [current_i]
        else: 
            year_hurricanes[current_year].append(current_i)
    return year_hurricanes

hurricanes_by_year = year_dict(hurricanes)


#Creates dictionary where (key = area affected) and (value = number of times affected)
def total_affected(hurricanes):
    affected_areas_count = dict()
    for i in hurricanes:
        for area in hurricanes[i]["Areas Affected"]:
            if area not in affected_areas_count:
                affected_areas_count[area]= 1
            else:
                affected_areas_count[area] += 1
    return affected_areas_count

total_affected_areas = total_affected(hurricanes)


#Returns most affected area out of all the data
def most_affected(total_affected_areas):
    affected_area = ''
    number_times_affected = 0
    for i in total_affected_areas:
        if total_affected_areas[i] > number_times_affected:
            affected_area = i
            number_times_affected = total_affected_areas[i]
    return affected_area, number_times_affected

most_affected_area = most_affected(total_affected_areas)


#Returns the hurricane that had the most deaths
def most_deaths(hurricanes):
    most_deaths_area = ''
    num_deaths = 0
    for i in hurricanes:
        if hurricanes[i]["Deaths"] > num_deaths:
            most_deaths_area = i
            num_deaths = hurricanes[i]["Deaths"]
    return most_deaths_area, num_deaths

highest_mortality_rate = most_deaths(hurricanes)


#Creates a dictionary of all data with key value of DEATH RATING
def mortality_rating(hurricanes):
    mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000}
    hurricane_ratings = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in hurricanes:
        num_deaths = hurricanes[i]["Deaths"]
        if num_deaths == mortality_scale[0]:
            hurricane_ratings[0].append(hurricanes[i])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            hurricane_ratings[1].append(hurricanes[i])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            hurricane_ratings[2].append(hurricanes[i])
        elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
            hurricane_ratings[3].append(hurricanes[i])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            hurricane_ratings[4].append(hurricanes[i])
        else:
            hurricane_ratings[5].append(hurricanes[i])
    return hurricane_ratings

hurricane_ratings = mortality_rating(hurricanes)


#Returns the hurricane that caused the most damage
def most_damage(hurricanes):
    most_damaged = ''
    damage_amount = 0
    for i in hurricanes:
        if hurricanes[i]["Damage"] == "Damages not recorded":
            pass
        elif hurricanes[i]["Damage"] > damage_amount:
            most_damaged = i
            damage_amount = hurricanes[i]["Damage"]
    return most_damaged, damage_amount

most_damaged = most_damage(hurricanes)


#Creates a dictionary of all data with key value of DAMAGE RATING
def damage_rating(hurricanes):
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    damage_rating = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in hurricanes:
        damage = hurricanes[i]["Damage"]
        if damage == 'Damages not recorded':
            damage_rating[0].append(hurricanes[i])
        elif damage == damage_scale[0]:
            damage_rating[0].append(hurricanes[i])
        elif damage > damage_scale[0] and damage <= damage_scale[1]:
            damage_rating[1].append(hurricanes[i])
        elif damage > damage_scale[1] and damage <= damage_scale[2]:
            damage_rating[2].append(hurricanes[i])
        elif damage > damage_scale[2] and damage <= damage_scale[3]:
            damage_rating[3].append(hurricanes[i])
        elif damage > damage_scale[3] and damage <= damage_scale[4]:
            damage_rating[4].append(hurricanes[i])
        else:
            damage_rating[5].append(hurricanes[i])
    return damage_rating

damage_ratings = damage_rating(hurricanes)