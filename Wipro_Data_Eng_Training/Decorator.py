def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

#@my_decorator
def my_func():
    print("Welcome")

#my_func()
#second syntax
decorated = my_decorator(my_func)
decorated()