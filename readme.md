# Python Programming

# Python Code Examples and Notes

This document provides an overview of various Python code examples, including explanations and expected outputs for each code snippet.

## 1. Basic Arithmetic Operations

```python
# Arithmetic operations: addition, subtraction, multiplication, division, modulus, floor division, exponentiation

# Addition
print('The sum of 3 and 4 is:', 3 + 4)
# Output: The sum of 3 and 4 is: 7

# Subtraction
print('The difference between 4 and 3 is:', 4 - 3)
# Output: The difference between 4 and 3 is: 1

# Multiplication
print('The product of 3 and 4 is:', 3 * 4)
# Output: The product of 3 and 4 is: 12

# Division (float)
print('The division of 4 by 3 is:', 4 / 3)
# Output: The division of 4 by 3 is: 1.3333333333333333

# Modulus (remainder)
print('The remainder when 4 is divided by 3 is:', 4 % 3)
# Output: The remainder when 4 is divided by 3 is: 1

# Exponentiation (power)
print('3 raised to the power of 4 is:', 3 ** 4)
# Output: 3 raised to the power of 4 is: 81

# Floor Division (integer division)
print('The floor division of 4 by 3 is:', 4 // 3)
# Output: The floor division of 4 by 3 is: 1
```

##  Comments and Documentation

```py
# This is a single-line comment. Any text preceded by a hash symbol (#) is a comment in Python.
# Purpose of comments: To make code more readable and maintainable.

# The `print` function is a built-in function that outputs its arguments to the console.
print('Hello', 2024, 'Python', 9.8, 3.14, 100)
# Output: Hello 2024 Python 9.8 3.14 100

'''
This is a multi-line comment (or docstring) that allows us to write 
several lines of comments in our Python code. 

It can be used for longer explanations or documentation.
'''

"""
This is another style of multi-line comment.

Both styles of multi-line comments are used for writing longer explanations or documentation.
"""
```

## Built-in Functions

```py
# Built-in functions in Python: print, len, input, type, int, float, min, max, sum, list, range, abs, round, dir
# The `print` function displays the provided inputs.
print('Asabeneh', 2024, True, False, [1, 2, 3, 4], 'We love Python', sep=', ')
# Output: Asabeneh,2024,True,False,[1, 2, 3, 4],We love Python

print('Asabeneh', 2024, True, False, [1, 2, 3, 4], 'We love Python', sep='\n')
# Output:
# Asabeneh
# 2024
# True
# False
# [1, 2, 3, 4]
# We love Python

# The `len` function returns the number of items in an object (e.g., string, list).
print('Length of "cat":', len('cat'))
# Output: Length of "cat": 3

print('Length of list [1, 2, 3, 4, 5, 6]:', len([1, 2, 3, 4, 5, 6]))
# Output: Length of list [1, 2, 3, 4, 5, 6]: 6

print('Length of "I love cat":', len('I love cat'))
# Output: Length of "I love cat": 11

# The `type` function returns the type of an object.
print('Type of float(\'9.81\'):', type(float('9.81')))
# Output: Type of float('9.81'): <class 'float'>

# The `min` function returns the smallest of the given arguments.
print('Minimum value:', min(1, 2, 20, -10, 200, 0))
# Output: Minimum value: -10

# The `max` function returns the largest of the given arguments.
print('Maximum value:', max(1, 2, 20, -10, 200, 0))
# Output: Maximum value: 200

# The `sum` function returns the sum of all items in an iterable.
print('Sum of list [1, 2, 20, -10, 200, 0]:', sum([1, 2, 20, -10, 200, 0]))
# Output: Sum of list [1, 2, 20, -10, 200, 0]: 213

# The `list` function creates a list object.
print('Empty list:', list())
# Output: Empty list: []

print('List from string "cat":', list('cat'))
# Output: List from string "cat": ['c', 'a', 't']

# The `range` function generates a sequence of numbers.
print('Range from 0 to 10:', list(range(0, 10, 1)))
# Output: Range from 0 to 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('Range from 0 to 100:', list(range(0, 101, 1)))
# Output: Range from 0 to 100: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 100]

print('Range from 0 to 100 with step 2:', list(range(0, 101, 2)))
# Output: Range from 0 to 100 with step 2: [0, 2, 4, 6, 8, ..., 100]

print('Range from 1 to 100 with step 2:', list(range(1, 101, 2)))
# Output: Range from 1 to 100 with step 2: [1, 3, 5, 7, 9, ..., 99]

# The `round` function returns a number rounded to a specified number of decimal places.
print('Round 3.14159 to 2 decimal places:', round(3.14159, 2))
# Output: Round 3.14159 to 2 decimal places: 3.14

print('Round 9.87654 to 1 decimal place:', round(9.87654, 1))
# Output: Round 9.87654 to 1 decimal place: 9.9

# The `abs` function returns the absolute value of a number.
print('Absolute value of -5:', abs(-5))
# Output: Absolute value of -5: 5
```

