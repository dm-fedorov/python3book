# exception_01.py
def try_div(x):
    """
    Функция возвращает результат деления.
    В случае возникновения ошибки вернет None.
    """
    if x:
        return 5 / x 
    # else: return None

print(try_div(5))
print(try_div(0)) # ошибка, поэтому функция вернет None
