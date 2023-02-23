crd = [[0 for _ in range(101)] for _ in range(101)]
ans = 0
for _ in range(4):
    lst = list(map(int, input().split()))
    for i in range(lst[1], lst[3]):
        for j in range(lst[0], lst[2]):
            crd[i][j] = 1
for x in crd:
    if 1 in x:
        ans += sum(x)
print(ans)