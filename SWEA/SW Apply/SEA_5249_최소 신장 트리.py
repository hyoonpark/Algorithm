def find_set(x):
    while x != parent[x]:
        x = parent[x]
    return x


# def union(x, y):
#     rep[find_set(y)] = find_set(x)
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    tree_lst = [list(map(int, input().split())) for _ in range(E)]
    tree_lst.sort(key=lambda x:x[2])
    N = V + 1
    sm = 0
    cnt = 0
    for v1, v2, w in tree_lst:
        if find_set(v1) != find_set(v2):
            cnt += 1
            sm += w
            union(v1, v2)
            if cnt == N-1:
                break
    print(f'#{tc}', sm)