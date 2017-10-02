A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A <= C <= B:
    A, B, C = A, C, B
elif B <= A <= C:
    A, B, C = B, A, C
elif B <= C <= A:
    A, B, C = B, C, A
elif C <= A <= B:
    A, B, C = C, A, B
elif C <= B <= A:
    A, B, C = C, B, A

if D <= E:
    D, E = E, D

if B <= D and A <= E:
    print('YES')
else:
    print('NO')
