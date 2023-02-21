from collections import deque

def BFS(graph, start, goal):
    queue = deque([])
    visited = [0] * (V + 1)
    visited[start] = 1
    queue.append(start)

    while queue:
        node = queue.pop()
        for v in range(V+1):
            if not visited[v] and graph[node][v]:
                queue.appendleft(v)
                visited[v] = visited[node] + 1


    return visited[goal] - visited[start]






for tc in range(1, int(input())+1):
    V, E = map(int, input().split())    # node, edge
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j], graph[j][i] = 1, 1    # 방향성 없으니까

    S, G = map(int, input().split())    # 출발, 도착

    ans = BFS(graph, S, G)
    if ans < 0:
        ans = 0
    print(f'#{tc}', ans)