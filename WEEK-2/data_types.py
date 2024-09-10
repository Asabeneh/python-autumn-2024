# Python Data Types: Numbers (int, float, complex), Booleans, Strings, Lists, Tuples, Sets, Dictionaries

# Numbers
print("Numbers:")
print(type(10))  # int
print(type('10'))  # str
print(type(9.81))  # float
print(type(1 + 2j))  # complex

# Booleans: True or False
print("\nBooleans:")
print(type(True))  # bool
print(type(False))  # bool
print(type(0 < 1))  # bool
print(len('cat') == len('car'))  # False
print('cat' == 'cat')  # True

# Strings: A sequence of characters enclosed in single, double, or triple quotes
print("\nStrings:")
print('a')  # Single character string
print('I love Python programming')  # String sentence
print('I love Python programming'.lower())  # Convert to lowercase
print('I love Python programming'.upper())  # Convert to uppercase
print('I love Python programming'.title())  # Title case
print('I love Python programming'.swapcase())  # Swap case
print('I love Python programming'.split())  # Split into a list of words
print('I love Python programming'.startswith('I love'))  # Check if it starts with 'I love'
print('I love Python programming'.endswith('ing'))  # Check if it ends with 'ing'

# Explore string methods
print(dir('example_string'))  # Show available string methods

# Lists: A collection of ordered and mutable elements
print("\nLists:")
print([1, 2, 3, 4, 5])  # List of numbers
print(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey'])  # List of strings
print(len(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey']))  # List length
print(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey'][0])  # Accessing the first item

# Tuples: Ordered, indexed, and immutable collections
print("\nTuples:")
print((1, 2, 3, 4, 5))  # Tuple of numbers
print(len((1, 2, 3, 4, 5)))  # Tuple length
print(type((1, 2, 3, 4, 5)))  # Type check
print((1, 2, 3, 4, 5)[0])  # Accessing the first item

# Sets: An unordered collection of unique items (no duplicates allowed)
print("\nSets:")
print({1, 2, 3, 7, 8, 4, 5})  # Set of numbers
print(len({1, 2, 3, 3, 3, 4, 5}))  # Set length (duplicates removed)
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Sweden', 'Finland']
print(len(countries))  # Length of original list
print(list(set(countries)))  # Convert to set to remove duplicates and back to list

# Dictionaries: A collection of key-value pairs
print("\nDictionaries:")
translations = {
    'auto': 'car',
    'talo': 'house',
    'tuoli': 'chair',
    'tietokone': 'computer'
}
print(translations)  # Dictionary of translations

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
print(len(person))  # Dictionary length
print(type(person))  # Type check

