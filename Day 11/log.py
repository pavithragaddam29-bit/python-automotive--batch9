def logfunction(func):
    def wrapper(*args,**kargs):
        print(f"calling function:{func.__name__}")
        result=func(*args,**kargs)
        print(f"function name:{func.__name__}")
        return result
    return wrapper
@logfunction
def greeting(name):
    return f"hello,{name}"
print(greeting("pavi"))