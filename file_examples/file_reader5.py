with open('example_text.txt', 'r') as file:
    contents = file.read(10)  # указываем кол-во символов для чтения
    # курсор перемещается на 11 символ
    rest = file.read()    # читаем с 11 символа
print("10:", contents)
print("остальное:", rest)
