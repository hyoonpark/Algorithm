def backtrack(row, score):
    global Min
    if score > Min:
        return
    if row == N:
        Min = min(Min, score)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            backtrack(row+1, score+lst[row][i])
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    Min = N * 99

    backtrack(0, 0)
    print(f'#{tc}', Min)