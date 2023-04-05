from collections import deque
import sys

N = int(sys.stdin.readline())
dq = deque()
for _ in range(N):
    lst = sys.stdin.readline().split()
    a = lst[0]
    if a == 'push':
        dq.append(int(lst[1]))
    elif a == 'pop':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif a == 'size':
        print(len(dq))
    elif a == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    elif a == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)