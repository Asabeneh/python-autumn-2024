"""
Operators:
- assignment operator (=)
- Arithmetics: +, -, *, /, %, //, **
- Comparison operators: >, >=, <, <=, ==, !=
- Logical operators: or, and, not

"""

# Assignment operator(=)
a = 3 
mass = 75
gravity = 9.8 

# Arithmetics: +, -, *, /, %, //, **
a = 3 
b = 4 

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

# - Comparison operators: >, >=, <, <=, ==, !=

print(4 > 3)
print(4 >= 3)

print(4 < 3)
print(3 < 4)
print(3 <= 4)


print(4 == 3)
print(4 == 4)
print(4 == '4')
print(4 == int('4'))
print(4 == 2 ** 2)

print(4 != 3)
print(4 != 4)
print(4 != '4')
print(4 is 4)
print(2 is not 4)
print(2 is 4 )

# Membership
print('Py' in 'Python')
print('Does land exist in FInland', 'land' in 'Finland')
print('check if a is a vlue', 'a' in ['a','e','i','o','u'])

print('Both sides are true:', 4 > 3 and 3 < 4)
print('When one side is true:', 4 > 3 and 3 == 4)
print('Both sides are false:', 4 < 3 and 3 > 4)

print('Both sides are true:', 4 > 3 or 3 < 4)
print('When one sides is true:', 4 > 3 or 3 == 4)
print('Both one sides is false:', 4 < 3 or 3 == 4)

print('NEGATION')
print(True)
print(not True)
print(not not True)
print('Both one sides are false:', 4 < 3 or 3 == 4)
print('Both one sides are false:', not (4 < 3 or 3 == 4) )
print('Both one sides are false:', 4 < 3 or not 3 == 4 )


age = 250
age = 19
height = 1.72 
complex_num = 5j
print(type(complex_num))





