N = int(input())
move = list(map(int, input().split()))
arr = [i for i in range(1, N+1)]

for k in range(1, N):
    m = move[k]
    while m != 0:
        arr[k-1], arr[k] = arr[k], arr[k-1]
        m -= 1
        k -= 1

print(*arr)