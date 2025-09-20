a = int(input())
yr = int(input())
if a % 2 ==0 and a!=2:
    print(31)
elif a %2 != 0:
    print(30)
elif a==2 and yr % 4==0 and yr %100!=0 and yr %400 != 0 :
    print(29)
elif a==2 and yr % 4 != 0 or yr%100==0 or yr%400==0:
    print(28)