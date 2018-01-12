import tkinter

# Контроллер: функция вызывается в момент нажатия на кнопку
def click():
    # метод get() возвращает текущее значение counter 
    # метод set() устанавливает новое значение counter
    counter.set (counter.get() + 1)

window = tkinter.Tk()
# Модель: создаем объект класса IntVar
counter = tkinter.IntVar()
# Обнуляем созданный объект с помощью метода set()
counter.set (0)
frame = tkinter.Frame (window)
frame.pack()
# Создаем кнопку и указываем обработчик (функция click) при нажатии на нее 
button = tkinter.Button (frame, text='Click', command=click)
button.pack()
# Вид: в реальном времени обновляется содержимое виджета Label
label = tkinter.Label (frame, textvariable=counter)
label.pack()
window.mainloop()
