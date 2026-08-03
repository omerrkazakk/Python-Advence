# #BONUS SECTİON :COMBINING DECORATORS
#
print("-"*60)
print("Bonus Section: Combining Decorators")
print("-"*60)

def multiply_decorator(func):
    def wrapper(x:int):
        return func(x)*2
    return wrapper

def other_decorator(func):
    def wrapper(x:int):
        return func(x)*4
    return wrapper

@other_decorator
@multiply_decorator
def calculate(x:int):
    return x*2

print(calculate(100))