# exception_04.py
import exception_03
def my_function_2(x):
    result = my_function_1(x)
    if result is not None:
        return result ** 3
    return "Ошибка деления на ноль!"

print(my_function_2(5))
print(my_function_2(0))
