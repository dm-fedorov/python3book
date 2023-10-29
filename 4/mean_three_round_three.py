# mean_three_round_three.py
def mean_three_round_three(x, y, z):
    """Вычисляет среднее арифметическое трех чисел, 
    округленное до трех знаков после запятой.
    >>> mean_three_round_three(20, 30, 70)
    40.0
    >>> mean_three_round_three(1, 5, 8)
    4.667
    """
    return round((x + y + z) / 3, 3)

if __name__ == "__main__":
    import doctest
    #	автоматически проверяет тесты в документации: 
    doctest.testmod()