        FIBANACHI
fiblim = 4000000
a = 1
b = 2
otv = 0
while a<=fiblim:
    if a % 2 ==0:
        otv +=a
    sled = a + b
    a = b
    b = sled
print(otv)