km = int(input())
m = int(input())
if km*1000 > m:
    print(km)
elif km*1000 == m:
    print("Они равны")
elif km*1000<m:
    print(m)