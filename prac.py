
from queue import PriorityQueue

t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)] # visited 배열 초기화
    costs = [[float('inf')] * n for _ in range(n)]
    costs[0][0] = 0
    q = PriorityQueue()
    q.put((0, 0, 0))

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    while not q.empty():
        cost, x, y = q.get()

        if visited[x][y]:
            continue
        visited[x][y] = True

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + max(0, maze[nx][ny] - maze[x][y]) + 1

                if not visited[nx][ny] and costs[nx][ny] > new_cost:
                    costs[nx][ny] = new_cost
                    q.put((new_cost, nx, ny))

    print("#{} {}".format(test_case, costs[n-1][n-1]))