di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def Balloon(lst, N, M):
    num_max = 0

    for i in range(N):
        for j in range(M):
            rslt = lst[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M:
                    rslt += lst[ni][nj]
            if rslt > num_max:
                num_max = rslt

    return num_max



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num_lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}', Balloon(num_lst, N, M))