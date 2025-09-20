a = list(map(int, input().split()))
b = list(map(int, input().split()))
deleter = set(b)
arr = []
for x in a:
    if x not in deleter:
        arr.append(x)
print(arr)