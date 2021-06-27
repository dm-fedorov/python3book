# exception_07.py
def my_function_1(x):
    import math
    return 5/x * math.pi

def my_function_2(x):
    return my_function_1(x) ** 3

try:
    print(my_function_2(0))
except ZeroDivisionError:
    print("Ошибка деления на ноль!")
