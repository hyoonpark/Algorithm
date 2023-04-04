def find_set(k):
    if parent[k] != k:
        parent[k] = find_set(parent[k])
    return parent[k]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    m_lst = list(map(int, input().split()))
    parent = [i for i in range(N+1)]
    for j in range(0, M*2, 2):
        union(m_lst[j], m_lst[j+1])
    ans = set()
    for p in parent:
        ans.add(find_set(p))
    ans = len(ans)-1
    print(f'#{tc}', ans)