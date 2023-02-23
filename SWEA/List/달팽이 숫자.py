T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for t in range(1, T+1):
    N = int(input())
    N_lst = [[0 for _ in range(N)] for _ in range(N)]
    sN = N ** 2
    i = 0
    j = 0
