a = input()

first = a.find('h')
last = a[::-1].find('h')
last = len(a) - last
print(a[:first], a[last:], sep='')
