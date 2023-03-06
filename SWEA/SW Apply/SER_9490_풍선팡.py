di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def pang(i, j):
    global mx
    temp = ballon[i][j]
    x = ballon[i][j]
    for a in range(1, x+1):
        for k in range(4):
            ni = i + di[k]*a
            nj = j + dj[k]*a
            if 0<=ni<N and 0<=nj<M:
                temp += ballon[ni][nj]
    mx = max(mx, temp)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ballon = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(M):
            pang(i, j)
    print(f'#{tc}', mx)