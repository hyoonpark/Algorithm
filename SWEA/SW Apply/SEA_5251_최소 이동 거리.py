def dijkstra():
    dist = [987654321] * (N + 1)
    visited = [0] * (N + 1)
    # 시작 node 거리표시
    dist[0] = 0

    for _ in range(N):
        minIdx = -1
        MIN = 987654321
        # 방문표시와 MIN값 갱신
        for i in range(N + 1):
            # 방문하지 않았고, MIN보다 더 짧다면 MIN값 갱신
            if not visited[i] and MIN > dist[i]:
                MIN = dist[i]
                minIdx = i
        # min값 방문표시
        visited[minIdx] = 1

        # 갱신한 MIN에서 j로 향할때 더 작은 값이 있으면 dist를 더 작은값으로 바꿔줌
        for j in range(N + 1):
            # 방문하지 않았고, min에서 j로 향하는 값이 더 작은게 있다면 dist[j] 갱신
            if not visited[j] and dist[j] > adj[minIdx][j] + dist[minIdx]:
                dist[j] = adj[minIdx][j] + dist[minIdx]
    return dist[N]


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[987654321] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    print(f'#{tc}', dijkstra())