M, N = map(int, input().split())
c = int(input())
row = []
col = []
for _ in range(c):
    a, b = map(int, input().split())
    if a:
        col.append(b)
    else:
        row.append(b)
if row:
    row.sort()
    if N-row[-1] > row[0]:
        r_mx = N - row[-1]
    else:
        r_mx = row[0]
    for i in range(0, len(row)-1):
        if (i+1) < len(row):
            h = row[i+1] - row[i]
            if h >= r_mx:
                r_mx = h
else:
    r_mx = N
if col:
    col.sort()
    if M - col[-1] > col[0]:
        c_mx = M - col[-1]
    else:
        c_mx = col[0]
    for j in range(0, len(col) - 1):
        if (j + 1) < len(col):
            w = col[j + 1] - col[j]
            if w >= c_mx:
                c_mx = w
else:
    c_mx = M
ans = r_mx * c_mx
print(ans)