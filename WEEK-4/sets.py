# Set is a collection of items, items are not orderd, no indexing, mutable
empty_set = set()

print(empty_set, len(empty_set))
print(dir(empty_set))
empty_set.add('Milk')
empty_set.add('Coffee')
print(empty_set)

A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 7, 8}
# A U B = {1, 2, 3, 4, 5, 6, 7, 8} A U B = B U A
# A n B = { 3, 4}
# A \ B = {1, 2, 5, 6}
# B \ A = {7, 8}
# A Δ B = (A \ B) U (B\A) = {1, 2, 5, 6, 7, 8}

print(A.union(B))
print(B.union(A))
print(A.intersection(B))
print(B.intersection(A))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))

print(dir(empty_set))
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('kiwi' in fruits)
print('orange' in fruits)

for fruit in fruits:
    print(fruit)

fruits.add('guava')
fruits.add('papaya')

print(fruits)
fruits.update(['apple', 'apricot','watermelon'])
# print(fruits)
# fruits.pop()
# print(fruits)
fruits.remove('orange')
print(fruits)
fruits.clear()
print(fruits)
# del fruits
# print(fruits)

print(set(['Finland','Sweden','Denmark','Sweden']))

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

A = {1, 2, 3, 4}
B = {1, 2, 3, 3, 4, 5, 6}
# A c B
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.issuperset(A))