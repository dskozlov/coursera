import math as m
n = float(input())

if 0 < n - int(n) < 0.5:
    print(m.floor(n))
elif int(n) >= 0.5:
    print(m.ceil(n))
elif int(n) <= -0.5:
    print(m.floor(n))
else:
    print(m.ceil(n))
