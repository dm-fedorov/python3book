class Person():
    name=""
    def __init__(self):  # конструктор базового класса
        print ("Создан человек")

class Employee (Person):
    job_title=""
    def __init__(self): # конструктор дочернего класса
        print ("Создан работник")

class Customer (Person):
    email=""
    def __init__(self):  # конструктор дочернего класса
        print ("Создан покупатель")

person1 = Person()
personEmployee = Employee()
personCustomer = Customer()
