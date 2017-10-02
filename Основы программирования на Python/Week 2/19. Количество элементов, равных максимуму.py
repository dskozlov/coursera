n = int(input())
nMax = n
count = 1
while n != 0:
    n = int(input())
    if n > nMax:
        nMax = n
        count = 1
    elif n == nMax:
        count += 1
print(count)
