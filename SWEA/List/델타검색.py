for t in range(1, 11):
    N = int(input())
    num_lst = [0 for _ in range(N)]
    for n in range(N):
        num_lst[n] = list(map(int, input().split()))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    result = 0
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(num_lst[i][j] - num_lst[ni][nj])
    print(f'#{t} {result}')




