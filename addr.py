addr_name = 'Иван Иванов'    
addr_line1 = 'Московский пр. 122' # адрес прописка
addr_line2 = ''                   # фактический адрес проживания
addr_city = 'Москва'
addr_state = 'Восточный'          # административный округ
addr_zip = '123678'               # индекс адреса прописки

def printAddress (name, line1, line2, city, state, zip_code):
    print (name)
    if (len (line1) > 0):
        print (line1)
    if (len (line2) > 0):
        print (line2)
    print (city+", "+state+" "+zip_code)
# Вызов функции, передача аргументов: 
printAddress(addr_name, addr_line1, addr_line2, addr_city, addr_state, addr_zip)


