di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def absSum(lst, N):
    Sum = 0

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    Sum += abs(lst[i][j] - lst[ni][nj])

    return Sum



for tc in range(1, 11):
    N = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc}', absSum(num_lst, N))