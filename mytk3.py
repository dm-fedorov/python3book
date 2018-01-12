import tkinter
window = tkinter.Tk()
# Создаем фрейм в главном окне
frame = tkinter.Frame(window)
frame.pack()
# Создаем виджеты и помещаем их во фрейме frame
first = tkinter.Label (frame, text='First label')
# Отображаем виджет с помощью менеджера pack
first.pack()
second = tkinter.Label (frame, text='Second label')
second.pack()
third = tkinter.Label (frame, text='Third label')
third.pack()
window.mainloop() 
