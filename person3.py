class Person():
    name=""
    def __init__ (self):
        print ("Создан человек")

class Employee (Person):
    job_title=""
    def __init__ (self):
        Person.__init__ (self) # вызываем конструктор базового класса
        print ("Создан работник")

class Customer(Person):
    email=""
    def __init__ (self):
        Person.__init__ (self) # вызываем конструктор базового класса
        print ("Создан покупатель")

person1 = Person()
personEmployee = Employee()
personCustomer = Customer()
