def DFS(arr):
    sck = []
    visited = [0 for _ in range(100)]
    sck.append(0)

    while sck:
        elem = sck.pop()
        visited[elem] = 1
        for n in range(100):
            if visited[n] == 0 and arr[elem][n]:
                sck.append(n)

    return visited[99]



for _ in range(10):
    tc, total = map(int, input().split())
    graph = [[0 for _ in range(100)] for _ in range(100)]
    E = list(map(int, input().split()))
    for i in range(0, len(E), 2):
        graph[E[i]][E[i+1]] = 1

    print(f'#{tc}', DFS(graph))