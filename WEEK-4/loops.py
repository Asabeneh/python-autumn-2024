# What is loop in python?
# Loop is a control structure that repeats a group of statements a specified number of times or until a specific condition is met.
# There are two types of loops in Python, for and while.
# For loop: For loops iterate over a given sequence. Here is an example:
# for val in sequence:
#     Body of for
# While loop: While loop repeats as long as a certain boolean condition is met. Here is an example:
# while condition:

print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')
print('Hello World!')

nums = range(1, 10, 1)

for num in nums :
    print(num, 'Hello world!')

names = ['Mikko','Matti','Elena', 'Olga','Lauri','Kimm0','Mehrnaz','Jevgeni','Goodluck','Pullo','Asabeneh']
print(len(names))

for name in names:
    # print(name, len(name), name.upper())
    if len(name) > 6:
        print(f'{name} is a long name.')
    else:
        print(f'{name} is a short name')

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
print(len(countries))
""" 
for country in countries:
    print(country, country.upper(),  country.upper()[:3]) """


print('Py' in 'Python')

countries_with_land = []
for country in countries:
    if 'land' in country:
        countries_with_land.append(country)

print(countries_with_land, len(countries_with_land))

for country in countries:
    if country.endswith('ia'):
        print(country)

# Write a similar loops that find the list of countries starts with S

countries_starts_with_s = []
for country in countries:
    if country.startswith('B'):
        countries_starts_with_s.append(country)
print(countries_starts_with_s, len(countries_starts_with_s))

""" dct = [
    {
        'A':['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan'],
        'count':11
    },
    {
        'B':['Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi'],
        'count':17
    }
] """

nums = [-10, 5, 0, 20, 4.5, 20, -14, 25, -3]
print(sum(nums))

total = 0
for num in nums:
    total += total + num

print(total)

even_nums = []
odd_nums = []
for num in nums:
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)
print('even numbers:', even_nums)
print('odd numbers:', odd_nums)

positive_nums = []
negative_nums = []
for num in nums:
    if num > 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)


print(positive_nums)
print(negative_nums)

# While

names = []
while True:
    name = input('Enter name: ')
    if name == 'quit' or name == '':
        break
    names.append(name)
print(names)


count = 0 

while count < 6:
    print(count)
    count = count + 1


print('=== for loop result ===')

for i in range(5, -1, -1):
    print(i)

print('=== while loop result ===')

count = 5 

while count > -1:
    print(count)
    count = count - 1


nums = [-10, 5, 0, 20, 4.5, 20, -14, 25, -3]

print(' skip negative value')
for num in nums:
    if num <= 0:
        continue
    print(num)

print('break if zero exist in the list')
for num in nums:
    if num == 0:
        break 
    print(num)

    for i in range(11):
        print(f'{i} x {i} = {i * i}')