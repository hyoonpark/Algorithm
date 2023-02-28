di = [-1, 1, 0, 0, -1, 1, 1, -1]
dj = [0, 0, -1, 1, 1, 1, -1, -1]
def killer(i, j):
    global mx
    cnt1 = fly[i][j]
    cnt2 = fly[i][j]

    for m in range(1, M):
        for k in range(4):
            ni = i + di[k]*m
            nj = j + dj[k]*m
            if 0<=ni<N and 0<=nj<N:
                cnt1 += fly[ni][nj]

        for k in range(4, 8):
            ni = i + di[k]*m
            nj = j + dj[k]*m
            if 0<=ni<N and 0<=nj<N:
                cnt2 += fly[ni][nj]

    if cnt1>=cnt2 and cnt1>mx:
        mx = cnt1
    elif cnt2>=cnt1 and cnt2>mx:
        mx = cnt2




for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(N):
            killer(i, j)
    print(f'#{tc}', mx)