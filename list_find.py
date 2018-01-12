def list_find(lst, target):
    try:
        index = lst.index(target) 
    # метод index генерирует исключение ValueError:
    except ValueError:
    ## ValueError: value is not in list        
        index = -1
    return index

print (list_find([3,5,6,7], -6))
