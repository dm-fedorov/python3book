try:
    x = int(input("Введите число: "))
    print(5/x)
except ZeroDivisionError:  # указываем тип исключения 
    print("Возникла ошибка деления на нуль")
except ValueError:
    print("Возникла ошибка преобразования типов")
