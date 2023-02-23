def isRoute(lst, S, G):
    Sck = []
    visited = [0 for _ in range(V+1)]
    Sck.append(S)

    while Sck:
        elem = Sck.pop()
        visited[elem] = 1
        for n in range(1, V+1):
            if visited[n] == 0 and n_lst[elem][n] == 1:
                Sck.append(n)

    return visited[G]



for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    n_lst = [[0 for _ in range(V+1)] for _ in range(V+1)]   # 노드가 1 부터 시작
    for _ in range(E):
        i, j = map(int, input().split())
        n_lst[i][j] = 1
    S, G = map(int, input().split())

    print(f'#{tc}', isRoute(n_lst), S, G)