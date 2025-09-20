def accum(stroka):
    arr = []
    cnt=0
    while cnt < len(stroka):
        xd = stroka[cnt]
        arr.append(xd.upper()+xd.lower()*cnt)
        cnt+=1
    return "-".join(arr)
print(accum("Rquasdt"))