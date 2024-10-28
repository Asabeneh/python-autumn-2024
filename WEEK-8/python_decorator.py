def decorate_me(func):
    def wrapper ():
        print('I will decorate you')
        func()
        print('Hopefully you are decorated')
    return wrapper

@decorate_me
def say_hello():
    print('Hello people!')
    
    
say_hello()