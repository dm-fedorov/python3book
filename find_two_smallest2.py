def find_two_smallest (L):
    temp_list = sorted (L)  # возвращаем КОПИЮ отсортированного списка
    smallest = temp_list [0]   
    next_smallest = temp_list [1]
    min1 = L.index (smallest)
    min2 = L.index (next_smallest)
    return (min1, min2)
