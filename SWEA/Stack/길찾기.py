def Route(S, G):
    stack = []
    visited = [0 for _ in range(100)]
    stack.append(S)

    while stack:
        s = stack.pop()
        visited[s] = 1
        for e in range(100):
            if visited[e] == 0:
                if graph[s][e] == 1:
                    stack.append(e)
    return visited[G]


for _ in range(10):
    T, E = map(int, input().split())
    graph = [[0 for _ in range(100)] for _ in range(100)]
    route_list = list(map(int, input().split()))
    for i in range(0, 2 * E, 2):
        route = route_list[i:i+2]
        graph[route[0]][route[1]] = 1

    print(f'#{T}', Route(0, 99))