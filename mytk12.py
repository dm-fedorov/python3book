import tkinter
# Вызывается в момент нажатия на кнопку:
def click():
  # Получаем строковое содержимое поля ввода с помощью метода get() 
  # C помощью config() можем изменить отображаемый текст
    label.config (text=entry.get())

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()
entry = tkinter.Entry(frame)
entry.pack()
label = tkinter.Label(frame)
label.pack()
# Привязываем обработчик нажатия на кнопку к функции click()
button = tkinter.Button(frame, text='Печать!', command=click) 
button.pack()
window.mainloop()
