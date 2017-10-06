import math
P = int(input())
X = int(input())
Y = int(input())

n = X + Y / 100
m = int(n * (1 + P / 100)*100)/100
print(int(m), round((m - int(m)) * 100))
