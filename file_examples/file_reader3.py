try:
    # освобождение ресурсов происходит автоматически 
    # внутри менеджера контекста:
    with open('1example_text.txt', 'r') as file:
        contents = file.read()
    print(contents)
except:
    print ("Ошибка открытия файла")
