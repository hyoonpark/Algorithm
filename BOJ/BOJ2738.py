N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        arr[i][j] = A[i][j] + B[i][j]
for lst in arr:
    print(*lst)