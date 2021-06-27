# exception_03.py
import exception_01
def my_function_1(x):
    import math
    result = try_div(x)
    if result is not None: 
        return result * math.pi
    return "Ошибка деления на ноль!"

print(my_function_1(5))
print(my_function_1(0)) 
