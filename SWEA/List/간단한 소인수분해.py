T = int(input())

for i in range(1, T+1):
    N = int(input())
    a = b = c = d = e = 0
    while N % 2 == 0:
        a += 1
        N //= 2
    while N % 3 == 0:
        b += 1
        N //= 3
    while N % 5 == 0:
        c += 1
        N //= 5
    while N % 7 == 0:
        d += 1
        N //= 7
    while N % 11 == 0:
        e += 1
        N //= 11
    print(f'#{i}', a, b, c, d, e)