import os 
""" 
if not os.path.exists('new_folder'):
    os.mkdir('new_folder')
     
else:
    os.rmdir('new_folder')
with open('new_folder/notes.txt', 'w') as f:
    f.write('This is my note') """
    
print(dir(os))
for data in os.walk('.'):
    # print(data[2:])
    pass
    
    # x, y, z = data
    # if '.git' not in x:
    #     print(x)

for path, directories, files in os.walk('.'):
    # print('path:', path)
    # print(files)
    pass
    
import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
from countries_data_big import countries_data_big

lst = []
for c in countries_data_big:
    name = c['name']
    capital = c['capital']
    population = c['population']
    pass
 

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./data/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, indent=4)
    
# countries.json file in the data folder