## Variables

```py

# Variables: Containers to store different data types
a = 3 
b = 4 
c = a + b

# Printing variables
print('Value of a:', a)
# Output: Value of a: 3

print('Sum of a and b:', c)
# Output: Sum of a and b: 7

# Arithmetic operations with variables
print('Sum of a and b is', a + b)
# Output: Sum of a and b is 7

print('Difference of a and b is', a - b)
# Output: Difference of a and b is -1

print('Product of a and b is', a * b)
# Output: Product of a and b is 12

print('Division of a and b is', a / b)
# Output: Division of a and b is 0.75

# Define more variables
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250  # Note: age should not be a tuple, corrected here
is_married = True 
skills = ['HTML', 'CSS', 'JavaScript', 'Python']  # List
# skills = ('HTML', 'CSS', 'JavaScript', 'Python')  # Tuple (commented out)
# skills = {'HTML', 'CSS', 'JavaScript', 'Python'}  # Set (commented out)

gravity = 9.81
mass = 75

weight = mass * gravity 
print('Weight:', round(weight, 1))
# Output: Weight: 735.8

current_year = 2024
```

## Data types

Python data types, including examples and expected outputs for each type. Understanding these data types is crucial for effective programming in Python.

### 1. Numbers

In Python, numbers come in several types:

```python
# Numbers
print("Numbers:")
print(type(10))  # int
# Output: <class 'int'>

print(type('10'))  # str
# Output: <class 'str'>

print(type(9.81))  # float
# Output: <class 'float'>

print(type(1 + 2j))  # complex
# Output: <class 'complex'>
```

### 2. Booleans
 Booleans: True or False

```py
print("\nBooleans:")
print(type(True))  # bool
# Output: <class 'bool'>

print(type(False))  # bool
# Output: <class 'bool'>

print(type(0 < 1))  # bool
# Output: <class 'bool'>

print(len('cat') == len('car'))  # False
# Output: False

print('cat' == 'cat')  # True
# Output: True
```


### 3. Strings

 Strings: A sequence of characters enclosed in single, double, or triple quotes
print("\nStrings:")

```py
print('a')  # Single character string
# Output: a

print('I love Python programming')  # String sentence
# Output: I love Python programming

print('I love Python programming'.lower())  # Convert to lowercase
# Output: i love python programming

print('I love Python programming'.upper())  # Convert to uppercase
# Output: I LOVE PYTHON PROGRAMMING

print('I love Python programming'.title())  # Title case
# Output: I Love Python Programming

print('I love Python programming'.swapcase())  # Swap case
# Output: i LOVE pYTHON PROGRAMMING

print('I love Python programming'.split())  # Split into a list of words
# Output: ['I', 'love', 'Python', 'programming']

print('I love Python programming'.startswith('I love'))  # Check if it starts with 'I love'
# Output: True

print('I love Python programming'.endswith('ing'))  # Check if it ends with 'ing'
# Output: True

# Explore string methods
print(dir('example_string'))  # Show available string methods
# Output: List of string methods
```

