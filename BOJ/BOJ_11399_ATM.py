N = int(input())
times = list(map(int, input().split()))
times.sort()
for i in range(1, N):
    times[i] += times[i-1]
ans = sum(times)
print(ans)