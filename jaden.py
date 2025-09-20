text = str(input(""))
words = text.split()
arr = []
for a in words:
    a = a.capitalize()
    arr.append(a)

otvet=" ".join(arr)
print(otvet)
