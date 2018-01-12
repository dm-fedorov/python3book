s='aa3aBbb6ccc'
total=0
for i in range(len(s)):
    if s[i].isalpha():   # посимвольно проверяем наличие буквы
        continue  # инструкция перехода к следующему шагу цикла
    total=total+int(s[i]) # накапливаем сумму, если встретилась цифра

print ("сумма чисел:", total)
