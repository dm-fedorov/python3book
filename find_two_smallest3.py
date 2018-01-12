def find_two_smallest (L):
    if L[0] < L[1]:           
        min1, min2 = 0, 1  # устанавливаем начальные значения
    else:
        min1, min2 = 1, 0

    for i in range (2, len (L)):
        if L[i] < L[min1]:  # «первый случай»
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:  # «второй случай»
            min2 = i
    return (min1, min2)
