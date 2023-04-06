from collections import deque

N, K = map(int, input().split())
table = deque(i for i in range(1, N+1))
lst = []

print('<', end='')
for i in range(N):
    table.rotate(-K)
    if i == N-1:
        print(table.pop(), end='')
    else:
        print(table.pop(), end=', ')
print('>')