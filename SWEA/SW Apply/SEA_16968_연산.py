from collections import deque
def bfs(N, M):
    Q = deque([(N, 0)])
    visited = [0] * 1000001
    visited[N] = 1

    while Q:
        num, cnt = Q.popleft()
        if num == M:
            return cnt
        if num*2 <= 1000000 and not visited[num*2]:
            visited[num*2] = 1
            Q.append((num*2, cnt+1))
        if num+1 <= 1000000 and not visited[num+1]:
            visited[num+1] = 1
            Q.append((num+1, cnt+1))
        if num-1 >= 0 and not visited[num-1]:
            visited[num-1] = 1
            Q.append((num-1, cnt+1))
        if num-10 >= 0 and not visited[num-10]:
            visited[num-10] = 1
            Q.append((num-10, cnt+1))



for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    ans = bfs(N, M)
    print(f'#{tc}', ans)