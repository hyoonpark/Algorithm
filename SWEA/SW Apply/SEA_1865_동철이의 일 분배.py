def backtrack(row, power):
    global Max
    if power <= Max:
        return
    if row == N:
        Max = max(Max, power)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(row+1, power*power_lst[row][i])
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    power_lst = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    visited = [0] * N
    Max = 0

    backtrack(0, 100)

    print(f'#{tc} {Max:.6f}')