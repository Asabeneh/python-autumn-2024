# Conditionals allows us to make decision based some condition

a = -105

if a > 0:
    print(f'{a} is a positive number')
elif a < 0:
    print(f'{a} is a negative number')
elif a == 0:
    print(f'{a} is zero')
else:
    print('This not an integer')


is_raining = False 

if is_raining:
    print('Go out with an umbrella')
else:
    print('It seems a shiny day go out freely and enjoy your day')

weather = input('What is the weather today? ').lower()
print(weather)

if weather == 'rainy':
     print('Go out with an umbrella')
elif weather == 'sunny':
     print('It seems a shiny day go out freely and enjoy your day')
elif weather == 'cloudy':
    print('It may rain, good to consider a raincoat')
elif weather == 'snowy':
    print('The road might be slippery')
else:
    print('No one knows about the weather')

number = int(input('Write a number? '))

if number > 0:
    print('The absolute value is', number)
else:
    print('The absolute value is', number * -1)



