from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def bfs(graph, N):
    # 시작 위치는 (0, 0)
    start = (0, 0)
    # 거리 정보를 저장할 2차원 리스트. 초기값은 큰 수로 설정
    dist = [[100000000]*N for _ in range(N)]
    dist[0][0] = 0  # 시작 위치의 거리는 0

    Q = deque()
    Q.append(start)

    while Q:
        i, j = Q.popleft()

        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0<=ni<N and 0<=nj<N:
                diff = 0
                if height[ni][nj] > height[i][j]:
                    diff = height[ni][nj] - height[i][j]
                if dist[i][j]+diff+1 < dist[ni][nj]:
                    dist[ni][nj] = dist[i][j] + diff + 1
                    Q.append((ni, nj))

    return dist[N-1][N-1]  # 도착 지점의 최소 비용을 반환


for tc in range(1, int(input())+1):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs(height, N)
    print(f'#{tc}', ans)
