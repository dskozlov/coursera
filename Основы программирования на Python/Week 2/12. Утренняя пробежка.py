x = int(input())
y = int(input())
n = 0
while x * (1.1)**n < y:
    n += 1
else:
    print(n + 1)
