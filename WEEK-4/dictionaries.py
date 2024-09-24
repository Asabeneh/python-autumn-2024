# It is a key value data structure

empty_dict = {} # dict()
print(type(empty_dict), len(empty_dict))

dict_methdods = ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'is_married':True,
    'address': {
        'country':'Finland',
        'city':'Espoo',
        'zipcode':'02770',
        'street':'Space street'
    },
    'skills':['HTML','CSS', 'JavaScript', 'Python', 'NumPy','TextBob', 'Flask', 'MySQL'],
    'educations':[
       {
        'name':'Helsinki Metropolia University of Applied Science',
        'qualification':'BEng.',
        'field':'Information Technology',
        'starting_year':2012,
        'ending_year':2017
       },
        {
        'name':'Helsinki University',
        'qualification':'MSc.',
        'field':'Computer Science',
        'starting_year':2017,
        'ending_year':2017
       }
    ]

}
print(person)
print(len(person))
print(person['first_name'])
print(person['address']['country'])
print(person.get('nationality'))
person['nationality'] = 'Ethiopian'

print(person)

print(person.get('nationality'))
print(len(person))
person['hobbies'] = []
print(person)
person['hobbies'].append('Ice skating')
person['hobbies'].append('Running')

print(person)

for item in person:
    print(item, person[item])

items = person.items()
print(items)

for key, value in items:
    print(key, value)


keys = person.keys()
print(keys)
values = person.values()
print(values)