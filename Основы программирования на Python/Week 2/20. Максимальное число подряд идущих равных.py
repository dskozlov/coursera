n = int(input())
num = n
count = 1
count_max = 1
while n != 0:
    n = int(input())
    if n == num and count >= count_max:
        count += 1
        count_max = count
    elif n == num:
        count += 1
    else:
        count = 1
        num = n
print(count_max)
