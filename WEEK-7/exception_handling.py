from datetime import datetime 
now = datetime.now()
current_year = now.year 

""" try:
    birth_year = int(input('What your birth year? '))
    age = current_year - birth_year
    print(f'Your age is {age}')
except Exception as e:
    print('something wrong happend', e)
else:
    print('This code goes with the try, means when there is no exception')
finally:
    print('No matter what this block will be executed')
     """
try:
    # name = input('Enter your name:')
    # year_born = input('Year you were born:')
    # age = current_year - year_born
    # print(f'You are {name}. And your age is {age}.')
    # print([1, 2,3][4])
    user = {'name':'Asab'}
    print(user['age'])
except KeyError:
    print('Key error')  
except Exception as e:
    print(e)
    
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]

lst = [0, *lst_one, *lst_two, 8, 9, 10]
print(lst)

countries = ['Finland','Sweden','Norway','Denmark','Iceland']
cities = ['Helsinki','Stockholm','Oslo','Copenhagen','Vij']
fin, swe, _, *rest = countries
print(fin, swe)
print(rest)

def sum_all_nums(*args):
    print(args)

sum_all_nums(1, 2, 3, 4, 5, 10, -50, 20)

for index,country in enumerate(countries):
    print(index + 1, country)
    
    
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage' ]
print(list(zip(fruits, vegetables)))
print(list(zip(countries,cities)))
