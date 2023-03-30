def change(money, d, i):
    poc[i] += (money//d)
    money %= d
    if '5' in str(d):
        d //= 5
    else:
        d //= 2
    i += 1
    if d > 5:
        change(money, d, i)


for tc in range(1, int(input())+1):
    N = int(input())
    poc = [0] * 8
    i = 0
    d = 50000
    change(N, d, i)

    print(f'#{tc}')
    print(*poc)