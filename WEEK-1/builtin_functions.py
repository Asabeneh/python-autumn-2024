# Builtin function: print, len, input, type, int, float, min, max, sum,  list,range, abs,dir

# print takes several inputs and display it
print('Asabeneh', 2024, True, False, [1, 2, 3, 4], 'We love python' , sep =', ')
print('Asabeneh', 2024, True, False, [1, 2, 3, 4], 'We love python' , sep ='\n')

# len allows us to give the numbers characters

print(len('cat'))
print(len([1, 2, 3,4,5,6]))
print('i love cat', len('i love cat'))


# input allows to get input from user

""" first_name = input('Enter your name: ')
birth_year = int(input('When were you born? '))
age = 2024 - birth_year

print(first_name, age)

radius = float(input('What is the radius of the circle? '))

area_of_circle = 3.14 * radius * radius

print(area_of_circle) """


print(type(float('9.81')))

print(min(1, 2, 20, -10, 200, 0))
print(max(1, 2, 20, -10, 200, 0))
print(sum([1, 2, 20, -10, 200, 0]))

print(list())
print(list('cat'))

print(range(0, 10, 1))
print(list(range(0, 101, 1)))
print(list(range(0, 101, 2)))
print(list(range(1, 101, 2)))

print(sum(range(1, 101, 2)))
print(sum(range(0, 101, 2)))

print(abs(-5))



