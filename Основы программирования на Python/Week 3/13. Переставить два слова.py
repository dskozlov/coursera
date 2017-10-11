a = input()

p = a.find(' ')
f1 = a[:p]
f2 = a[(p+1):]
print(f2, f1)
