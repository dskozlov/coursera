n = int(input())
nMax = n
m = int(input())
nMax2 = m
if m > n:
    nMax2, nMax = nMax, nMax2
while n != 0:
    n = int(input())
    if n > nMax:
        nMax2 = nMax
        nMax = n
    elif nMax >= n > nMax2:
        nMax2 = n
print(nMax2)
