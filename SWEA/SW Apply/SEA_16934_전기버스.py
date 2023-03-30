def backtrack(s, cnt, charge):
    global Min
    if cnt >= Min:
        return
    if s == N-1:
        Min = min(Min, cnt)
        return
    if charge > 0:
        backtrack(s+1, cnt, charge-1)
    backtrack(s+1, cnt+1, lst[s]-1)


for tc in range(1, int(input())+1):
    N, *lst = list(map(int, input().split()))
    Min = N
    charge = lst[0]
    # visited = [0] * N

    backtrack(0, 0, charge)
    print(f'#{tc}', Min)
