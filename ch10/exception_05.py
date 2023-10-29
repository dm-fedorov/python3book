# exception_05.py
def try_div_raise(x):
    if x:
        return 5 / x
    else:
        # генерируем исключение:
        raise ZeroDivisionError 

def my_function_1(x):
    import math
    return try_div_raise(x) * math.pi

def my_function_2(x):
    return my_function_1(x) ** 3

print(my_function_2(0))
