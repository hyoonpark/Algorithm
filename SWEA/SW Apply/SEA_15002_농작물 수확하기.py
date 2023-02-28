for tc in range(1, int(input())+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    c = N//2
    cnt = 0
    x = N
    for i in range(c, -1, -1):
        for j in range(c-i, c-i+x):
            cnt += int(field[i][j])
            # print(field[i][j], end=' ')
        x -= 2
    k = N - 2
    for i in range(c+1, N):
        for j in range(i-c, i-c+k):
            cnt += int(field[i][j])
            # print(field[i][j], end=' ')
        k -= 2

    print(f'#{tc}', cnt)