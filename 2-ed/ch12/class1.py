# class1.py
class Person:
    def __init__(self, name='Человек без имени'):
        self.name = name
        self.age = 0
    def say(self):
        print("{0} говорит".format(self.name))

class Employee(Person):
    def set_job(self, job_title='Безработный'):
        self.job_title = job_title        
    def get_job(self):
        print(self.job_title)
    
class Customer(Person):    
    def set_email(self, email='Нет почты'):
        self.email = email        
    def get_email(self):
        print(self.email)

person = Person('Иван')
person.say()

emp = Employee()
emp.say()
emp.get_job()
# хотим, чтобы в момент создания Employee
# заполнялась должность

cust = Customer('Петр')
cust.say()
cust.get_email()
# хотим, чтобы в момент создания Customer
# заполнялась почта
