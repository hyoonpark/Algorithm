from collections import deque

N, M = map(int, input().split())
S = deque()
cnt = 0
for _ in range(N):
    S.append(input())
for _ in range(M):
    chrs = input()
    if chrs in S:
        cnt += 1
    else:
        continue
print(cnt)