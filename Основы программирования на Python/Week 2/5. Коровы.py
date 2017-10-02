A = int(input())
last = A % 10
if last == 1 and (A < 10 or A > 20):
    print(A, end=' korova')
elif last <= 4 and last != 0 and (A < 10 or A > 20):
    print(A, end=' korovy')
else:
    print(A, end=' korov')
