def BFS():
    queue = []
    visited = [0] * 101
    queue.append(S)
    visited[S] = 1

    while queue:
        node = queue.pop(0)
        for w in range(1, 101):
            if contact[node][w] and visited[w] == 0:
                queue.append(w)
                visited[w] = visited[node] + 1

    Max = max(visited)
    for last in range(100, 0, -1):
        if visited[last] == Max:
            return last
            break



for tc in range(1, 11):
    V, S = map(int, input().split())    # 노드의 갯수와 시작점
    num_lst = list(map(int, input().split()))
    E = len(num_lst) // 2    # 간선의 갯수
    contact = [[0 for _ in range(101)] for _ in range(101)]
    for i in range(E):
        s, e = num_lst[2*i], num_lst[2*i+1]
        contact[s][e] = 1

    print(f'#{tc}', BFS())