for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    cus = [list(map(int, input().split())) for _ in range(N)]
    cus.sort()
    brd = [0] * (max(cus)+1)
    brd[M] = K
    if cus[0] < M:
        ans = 'Impossible'
    else:
        for i in range(len(cus)):
