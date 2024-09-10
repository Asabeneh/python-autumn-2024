"""
Python Operators:

- Assignment Operator: (=)
- Arithmetic Operators: +, -, *, /, %, //, **
- Comparison Operators: >, >=, <, <=, ==, !=
- Logical Operators: or, and, not
- Membership Operators: in, not in
"""

# Assignment operator (=)
a = 3
mass = 75
gravity = 9.8

# Arithmetic Operators: +, -, *, /, %, //, **
a = 3
b = 4

print("Arithmetic Operations:")
print(f"{a} + {b} =", a + b)   # Output: 3 + 4 = 7
print(f"{a} - {b} =", a - b)   # Output: 3 - 4 = -1
print(f"{a} * {b} =", a * b)   # Output: 3 * 4 = 12
print(f"{a} / {b} =", a / b)   # Output: 3 / 4 = 0.75
print(f"{a} % {b} =", a % b)   # Output: 3 % 4 = 3
print(f"{a} ** {b} =", a ** b) # Output: 3 ** 4 = 81
print(f"{a} // {b} =", a // b) # Output: 3 // 4 = 0
print()  # Blank line for readability

# Comparison Operators: >, >=, <, <=, ==, !=
print("Comparison Operations:")
print(f"4 > 3:", 4 > 3)     # Output: 4 > 3: True
print(f"4 >= 3:", 4 >= 3)   # Output: 4 >= 3: True
print(f"4 < 3:", 4 < 3)     # Output: 4 < 3: False
print(f"3 < 4:", 3 < 4)     # Output: 3 < 4: True
print(f"3 <= 4:", 3 <= 4)   # Output: 3 <= 4: True

print(f"4 == 3:", 4 == 3)   # Output: 4 == 3: False
print(f"4 == 4:", 4 == 4)   # Output: 4 == 4: True
print(f"4 == '4':", 4 == '4')   # Output: 4 == '4': False
print(f"4 == int('4'):", 4 == int('4')) # Output: 4 == int('4'): True
print(f"4 == 2 ** 2:", 4 == 2 ** 2)     # Output: 4 == 2 ** 2: True

print(f"4 != 3:", 4 != 3)   # Output: 4 != 3: True
print(f"4 != 4:", 4 != 4)   # Output: 4 != 4: False
print(f"4 != '4':", 4 != '4')   # Output: 4 != '4': True

# Identity Operators: is, is not
print(f"4 is 4:", 4 is 4)   # Output: 4 is 4: True
print(f"2 is not 4:", 2 is not 4)   # Output: 2 is not 4: True
print(f"2 is 4:", 2 is 4)   # Output: 2 is 4: False
print()  # Blank line for readability

# Membership Operators: in, not in
print("Membership Operations:")
print("'Py' in 'Python':", 'Py' in 'Python')   # Output: 'Py' in 'Python': True
print("'land' in 'Finland':", 'land' in 'Finland') # Output: 'land' in 'Finland': True
print("'a' in ['a', 'e', 'i', 'o', 'u']:", 'a' in ['a', 'e', 'i', 'o', 'u']) # Output: 'a' in ['a', 'e', 'i', 'o', 'u']: True
print()  # Blank line for readability

# Logical Operators: and, or, not
print("Logical Operations (and):")
print('Both sides are true:', 4 > 3 and 3 < 4)  # Output: Both sides are true: True
print('When one side is false:', 4 > 3 and 3 == 4)  # Output: When one side is false: False
print('Both sides are false:', 4 < 3 and 3 > 4)  # Output: Both sides are false: False

print("\nLogical Operations (or):")
print('Both sides are true:', 4 > 3 or 3 < 4)  # Output: Both sides are true: True
print('When one side is true:', 4 > 3 or 3 == 4)  # Output: When one side is true: True
print('Both sides are false:', 4 < 3 or 3 == 4)  # Output: Both sides are false: False

print("\nLogical Operations (not):")
print('Original True:', True)   # Output: Original True: True
print('Negation of True:', not True)   # Output: Negation of True: False
print('Double Negation of True:', not not True)  # Output: Double Negation of True: True
print('Negation with logical expression:', not (4 < 3 or 3 == 4)) # Output: Negation with logical expression: True
print()  # Blank line for readability

# More Examples
age = 19  # Assigning a new value
height = 1.72  # height in meters
complex_num = 5j  # Complex number

print(f"Data type of complex_num ({complex_num}):", type(complex_num)) # Output: Data type of complex_num (5j): <class 'complex'>
