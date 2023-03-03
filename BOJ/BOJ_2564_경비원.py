'''
0. 이게 맞나 싶고... 줄일 수 있는 방법이 있을 거 같은데
'''

M, N = map(int, input().split())
store = int(input())
crd = []
ans = 0
for _ in range(store):
    i, j = map(int, input().split())
    crd.append((i, j))
pos = tuple(map(int, input().split()))
for tu in crd:
    if pos[0] == 1:
        if tu[0] == 1:
            ans += abs(pos[1]-tu[1])
        elif tu[0] == 2:
            cnt1 = pos[1] + N + tu[1]
            cnt2 = abs(pos[1]-M) + N + abs(tu[1]-M)
            ans += min(cnt1, cnt2)
        elif tu[0] == 3:
            ans += (pos[1]+tu[1])
        elif tu[0] == 4:
            ans += (abs(pos[1]-M)+tu[1])
    elif pos[0] == 2:
        if tu[0] == 2:
            ans += abs(pos[1]-tu[1])
        elif tu[0] == 1:
            cnt1 = pos[1] + N + tu[1]
            cnt2 = abs(pos[1]-M) + N + abs(tu[1]-M)
            ans += min(cnt1, cnt2)
        elif tu[0] == 3:
            ans += (pos[1]+abs(tu[1]-N))
        elif tu[0] == 4:
            ans += (abs(pos[1]-M)+abs(tu[1]-N))
    elif pos[0] == 3:
        if tu[0] == 3:
            ans += abs(pos[1] - tu[1])
        elif tu[0] == 4:
            cnt1 = pos[1] + M + tu[1]
            cnt2 = abs(pos[1]-N) + M + abs(tu[1]-N)
            ans += min(cnt1, cnt2)
        elif tu[0] == 1:
            ans += (pos[1] + tu[1])
        elif tu[0] == 2:
            ans += (abs(pos[1]-N) + tu[1])
    elif pos[0] == 4:
        if tu[0] == 4:
            ans += abs(pos[1] - tu[1])
        elif tu[0] == 3:
            cnt1 = pos[1] + M + tu[1]
            cnt2 = abs(pos[1]-N) + M + abs(tu[1]-N)
            ans += min(cnt1, cnt2)
        elif tu[0] == 1:
            ans += (pos[1] + abs(tu[1]-M))
        elif tu[0] == 2:
            ans += (abs(pos[1]-N) + abs(tu[1]-M))
print(ans)