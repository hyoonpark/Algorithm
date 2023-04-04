import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    s = []
    lst = list(input())
    if len(lst)%2:
        print('NO')
    else:
        for i in lst:
            if i == '(':
                s.append(i)
            elif not s and i == ')':
                print('NO')
                break
            elif s and i == ')':
                s.pop()
        else:
            if s:
                print('NO')
            else:
                print('YES')