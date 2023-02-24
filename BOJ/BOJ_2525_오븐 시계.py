A, B = map(int, input().split())
C = int(input())
D, E = divmod(B+C, 60)
A = A + D
B = E
if A >= 24:
    A -= 24
print(A, B)