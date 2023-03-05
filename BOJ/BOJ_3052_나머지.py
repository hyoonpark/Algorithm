mod = []
for _ in range(10):
    mod.append(int(input())%42)
ans = len(set(mod))
print(ans)