def Bomb(i, j):
    rgn[i][j] = '%'
    for k in range(4):
        for l in range(1, K+1):
            ni = i + di[k]*l
            nj = j + dj[k]*l
            if 0<=ni<N and 0<=nj<M:
                if rgn[ni][nj] == '@':
                    Bomb(ni, nj)
                elif rgn[ni][nj] == '#':
                    break
                elif rgn[ni][nj] == '_':
                    rgn[ni][nj] = '%'




N, M = map(int, input().split())
K = int(input())
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
rgn = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if rgn[i][j] == '@':
            Bomb(i, j)

for ans in rgn:
    print(''.join(ans))