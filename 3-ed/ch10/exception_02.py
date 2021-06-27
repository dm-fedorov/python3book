# exception_02.py
import exception_01
a = 5
result = try_div(a)
if result is not None: # проверяем ошибочную ситуацию
    print(result)
else:
    print("Ошибка деления на ноль!")
