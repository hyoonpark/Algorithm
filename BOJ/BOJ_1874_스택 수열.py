from collections import deque

n = int(input())
k = 1
num_lst = deque()
ans = deque()
S = deque()
made = deque()
for _ in range(n):
    num_lst.append(int(input()))
for i in range(n):
    j = num_lst[i]
    while k <= j:
        S.append(k)
        ans.append('+')
        k += 1
    made.append(S.pop())
    ans.append('-')
if made == num_lst:
    for i in ans:
        print(i)
else:
    print('NO')