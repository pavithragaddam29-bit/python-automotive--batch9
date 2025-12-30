# Define the decorator function
def star_decorator(func):
    def wrapper():
        return "*****" + func() + "*****"
    return wrapper

# Define the say_hello function
def say_hello():
    return "Hello"

# Decorate say_hello without using @ syntax
decorated_hello = star_decorator(say_hello)
print(decorated_hello())  # Output: *****Hello*****

# Decorate say_hello using @ syntax
@star_decorator
def say_hello_decorated():
    return "Hello"

print(say_hello_decorated())  # Output: *****Hello*****
