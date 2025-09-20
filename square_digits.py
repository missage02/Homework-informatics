a = int(input())
stroka = str(a)
stroka1 = ""
for b in stroka:
    stroka1 += str(int(b)**2)
otvet = int(stroka1)
print(otvet)