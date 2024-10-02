from pprint import pprint
from countries import countries


def filter_country_with_land(lst):
    new_lst = []
    for country in lst:
        if 'land' in country:
            new_lst.append(country)
    return new_lst
# pprint(filter_country_with_land())

'''
A: ['Albania', 'Algeria' ]
F:['Finland','Fiji','France']
'''

# for country in countries:
#     for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         if country.startswith(letter):
#             print(country)

# 197 * 26

def xyz(lst):
    dct = {}
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        new_lst = []
        for country in lst:
            if country.startswith(letter):
                new_lst.append(country)
        dct[letter] = new_lst
    return dct

pprint(xyz(countries))

# Modules 

# multiplication Table


# for i in range(13):
#     x = ''
#     for j in range(13):
#         x += str(i * j)
#     print(x)


    



