import tkinter
window = tkinter.Tk()
# Создаем объект класса StringVar и присваиваем указатель на него data
# (создаем строковую переменную, с которой умеет работать tkinter)
data = tkinter.StringVar()
# Метод set класса StringVar позволяет изменить содержимое переменной:
data.set ('Данные в окне')
# textvariable присваиваем ссылку на строковый объект из переменной data
label = tkinter.Label (window, textvariable = data)
label.pack()
window.mainloop() 
