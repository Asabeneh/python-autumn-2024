# map, filter, reduce
# map => [1, 2, 3] => [1, 4, 9]
# ['Finland','Sweden','Denmark'] => ['Helsinki', 'Stockholm', 'Copenhage']
from countries_data import countries_data
from countries_data_big import countries_data_big
from functools import reduce
from pprint import pprint
nums = [1, 2, 3, 4, 5] 

 
country_names = list(map(lambda country: country['name'], countries_data))
populations = list(map(lambda country: country['population'], countries_data))

# pprint(list(country_names))
world_population = sum(populations)
# print(world_population)


'''
use the above map by changing the propety to languages
Then you get a list of list
Change the list of list to one big list
Then put this list to a set
then use len() to know the unique number of langues

'''

'''

Find the ten most populated countries
Find the ten most spoken languages 

'''

languages = list(map(lambda country: country['languages'], countries_data))

all_languages = []
for language in languages:
    all_languages.extend(language)
# pprint(all_languages)
# print(len(all_languages))
# unique_languages = set(all_languages)
# pprint(unique_languages)
# print(len(unique_languages))

# pprint(list(map(lambda country: [country['name'], country['name'].upper()[:3]], countries_data)))


# Filter 

nums = [0, -5, 2, 4, 10, 3]

evens = []
for num in nums:
    if num % 2 == 0:
        evens.append(num)
        
print(evens)

def is_even(n):
   return n % 2 != 0
    

# print(list(filter(is_even, nums)))
country_names = list(map(lambda country: country['name'], countries_data))
countries_with_land = list(filter(lambda country: 'land' in country, country_names))
# pprint(countries_with_land)

european_countries = list(filter(lambda country:country['region'] =='Europe', countries_data_big))
# pprint(european_countries)

# Reduc => 
nums = [1, 2, 3, 4, 5]
print(reduce(lambda acc, cur: acc * cur, nums))

total = 0 
for num in nums:
    total = total + num 
    

# List comprehension

nums = [1, 2, 3, 4, 5] # [2, 4, 6, 8, 10]

print(list(map(lambda n: n * 2, nums)))

squares = [num ** 2 for num in nums]
print('squares:', squares)

print([num + 100 for num in nums if num % 2 == 0])

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
""" def change_to_flat_list(lst):
    new_lst = []
    for l in lst:
        new_lst.extend(l)
    return new_lst 

print(change_to_flat_list(lst)) """
print([ n for l in lst for n in l])
pprint([[country['name'], country['capital'], country['population']] for country in countries_data])
country_names = [country['name'] for country in countries_data]
populations = [country['population'] for country in countries_data]

data = [{
    'name': country['name'], 
    'capital': country['capital'], 
    'population': country['population']
    } for country in countries_data]

pprint(data)

pprint([country['name'] for country in countries_data if 'land' in country['name']])


