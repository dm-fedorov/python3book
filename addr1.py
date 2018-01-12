addr_name = 'Иван Иванов'    
addr_line1 = 'Московский пр. 122' # адрес прописка
addr_line2 = 'Тихая ул. 12'       # фактический адрес проживания
addr_city = 'Москва'
addr_state = 'Восточный'          # административный округ
addr_zip = '123678'               # индекс адреса прописки
# добавим переменную, содержащую индекс адрес прописки
addr_zip2  = "678900"

def printAddress (name, line1, line2, city, state, zip_code, zip2):
    print (name)
    if (len (line1) > 0):
        print (line1)
    if (len (line2) > 0):
        print (line2)
    # добавили вывод на экран переменной zip2
    print (city+", "+state+" "+zip_code+" "+zip2)
# Добавили новый аргумент addr_zip2: 
printAddress(addr_name, addr_line1, addr_line2, addr_city, addr_state, addr_zip, addr_zip2)


