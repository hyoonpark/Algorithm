T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_lst = [[0 for _ in range(N)] for _ in range(N)]
    for n in range(N):
        num_lst[n] = list(map(int, input().split()))