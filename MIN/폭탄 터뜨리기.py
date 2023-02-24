'''
0. 문자열의 2차원 배열을 받고, 델타이동을 활용할 수 있다.
1. 격자의 크기를 잘 확인하여 2차원 배열 받기.
'''

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def Bomb(i, j):
    rgn[i][j] = '%'    # 폭탄 터진 구역 표시
    for k in range(4):
        for l in range(1, K+1):    # 폭탄의 화력까지 탐색
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
rgn = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if rgn[i][j] == '@':    # 그 지역에 폭탄이 있다면
            Bomb(i, j)

for ans in rgn:
    print(''.join(ans))