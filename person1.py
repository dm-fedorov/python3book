class Person():
    name=""
    def __init__ (self): # конструктор базового класса
        print("Создан человек")

class Employee (Person):
    job_title=""

class Customer (Person):
    email=""

person1 = Person()
personEmployee = Employee()
personCustomer = Customer()
