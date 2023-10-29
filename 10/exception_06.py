# exception_06.py
import exception_05
try:
    print(my_function_2(0))
except ZeroDivisionError:
    print("Ошибка деления на ноль!")