### 4. Lists
```py

# Lists: A collection of ordered and mutable elements
print("\nLists:")
print([1, 2, 3, 4, 5])  # List of numbers
# Output: [1, 2, 3, 4, 5]

print(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey'])  # List of strings
# Output: ['potatoes', 'tomatoes', 'milk', 'coffee', 'honey']

print(len(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey']))  # List length
# Output: 5

print(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey'][0])  # Accessing the first item
# Output: potatoes

```

### 5. Tuples

```py
# Tuples: Ordered, indexed, and immutable collections
print("\nTuples:")
print((1, 2, 3, 4, 5))  # Tuple of numbers
# Output: (1, 2, 3, 4, 5)

print(len((1, 2, 3, 4, 5)))  # Tuple length
# Output: 5

print(type((1, 2, 3, 4, 5)))  # Type check
# Output: <class 'tuple'>

print((1, 2, 3, 4, 5)[0])  # Accessing the first item
# Output: 1
```

### 6. Sets
```py
# Sets: An unordered collection of unique items (no duplicates allowed)
print("\nSets:")
print({1, 2, 3, 7, 8, 4, 5})  # Set of numbers
# Output: {1, 2, 3, 4, 5, 7, 8}

print(len({1, 2, 3, 3, 3, 4, 5}))  # Set length (duplicates removed)
# Output: 5

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Sweden', 'Finland']
print(len(countries))  # Length of original list
# Output: 7

print(list(set(countries)))  # Convert to set to remove duplicates and back to list
# Output: ['Denmark', 'Norway', 'Sweden', 'Finland']
```

### 7. Dictionaries

```py
# Dictionaries: A collection of key-value pairs
print("\nDictionaries:")
fin_eng_dict = {
    'auto': 'car',
    'talo': 'house',
    'tuoli': 'chair',
    'tietokone': 'computer'
}
print(fin_eng_dict)  # Dictionary of fin_eng_dict
# Output: {'auto': 'car', 'talo': 'house', 'tuoli': 'chair', 'tietokone': 'computer'}

person = {
    'first_name': 'Asab',
    'last_name': 'Yeta',
    'country': 'Finland',
    'city': 'Helsinki',
    'age': 250,
    'is_married': True,
    'skills': ['JavaScript', 'Python', 'SQL']
}
print(person)  # Person dictionary
# Output: {'first_name': 'Asab', 'last_name': 'Yeta', 'country': 'Finland', 'city': 'Helsinki', 'age': 250, 'is_married': True, 'skills': ['JavaScript', 'Python', 'SQL']}

print(len(person))  # Dictionary length
# Output: 7

print(type(person))  # Type check
# Output: <class 'dict'>
```

## Operators
# Python Operators Overview

 Python operators, including assignment, arithmetic, comparison, logical, membership, and identity operators. Examples are provided for each type of operator along with their expected outputs.

### 1. Assignment Operator

The assignment operator `=` is used to assign values to variables.

```python
# Assignment operator (=)
a = 3
mass = 75
gravity = 9.8
```

### 2. Arithmetic Operators
```py
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

```

### 3. Comparison Operators

```py
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

```

### 4. Identity Operators
```py
# Identity Operators: is, is not
print(f"4 is 4:", 4 is 4)   # Output: 4 is 4: True
print(f"2 is not 4:", 2 is not 4)   # Output: 2 is not 4: True
print(f"2 is 4:", 2 is 4)   # Output: 2 is 4: False
print()  # Blank line for readability
```
### 5. Membership Operators

```py
# Membership Operators: in, not in
print("Membership Operations:")
print("'Py' in 'Python':", 'Py' in 'Python')   # Output: 'Py' in 'Python': True
print("'land' in 'Finland':", 'land' in 'Finland') # Output: 'land' in 'Finland': True
print("'a' in ['a', 'e', 'i', 'o', 'u']:", 'a' in ['a', 'e', 'i', 'o', 'u']) # Output: 'a' in ['a', 'e', 'i', 'o', 'u']: True
print()  # Blank line for readability
```

### 6. Logical Operators

```py
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
```