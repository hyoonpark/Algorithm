from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def BFS(graph, y, x):
    queue = deque([])
    queue.append([y, x])
    maze[y][x] = 1

    while queue:
        crd = queue.pop()
        for k in range(4):
            ni = crd[0] + di[k]
            nj = crd[1] + dj[k]
            if maze[ni][nj] == '3':
                return 1
            elif maze[ni][nj] == '0':
                queue.appendleft([ni, nj])
                maze[crd[0]][crd[1]] = 1

    return 0



for _ in range(10):
    tc = int(input())
    maze = [list(input()) for _ in range(100)]

    print(f'#{tc}', BFS(maze, 1, 1))