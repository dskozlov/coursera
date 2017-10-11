a = input()

if a.find('f') == -1:
    print(-2)
else:
    f1 = a.find('f')
    f2 = a.find('f', f1+1)
    if f2 == -1:
        print(-1)
    else:
        print(f2)
