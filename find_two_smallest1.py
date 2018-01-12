def find_two_smallest (L):
    smallest = min (L)
    min1 = L.index (smallest) 
    L.remove (smallest)   # удаляем первый минимальный элемент

    next_smallest = min (L)
    min2 = L.index (next_smallest)
    L.insert (min1, smallest)# возвращаем первый минимальный обратно
    # проверяем индекс второго минимального из-за смещения:
    if min1 <= min2: 
        min2 += 1    # min2 = min2 + 1

    return (min1, min2)  # возвращаем кортеж
