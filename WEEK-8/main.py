import utils
from utils.fetch_data import fetch_data
from utils.create_json_file import create_json_file
from pprint import pprint

print('I am from the main.py file')

cats_url = 'https://api.thecatapi.com/v1/breeds'

data = fetch_data(cats_url)
print(data)


# cats_url = 'https://api.thecatapi.com/v1/breeds'
# cats = fetch_data(cats_url)

# countries = fetch_data('https://restcountries.com/v3.1/all')
# pprint(countries)

lst = []
for cat in data:
    mn, mx = cat['life_span'].split(' - ')
    average_life_span = (int(mn) + int(mx)) / 2
    min_weight, max_weight = cat['weight']['metric'].split(' - ')
    average_weight = (int(min_weight) + int(max_weight)) / 2
    
    dct = {
        'name':cat['name'],
        'country':cat['origin'],
        'description':cat['description'],
        'life_span':average_life_span,
        'weight':average_weight
    }
    lst.append(dct)
print(lst)
create_json_file('cats.json', lst)

