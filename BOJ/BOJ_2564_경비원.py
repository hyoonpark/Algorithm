M, N = map(int, input().split())
store = int(input())
crd = []
ans = 0
for _ in range(store):
    i, j = map(int, input().split())
    crd.append((i, j))
pos = tuple(map(int, input().split()))
