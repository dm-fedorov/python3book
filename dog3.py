class Dog():
    name=""
    # Конструктор вызывается в момент создания объекта этого класса
    def __init__ (self, newName):
        self.name = newName
    # Можем в любой момент вызвать метод и изменить имя собаки
    def setName (self, newName):
        self.name = newName
    # Можем в любой момент вызвать метод и узнать имя собаки
    def getName (self):
        return self.name # возвращаем текущее имя объекта

# Создаем собаку с начальным именем:
myDog = Dog ("Лайка")

# Выводим имя собаки:
print (myDog.getName())

# Установим новое имя собаки:
myDog.setName("Шарик")

# Посмотрим изменения имени:
print (myDog.getName())
