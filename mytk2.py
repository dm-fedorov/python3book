import tkinter
window = tkinter.Tk()
# Создаем объект-виджет класса Label в корневом окне window
# text – параметр для задания отображаемого текста
label = tkinter.Label (window, text = "Это текст в окне!")
# Отображаем виджет с помощью менеджера pack
label.pack()
window.mainloop()
