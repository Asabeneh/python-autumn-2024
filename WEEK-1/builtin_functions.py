# Built-in functions in Python: print, len, input, type, int, float, min, max, sum, list, range, abs, round, dir

# The `print` function displays the provided inputs.
print('Asabeneh', 2024, True, False, [1, 2, 3, 4], 'We love Python', sep=', ')
print('Asabeneh', 2024, True, False, [1, 2, 3, 4], 'We love Python', sep='\n')

# The `len` function returns the number of items in an object (e.g., string, list).
print('Length of "cat":', len('cat'))
print('Length of list [1, 2, 3, 4, 5, 6]:', len([1, 2, 3, 4, 5, 6]))
print('Length of "I love cat":', len('I love cat'))

# The `input` function gets input from the user. (Commented out for demonstration purposes)
"""
first_name = input('Enter your name: ')
birth_year = int(input('When were you born? '))
age = 2024 - birth_year
print(f'{first_name}, you are {age} years old.')

radius = float(input('What is the radius of the circle? '))
area_of_circle = 3.14 * radius * radius
print(f'The area of the circle is: {area_of_circle}')
"""

# The `type` function returns the type of an object.
print('Type of float(\'9.81\'):', type(float('9.81')))

# The `min` function returns the smallest of the given arguments.
print('Minimum value:', min(1, 2, 20, -10, 200, 0))

# The `max` function returns the largest of the given arguments.
print('Maximum value:', max(1, 2, 20, -10, 200, 0))

# The `sum` function returns the sum of all items in an iterable.
print('Sum of list [1, 2, 20, -10, 200, 0]:', sum([1, 2, 20, -10, 200, 0]))

# The `list` function creates a list object.
print('Empty list:', list())
print('List from string "cat":', list('cat'))

# The `range` function generates a sequence of numbers.
print('Range from 0 to 10:', list(range(0, 10, 1)))
print('Range from 0 to 100:', list(range(0, 101, 1)))
print('Range from 0 to 100 with step 2:', list(range(0, 101, 2)))
print('Range from 1 to 100 with step 2:', list(range(1, 101, 2)))

# The `round` function returns a number rounded to a specified number of decimal places.
print('Round 3.14159 to 2 decimal places:', round(3.14159, 2))
print('Round 9.87654 to 1 decimal place:', round(9.87654, 1))

# Summing ranges
print('Sum of range from 1 to 100 with step 2:', sum(range(1, 101, 2)))
print('Sum of range from 0 to 100 with step 2:', sum(range(0, 101, 2)))

# The `abs` function returns the absolute value of a number.
print('Absolute value of -5:', abs(-5))
