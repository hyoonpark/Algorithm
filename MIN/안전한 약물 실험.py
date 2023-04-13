def powerset(arr):
    n = len(arr)
    res = []
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if i & (1 << j)]
        res.append(subset)
    return [''.join(map(str, subset)) for subset in res]


N, K = map(int, input().split())
num_lst = [str(i) for i in range(1, N+1)]
toxic = input().split()
sets = powerset(num_lst)
cnt = 0
for st in sets:
    for tx in toxic:
        if tx in st:
            cnt += 1
            break
    # print(sets)
print(toxic)
ans = len(sets)-1
print(num_lst)
print(toxic)
print(sets)
print(ans)