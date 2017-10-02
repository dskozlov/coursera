n = int(input())
nMax = n
while n != 0:
    n = int(input())
    if nMax < n:
        nMax = n
print(nMax)
