stroka1 ="яблоко"
stroka2 ="яблоко"
n = stroka1.replace(" ", "")
h = len(n)
y = stroka2.replace(" ", "")
count = 0
for i in n:
    if i in y:
        count +=1
if count == h and h==len(y):
        print("Анаграмма")
else:
        print("Не анаграмма" )
