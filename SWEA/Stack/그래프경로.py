def Route(S, G):
    # global graph, V
    stack = []
    visited = [0 for _ in range(V+1)]
    stack.append(S)

    while stack:
        s = stack.pop()
        visited[s] = 1
        for e in range(1, V+1):
            if visited[e] == 0:
                if graph[s][e] == 1:
                    stack.append(e)
    return visited[G]


for t in range(1, int(input())+1):
    V, E = map(int, input().split())  # node갯수, edge갯수
    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    for _ in range(E):  # 그래프 만들기
        i, j = map(int, input().split())
        graph[i][j] = 1

    S, G = map(int, input().split())  # start, goal
    print(f'#{t}', Route(S, G))