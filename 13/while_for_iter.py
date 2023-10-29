x = [1, 2, 3]
# создаем итератор:
iterator = iter(x)
# уходим в бесконечный цикл:
while True:
    try:
        item = next(iterator) # перемещаемся по элементам
    except StopIteration: # итератор завершился
        del iterator
        break
    print(item)
