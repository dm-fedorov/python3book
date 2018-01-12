for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'равно', x, '*', n//x)
            break
    else:
        # не удалось найти множитель
        print (n, '- простое число')
