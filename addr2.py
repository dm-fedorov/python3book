class Address():  # имя класса выбирает программист
    name=""       # строковое поле класса 
    line1=""
    line2=""
    city=""
    state=""
    zip_code=""

homeAddress = Address()

# заполняем поле name объекта homeAddress:
homeAddress.name="Иван Иванов"  
homeAddress.line1="'Московский пр. 122"
homeAddress.line2="Тихая ул. 12"
homeAddress.city="Москва"
homeAddress.state="Восточный"
homeAddress.zip_code="123678" 

# переменная содержит адрес объекта класса Address:
vacationHomeAddress = Address()  

vacationHomeAddress.name="Иван Иванов" 
vacationHomeAddress.line1="пр.Мира 12"
vacationHomeAddress.line2=""
vacationHomeAddress.city="Коломна"
vacationHomeAddress.state="Центральный район"
vacationHomeAddress.zip_code="12489"

print ("Основной адрес проживания "+homeAddress.city)
print ("Адрес загородного дома "+vacationHomeAddress.city)

def printAddress(address): # передаем в функцию объект
    print (address.name)   # выводим на экран поле объекта
    if (len (address.line1) > 0):
        print (address.line1)
    if (len (address.line2) > 0):
        print (address.line2)
    print(address.city+", "+address.state+" "+address.zip_code)

printAddress (homeAddress)
printAddress (vacationHomeAddress)
