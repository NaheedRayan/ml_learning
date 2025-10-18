# Decorators let you modify or extend the behavior of functions — without changing their code.



def greet():
    print("Hello!")

def decorator(func):
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

# Using the decorator
@decorator
def greet():
    print("Hello!")


greet()