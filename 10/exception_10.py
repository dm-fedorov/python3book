# exception_10.py
try:
    x = int(input("Введите число: "))
    print(5/x)
except Exception as err: # информация об ошибке записывается в err
    print(err)  # печатаем содержимое ошибки 
