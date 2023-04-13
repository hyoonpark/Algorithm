crd = []
for _ in range(6):
    i, j = map(int, input().split())
    crd.append((i, j))
# print(crd)
cnt = 10000
if crd[2][0] == crd[0][0] or crd[5][0] == crd[0][0] or crd[2][1] == crd[0][1] or crd[5][1] == crd[0][1]:
    if crd[2][0] == crd[1][0] or crd[5][0] == crd[1][0] or crd[2][1] == crd[1][1] or crd[5][1] == crd[1][1]:
        cnt = 0
    elif crd[2][1]<=crd[1][1]<=crd[5][1]:
        x1 = abs(crd[2][0]-crd[1][0])
        x2 = abs(crd[3][0]-crd[1][0])
        y1 = abs(crd[5][1]-crd[1][1])
        y2 = abs(crd[2][1]-crd[1][1])
        cnt = min(x1, x2, y1, y2)
    elif crd[2][0]<=crd[1][0]<=crd[3][0]:
        x1 = abs(crd[2][0] - crd[1][0])
        x2 = abs(crd[3][0] - crd[1][0])
        y1 = abs(crd[5][1] - crd[1][1])
        y2 = abs(crd[2][1] - crd[1][1])
        cnt = min(x1, x2, y1, y2)
    else:
        x1 = abs(crd[2][0] - crd[1][0])
        x2 = abs(crd[3][0] - crd[1][0])
        y1 = abs(crd[3][1] - crd[1][1])
        y2 = abs(crd[4][1] - crd[1][1])
        cnt = min(x1, x2) + min(y1, y2)
elif crd[2][1]<=crd[1][1]<=crd[5][1]:
    if crd[2][1]<=crd[0][1]<=crd[5][1]:
        x1 = abs(crd[2][0]-crd[0][0])
        x2 = abs(crd[3][0]-crd[0][0])
        cnt = min(x1, x2)
    elif crd[2][0]<=crd[0][0]<=crd[3][0]:
        y1 = abs(crd[3][1]-crd[0][1])
        y2 = abs(crd[4][1]-crd[0][1])
        cnt = min(y1, y2)
    else:
        x1 = abs(crd[2][0] - crd[0][0])
        x2 = abs(crd[3][0] - crd[0][0])
        y1 = abs(crd[3][1] - crd[0][1])
        y2 = abs(crd[4][1] - crd[0][1])
        cnt = min(x1, x2) + min(y1, y2)
    dx1 = abs(crd[2][0]-crd[1][0])
    dx2 = abs(crd[3][0] - crd[1][0])
    cnt += min(dx1, dx2)
elif crd[2][0]<=crd[1][0]<=crd[3][0]:
    if crd[2][1]<=crd[0][1]<=crd[5][1]:
        x1 = abs(crd[2][0]-crd[0][0])
        x2 = abs(crd[3][0]-crd[0][0])
        cnt = min(x1, x2)
    elif crd[2][0]<=crd[0][0]<=crd[3][0]:
        y1 = abs(crd[3][1]-crd[0][1])
        y2 = abs(crd[4][1]-crd[0][1])
        cnt = min(y1, y2)
    else:
        x1 = abs(crd[2][0] - crd[0][0])
        x2 = abs(crd[3][0] - crd[0][0])
        y1 = abs(crd[3][1] - crd[0][1])
        y2 = abs(crd[4][1] - crd[0][1])
        cnt = min(x1, x2) + min(y1, y2)
    dy1 = abs(crd[3][1] - crd[1][1])
    dy2 = abs(crd[4][1] - crd[1][1])
    cnt += min(dy1, dy2)

cnt2 = abs(crd[0][0]-crd[1][0]) + abs(crd[0][1]-crd[1][1])
ans = min(cnt, cnt2)
print(ans)