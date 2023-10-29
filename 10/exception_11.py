# exception_11.py
def get_int(msg):
    while True:
        try:
            x = int(input(msg))
            return x
        except ValueError:
            print("Ошибка преобразования типов")

get_int("Введите целое число: ")
