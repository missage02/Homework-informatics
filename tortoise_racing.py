from math import *
def cherepaha(v1,v2,g):
    t = g/(v2-v1)
    if v1>=v2:
        return 0
    else:
        return "В часах:",floor(t),".","В минутах:",floor(t*60),".","В секундах",floor(((t*60)-floor(t*60))*60)
print(cherepaha(720, 850, 70))