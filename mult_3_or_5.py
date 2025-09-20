def mult_3_or_5(number):
    if number < 0:
        return 0

    cnt = 0
    for i in range(number):
        if i % 3 ==0 or i%5 ==0:
            cnt+=i
    return cnt