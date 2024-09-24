# Tuples are immutable data type. It has order and index

empty_tpl = tuple() # tuple()
print(type (empty_tpl))

nums = (1, 2, 3, 4)

print(len(nums), type(nums))

for num in nums:
    print(num)

fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[1:])
print(fruits[1:3])

o, m = fruits[1:3]
print(o, m)

fruits = ('banana', 'orange', 'mango', 'lemon', 'orange')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegest = fruits + vegetables
print(fruits_and_vegest)
print(fruits.count('lemon'))

for item in fruits_and_vegest:
    print(item)


print(fruits)
fruits_lst = list(fruits)
print(fruits_lst)
print(list(enumerate(fruits_lst)))

for index, value in enumerate(['Finland','Sweden','Norway','Denmark','Iceland']):
    print(f'{index + 1}. {value}')