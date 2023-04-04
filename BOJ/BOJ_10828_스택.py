import sys

N = int(sys.stdin.readline())
s = []
top = -1
for _ in range(N):
    lst = sys.stdin.readline().split()
    a = lst[0]
    if a == 'push':
        s.append(int(lst[1]))
        top += 1
    elif a == 'pop':
        if s:
            print(s.pop())
            top -= 1
        else:
            print(-1)
    elif a == 'size':
        print(len(s))
    elif a == 'empty':
        if s:
            print(0)
        else:
            print(1)
    elif a == 'top':
        if s:
            print(s[top])
        else:
            print(-1)