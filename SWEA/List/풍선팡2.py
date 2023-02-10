T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_lst = [[0 for _ in range(M)] for _ in range(N)]
    for n in range(N):
        num_lst[n] = list(map(int, input().split()))
    max_num = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(N):
        for j in range(M):
            result = num_lst[i][j]
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < N and 0 <= nj < M:
                    result += num_lst[ni][nj]
                if result > max_num:
                    max_num = result
    print(f'#{t}', max_num)