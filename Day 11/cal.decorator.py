def calculator(func):
    def wrapper(a,b):
        print(f"adding{a} and {b}")
        result=func(a,b)
        print(f"result:{result}")
        return result
    return wrapper
@calculator
def add(a,b):
    return a+b
add(5,5)
