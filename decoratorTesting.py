"""
def check(func):
    def wrapper(a,b):
        if b==0:
            print('Cant divide by zero.')
        else:
            print(func(a,b))
    return wrapper

@check
def div(a,b):
    return a/b

div(10,0)

"""
"""

def cough(func):
    def wrapper():
        print('cough1')
        func()
        print('cough2')
    return wrapper

@cough
def my_ask():
    print('can I get a discount on that?')

my_ask()

"""

def more(str):
    def wrapper():
        str = str*2
    return wrapper

@more
my_string = "hello"

print(my_var)
