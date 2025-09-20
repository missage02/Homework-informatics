def words_to_number(words):
    mn = ["hundred", "thousand", "million"]
    tenTotwenty = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
                   "seventeen", "eighteen", "nineteen"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    nums = ["one", 'two', 'three', 'four', "five", 'six', "seven", "eight", "nine"]
    numbers = words.split()
    result = 0
    for num in numbers:
        if num in nums:
            result += (nums.index(num)+1)
        elif num in mn:
            if mn.index(num) == 0:
                result *= 100
            elif mn.index(num) == 1:
                result *= 1000
            else:
                result *= 1000000
        elif num in tenTotwenty:
            result += (tenTotwenty.index(num) + 10)
        elif num in tens:
            result += ((tens.index(num)+2)*10)
        elif '-' in num:
            new_num = num.split('-')
            result += ((tens.index(new_num[0])+2)*10) + (nums.index(new_num[1])+1)

    return result