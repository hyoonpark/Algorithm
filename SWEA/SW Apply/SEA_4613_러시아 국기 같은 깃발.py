for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    minV = N*M
    for i in range(N-2):
        for j in range(i+1, N-1):
            cnt = 0
            for y in range(i+1):
                for x in range(M):
                    if flag[y][x] != 'W':
                        cnt += 1
            for y in range(i+1, j+1):
                for x in range(M):
                    if flag[y][x] != 'B':
                        cnt += 1
            for y in range(j+1, N):
                for x in range(M):
                    if flag[y][x] != 'R':
                        cnt += 1
            minV = min(minV, cnt)
    print(f'#{tc}', minV)