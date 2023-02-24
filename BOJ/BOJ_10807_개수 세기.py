N = int(input())
num_lst = list(map(int, input().split()))
inv = [0 for _ in range(201)]
for i in num_lst:
    inv[i+100] += 1
v = int(input()) + 100
ans = inv[v]
print(ans)
