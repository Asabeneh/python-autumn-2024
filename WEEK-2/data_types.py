# What are Python data types: Numbers(int, float, complex), Booleans, strings, list, tuples, dictionary

# Numbers

print(type(10))
print(type('10'))
print(type(9.81))
print(type(1 + 2j))


# Booleans: True or False

print(type(True))
print(type(False))
print(type(0 < 1))
print(len('cat') == len('car'))
print('cat' == 'cat')


# Strings: a text under single, double, triple quote. It could a single character or several pages.

print('a')
print('I love python programming')
print('I love python programming'.lower())
print('I love python programming'.upper())
print('I love python programming'.title())
print(print('I love python programming'.swapcase()))
print('I love python programming'.split())
print('I love python programming'.startswith('I love'))
print('I love python programming'.endswith('ing'))

print(dir('kdkdkdkdkdkdkdkd'))

print(dir(10))

## List: is a collection of data types are ordered and indexed, can be mutated

print( [1, 2, 3, 4, 5])
print(['potatos','tomatos', 'milk','coffee','honey'])
print(len(['potatoes','tomatos', 'milk','coffee','honey']))
print(['potatoes','tomatos', 'milk','coffee','honey'][0])


# tuple: indexed, ordered,immutable
print((1, 2, 3, 4, 5))
print(len((1, 2, 3, 4, 5)))
print(type((1, 2, 3, 4, 5)))
print((1, 2, 3, 4, 5)[0])


# Set: set is a collection of item, no order and no index, duplicate is not allowed
print({1, 2, 3, 7, 8, 4, 5})
print(len({1, 2, 3, 3, 3, 4, 5}))

print(len(['Finland','Sweden','Norway','Denmark', 'Finland','Sweden','Finland']))

print(list(set(['Finland','Sweden','Norway','Denmark', 'Finland','Sweden','Finland'])))


# Dictionary: key value pair


print({
    'auto':'car',
    'talo':'house',
    'tuoli':'chair',
    'tietokone':'computer'
})

print({
    'first_name':'Asab',
    'last_name':'Yeta',
    'country':'Finland',
    'city':'Helsinki',
    'age':250,
    'is_married':True,
    'skills':['JavaScript','Python','SQL']
})
print(len({
    'first_name':'Asab',
    'last_name':'Yeta',
    'country':'Finland',
    'city':'Helsinki',
    'age':250,
    'is_married':True,
    'skills':['JavaScript','Python','SQL']
}))
print(type({
    'first_name':'Asab',
    'last_name':'Yeta',
    'country':'Finland',
    'city':'Helsinki',
    'age':250,
    'is_married':True,
    'skills':['JavaScript','Python','SQL']
}))





