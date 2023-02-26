def DFS(S, G):
    stack = []
    visited = [0] * 100
    stack.append(S)
    visited[S]


    while stack:
        n = stack.pop()
        for num in range(100):
            if not visited[num] and num_lst[n][num]:
                stack.append(num)
                visited[num] = 1

    return visited[G]


for _ in range(10):
    tc, N = map(int, input().split())
    num_lst = [[0 for _ in range(100)] for _ in range(100)]
    e_lst = list(map(int, input().split()))
    for e in range(0, N*2, 2):
        num_lst[e_lst[e]][e_lst[e+1]] = 1
    ans = DFS(0, 99)
    print(f'#{tc}', ans)

# def DFS(arr):
#     sck = []
#     visited = [0 for _ in range(100)]
#     sck.append(0)
#
#     while sck:
#         elem = sck.pop()
#         visited[elem] = 1
#         for n in range(100):
#             if visited[n] == 0 and arr[elem][n]:
#                 sck.append(n)
#
#     return visited[99]
#
#
# for _ in range(10):
#     tc, total = map(int, input().split())
#     graph = [[0 for _ in range(100)] for _ in range(100)]
#     E = list(map(int, input().split()))
#     for i in range(0, len(E), 2):
#         graph[E[i]][E[i + 1]] = 1
#
#     print(f'#{tc}', DFS(graph), len(E))