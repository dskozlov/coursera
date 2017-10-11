a = input()

first = a.find('f')
last = a[::-1].find('f')
last = len(a) - last - 1
if first != last and first != -1:
    print(first, last)
elif first != -1:
    print(first)
