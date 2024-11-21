stroka1 ="яблоко"
stroka2 ="яблоко"
n = stroka1.replace(" ", "") #Убираем пробелы
h = len(n)
y = stroka2.replace(" ", "") #Убираем пробелы
count = 0
for i in n: #Проверяем символы
    if i in y: #Проверяем символы
        count +=1 #Увеличивааем счетчик
if count == h and h==len(y): #Сравниваем длину строчек
        print("Анаграмма")
else:
        print("Не анаграмма" )
