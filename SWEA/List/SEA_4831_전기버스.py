T = int(input())

for i in range(1, T+1):
    K, N, M = map(int, input().split())
    M_idx = list(map(int, input().split()))
    now = 0
    charge = 0
    stops = [0] * (N+1)
    for j in M_idx:
        stops[j] = 1
    while now + K < N:
        max_idx = now
        for k in range(1, K+1):
            if stops[k+now] == 1:
                max_idx = now + k
        if max_idx == now:
            charge = 0
            break
        charge += 1
        now = max_idx


    print(f'#{i} {charge}')


