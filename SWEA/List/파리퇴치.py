T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_lst = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        num_lst[n] = list(map(int, input().split()))
    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_num = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_num += num_lst[x][y]
            if max_num < sum_num:
                max_num = sum_num
    print(f'#{t}', max_num)
