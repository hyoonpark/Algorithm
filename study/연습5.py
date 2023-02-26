def Road(graph, start, goal):
    Q = []
    visited = [0] * (V+1)
    visited[start] = 1
    Q.append(start)

    while Q:
        n = Q.pop(0)
        for v in range(V+1):
            if not visited[v] and graph[n][v]:
                Q.append(v)
                visited[v] = visited[n] + 1

    return visited[goal] - visited[start]


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    ans = 0
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s][e], graph[e][s] = 1, 1
    S, G = map(int, input().split())
    ans = Road(graph, S, G)
    if ans < 0:
        ans = 0
    print(f'#{tc}', ans)