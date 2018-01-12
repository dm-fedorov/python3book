import tkinter
window = tkinter.Tk()
# Создаем кнопку, изменяем шрифт с помощью кортежа
button = tkinter.Button(window, text='Hello',
                      font=('Courier', 14, 'bold italic'))
button.pack()
window.mainloop()
