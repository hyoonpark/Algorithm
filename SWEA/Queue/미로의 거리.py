from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
def BFS():
    queue = deque([])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[row][col] = 1
    queue.append([row, col])

    while queue:
        crd = queue.pop()
        for k in range(4):
            ni = crd[0] + di[k]
            nj = crd[1] + dj[k]
            if 0<=ni<N and 0<=nj<N:
                if maze[ni][nj] == '3':
                    return visited[crd[0]][crd[1]] - visited[row][col]
                elif maze[ni][nj] == '0':
                    queue.appendleft([ni, nj])
                    visited[ni][nj] = visited[crd[0]][crd[1]] + 1
                    maze[crd[0]][crd[1]] = 1

    return 0




for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    for i in range(N):
        if '2' in maze[i]:
            row = i
            col = maze[i].index('2')
            break

    print(f'#{tc}', BFS())