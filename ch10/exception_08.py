# exception_08.py
try:
    x = int(input("Введите число: "))
    print(5/x)
except ZeroDivisionError:
    print("Ошибка деления на ноль!!!")
except ValueError:
    print("Ошибка преобразования типа!!!")
