try:
    x = int(input("Введите число: "))
    print(5/x)
except ZeroDivisionError as z:
    print("Обрабатываем исключение - деление на нуль!")
    print(z) # выводим на экран информацию об ошибке ZeroDivisionError
except ValueError as v:
    print("Обрабатываем исключение - преобразование типов!")
    print(v)
else:
    print("Выполняется, если не произошло исключительных ситуаций!")
finally:
    print("Выполняется всегда и в последнюю очередь!")
