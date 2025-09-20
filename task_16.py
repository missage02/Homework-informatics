n=int(input())
numbers = input().split()
b=[0]*(n+1)
a=[0]*(n+1)
for guest in range(0,n+1):
    seat = int(numbers[guest - 1])
    b[seat] = guest
print(numbers)
print(b[1:])