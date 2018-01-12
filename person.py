class Person():
    name=""  # имя человека
class Employee (Person): # указываем базовый класс Person
    job_title=""   # наименование должности работника
class Customer (Person): # указываем базовый класс Person
    email=""       # почта клиента

person1 = Person()                        # создаем объект класса Person
person1.name = "Иван Петров"    # заполняем поле объекта

personEmployee = Employee() # создаем объект класса Employee
# поле name наследуется от класса Person:
personEmployee.name = "Петр Иванов"  
personEmployee.job_title = "Программист" 

personCustomer = Customer()
personCustomer.name = "Петр Петров" 
personCustomer.email = "me@me.ru"

print(person1.name, personEmployee.name, personEmployee.job_title, personCustomer.name, personCustomer.email)
